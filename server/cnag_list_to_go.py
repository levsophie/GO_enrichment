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
    return gene_func

def find_enriched_groups(sample_test, sample_control, number_of_control_annotations,
                                           number_of_test_annotations, GO_map, definitions, significance):
    enriched_groups = []
    id = 0
    for term in GO_map.keys():
        if len(sample_test[term]) > 0:
            a = len(sample_test[term])  
            b = len(sample_control[term]) - a
            c = number_of_test_annotations - a
            d = number_of_control_annotations - len(sample_control[term]) - c
            _, p = fisher_exact(np.array([[a,b],[c,d]]))
            if p < significance:
                id += 1
                # print(a,b,c,d)
                enriched_groups.append({'id': id, 'pvalue': round(p, 10),
                                        'test': a, 'control': b, 'term': term,
                                        'description': definitions[term]})
    return sorted(enriched_groups, key = lambda i: i['pvalue'])


def more_GO_info(gene_list, term_of_interest):
    gene_func = create_all_genes_control() # dictionary key: cnag, value: function
    f = open("GO_to_CNAG.txt", "r")
    test = []
    gene_list = parse(gene_list)
    control = []
    cnags = []
    for line in f:
        if line[:10] == term_of_interest:
            items = line.split("'")
            for item in items:
                if item.startswith("CNAG_"):
                    cnag = item[:10]
                    if cnag in gene_list and not cnag in cnags:
                        test.append({'cnag': cnag, 'function': gene_func[cnag]})
                        cnags.append(cnag)
                    elif not cnag in cnags:
                        control.append({'cnag': cnag, 'function': gene_func[cnag]})
                        cnags.append(cnag)
    print(f'{len(test)} genes in test list, {len(control)} genes in control list')
    return {'test': test, 'control': control}
                

def main_endpoint(test_input, significance):
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
    return  enriched_groups_test
    
  