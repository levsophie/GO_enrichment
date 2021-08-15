import sys 
sys.path.append('.')
from add_go_from_higherup import enrich_cnag_map
import copy
from scipy.stats import hypergeom, fisher_exact
from go_processing import list_names_for_terms
from from_uniprot_get_go import create_all_go_map
import numpy as np
from parse_client_input import parse

def create_empty_go_map():
    '''Creates an empty dictionary of all GOs as keys'''
    f = open('GO_names.txt', 'r')
    names = {}
    empty_GO_map = {}
    for line in f:
        line = line.strip('\n')
        line = line.split('\t')
        empty_GO_map[line[0]] = []
        names[line[0]] = line[1]
    f.close()
    return empty_GO_map, names

def process_gene_list(GO_map, cnag_list):
    '''Processes a given CNAG list assigning each GO group (key) a number of genes from the list (value).
    The GO_map is initially empty dictionary of all GO groups, get filled with the unique cnag_list profile.'''
    f = open("CNAG_to_GO.txt", "r")
    CNAG_GO_map = {}
    for line in f:
        line = line.strip('\n')
        line = line.split('\t')
        CNAG_GO_map[line[0]] = line[1:]
    annotated_count = 0
    not_annotated_count = 0
    number_of_annotations = 0
    for cnag in cnag_list:
        if cnag in CNAG_GO_map:
            annotated_count += 1
            for term in CNAG_GO_map[cnag]:
                GO_map[term].append(cnag)
                number_of_annotations += 1
        else:
            not_annotated_count += 1
    f.close()
    # print(f'Assigned {annotated_count} genes to GO groups, did not assign {not_annotated_count} genes.')
    return GO_map, number_of_annotations

def create_all_genes_control():
    '''Creates a list of all CNAGs from the file prepared from the UniProt source file.'''
    f = open("CNAG_to_func.txt", "r")
    gene_func = {}
    for line in f:
        line = line.split('\t')
        cnag = line[0][:10]
        gene_func[cnag] = line[1].rstrip('\n')
    f.close()
    # print(f'total number of genes is {len(gene_func.keys())}')
    return gene_func

def find_enriched_groups(sample_test, sample_control, number_of_control_annotations,
                                           number_of_test_annotations, GO_map, definitions, significance):
    
    enriched_groups = []
    id = 0
    for term in GO_map.keys():
        if len(sample_test[term]) > 0:
            # print(len(sample_test[term]), len(sample_control[term]), term)
            a = len(sample_test[term])  
            b = len(sample_control[term]) - a
            c = number_of_test_annotations - a
            d = number_of_control_annotations - len(sample_control[term]) - c
            # print(a,b,c,d)
            _, p = fisher_exact(np.array([[a,b],[c,d]]))
            if p < significance:
                id += 1
                # print(a,b,c,d)
                enriched_groups.append({'id': id, 'pvalue': round(p, 10),
                                        'test': a, 'control': b, 'term': term,
                                        'description': definitions[term]})
    return sorted(enriched_groups, key = lambda i: i['pvalue'])


def more_GO_info(term_of_interest, definitions, all_genes_control, sample_test, sample_control):
    while term_of_interest:
        term_of_interest = term_of_interest.strip(' ').rstrip(' ')
        try:
            print(f'Sample genes for GO term {term_of_interest}, {definitions[term_of_interest]}')
            for gene in sample_test[term_of_interest]:
                print(gene, '\t', all_genes_control[gene])
            print(f'\nControl genes for term {term_of_interest}, {definitions[term_of_interest]}')
            for gene in sample_control[term_of_interest]:
                if not gene in sample_test[term_of_interest]:
                    print(gene, '\t', all_genes_control[gene])
        except:
            print('Wrong input, exiting...')
        term_of_interest = input('\nList genes for another GO term? Please copy and paste the term, otherwise "Enter"\n')


def main_endpoint(test_input, control_input, significance):
    print('Processing request...')
    # The GO_map is initially empty dictionary of all GO groups, gets filled with the unique cnag_list profile.'''
    GO_map, definitions = create_empty_go_map()
       
    # Operations on all genes control
    all_genes = copy.deepcopy(GO_map)
    all_genes_list = create_all_genes_control().keys()  # uses full list of GO-annotated CNAG numbers
    all_genes_control, number_of_all_annotations = process_gene_list(all_genes, all_genes_list)

    # Operations on the test list
    test = copy.deepcopy(GO_map)
    test_gene_list = parse(test_input)
    sample_test, number_of_test_annotations = process_gene_list(test, test_gene_list)  # sample_test['GO:0005829'] == 1
    enriched_groups_test = find_enriched_groups(sample_test, all_genes_control, number_of_all_annotations,
                                           number_of_test_annotations, GO_map, definitions, significance=float(significance))
    
    # Operations on the control list
    if control_input:
        control = copy.deepcopy(GO_map)
        control_gene_list = parse(control_input)
        sample_control, number_of_control_annotations = process_gene_list(control, control_gene_list)
        enriched_groups_control = find_enriched_groups(sample_control, all_genes_control, number_of_all_annotations,
                                           number_of_control_annotations, GO_map, definitions, significance=float(significance))
 
        controls = []
        for group in enriched_groups_control:
            controls.append(group['term'])
        for group in enriched_groups_test:
            if group['term'] in controls:
               enriched_groups_test.remove(group)
               print(f"Removed {group['description']}")
        # print(enriched_groups_test)       
        return enriched_groups_test  
    return  enriched_groups_test
    
    
    # enriched_groups = sorted(enriched_groups)
    # print(enriched_groups)
    # print(f"\nP-value{' '*11}In test     In control  GO ID{' '*13}GO description")
    # for group in enriched_groups:
    #     print(f'{group[0]:<18}{group[1]:<12}{group[2]:<12}{group[3]:<18}{group[4]}')

    # term_of_interest = input('\nList genes for a specific GO term? Please copy and paste the term, otherwise "Enter"\n')
    # if term_of_interest:
    #     more_GO_info(term_of_interest, definitions, all_genes_control, sample_test, sample_control)
  