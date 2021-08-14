import sys 
sys.path.append('.')
from add_go_from_higherup import enrich_cnag_map
import copy
from scipy.stats import hypergeom, fisher_exact
from go_processing import list_names_for_terms
from from_uniprot_get_go import create_all_go_map
import numpy as np

def create_empty_go_map():
    '''Creates an empty dictionary of all GOs as keys'''
    f = open("GO_names", "r")
    empty_GO_map = {}
    names = {}
    for line in f:
        line = line.split('\t')
        empty_GO_map[line[0]] = []
        names[line[0]] = line[1]
    f.close()
    return empty_GO_map, names

def process_gene_list(GO_map, cnag_list):
    '''Processes a given CNAG list assigning each GO group (key) a number of genes from the list (value).
    The GO_map is initially empty dictionary of all GO groups, get filled with the unique cnag_list profile.'''
    CNAG_GO_map = enrich_cnag_map("go-basic.obo", "uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt", "CNAG_to_GO.txt")   # CNAGs as keys and GO groups in a set as values from read_GO'''
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
    for term in GO_map.keys():
        if len(sample_test[term]) > 0:
            a = len(sample_test[term])  
            b = len(sample_control[term]) - a
            c = number_of_test_annotations - a
            d = number_of_control_annotations - len(sample_control[term]) - c
            _, p = fisher_exact(np.array([[a,b],[c,d]]))
            if p < significance:
                enriched_groups.append([round(p, 10), a, b, term, definitions[term]])
                # print(a,b,c,d)
    return enriched_groups

def generate_cnag_list(file):
    '''Generates the list of CNAGS from a given file in any format under  
    the condition that each line starts with CNAG number'''
    try:
        f = open(file)
        cnags = set()
        for line in f:
            if line.startswith('CNAG_'):
                cnag = line[:10]
                if not cnag in cnags:
                    cnags.add(cnag)
        return list(cnags)
    except:
        print("File not found, try again")


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


if __name__ == '__main__':
    GO_map, definitions = create_empty_go_map()
    test = copy.deepcopy(GO_map)
    # The GO_map is initially empty dictionary of all GO groups, gets filled with the unique cnag_list profile.'''
    # file = "experimental_data/up_in_kcs1.txt"
    file = input('Please type the name of the text file with gene list (from experimental_data)\n')
    file = "experimental_data/" + file + ".txt"
    gene_list = generate_cnag_list(file)
    sample_test, number_of_test_annotations = process_gene_list(test, gene_list)  # sample_test['GO:0005829'] == 1

    all_genes_control = create_all_genes_control()  # uses full list of GO-annotated CNAG numbers
    control = copy.deepcopy(GO_map)
    sample_control, number_of_control_annotations = process_gene_list(control, all_genes_control.keys())

    p_significance = input('\nPlease enter desired P-value threshold, "Enter" for default (0.001)\n')
    if not p_significance:
        p_significance = 0.001
    print('Processing request...')
    enriched_groups = find_enriched_groups(sample_test, sample_control, number_of_control_annotations,
                                           number_of_test_annotations, GO_map, definitions, significance=float(p_significance))
    enriched_groups = sorted(enriched_groups)
    print(f"\nP-value{' '*11}In test     In control  GO ID{' '*13}GO description")
    for group in enriched_groups:
        print(f'{group[0]:<18}{group[1]:<12}{group[2]:<12}{group[3]:<18}{group[4]}')

    term_of_interest = input('\nList genes for a specific GO term? Please copy and paste the term, otherwise "Enter"\n')
    if term_of_interest:
        more_GO_info(term_of_interest, definitions, all_genes_control, sample_test, sample_control)
