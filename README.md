## Workflow for GO analysis for Cryptococcus neoformans var. grubii Serotype A strain H99

Download GO annotations for Cryptococcus neoformans from Uniprot [a link](https://www.uniprot.org/uniprot/?query=yourlist:M202108126320BA52A5CE8FCD097CB85A53697A3510768EK&sort=yourlist:M202108126320BA52A5CE8FCD097CB85A53697A3510768EK&columns=yourlist(M202108126320BA52A5CE8FCD097CB85A53697A3510768EK),isomap(M202108126320BA52A5CE8FCD097CB85A53697A3510768EK),id,genes,genes(ALTERNATIVE),protein%20names,genes(PREFERRED),genes(ORF),genes(OLN),entry%20name)
uniprot-proteome_UP000010091.tab

Download GO structure from GENEONTOLOGY [a link](http://geneontology.org/docs/download-ontology/#go_basic)
go-basic.obo

1. From Uniprot record, find GO terms for each CNAG; map GO groups to CNAG IDs and CNAG IDs to GO groups.

2. From GO generic structure associate GO terms with additional terms higher in the hierarchy (is_a relationship).

3. Combine 1 and 2.


### go_processing.py
Used to enrich annotation of genes from the few existing GO terms
def process_ontology():
    '''Processes go-basic.obo file to extract higher GO terms'''
    return GO_association['GO:XXXXXXX'] = (GO1, GO2...)

def list_names_for_terms():
    '''Processes go-basic.obo file to extract all names'''
    return GO['GO:XXXXXXX'] = 'name'
    
### from_uniprot_get_go.py
Parses the original Uniprot collection that contains GO terms
def create_all_go_map():
    '''Creates a dictionary of all GOs from the Uniprot file as keys
    and a dictionary of all CNAG IDs as keys'''
    return GO_map['GO:XXXXXXX'] = (CNAG_XXXXX, CNAG_XXXXX), CNAG_map['CNAG_XXXXX'] = (GO1, GO2)
    
### add_go_from_higherup.py
Enriched Uniprot-derived GO annotation from the generic GO structure
def enrich_cnag_map():
    '''Creates a dictionary and a file with CNAG IDs as keys and GO terms
    as values; includes higher GO categories'''
    return CNAG_map['CNAG_XXXXX'] = (GO1, GO2...)
    
def enrich_go_map():
    '''Creates a dictionary and a file with GO terms as keys and CNAG IDs 
    as values; includes higher GO categories'''
    return GO_map['GO:XXXXXXX'] = (CNAG_XXXXX, CNAG_XXXXX)
    
### cnag_list_to_go.py
def create_all_go_map():
    '''Creates an empty dictionary of all GOs as keys'''
    
def generate_cnag_list(file):
    '''Generates the list of CNAGS from a given file in any format under  
    the condition that each line starts with CNAG number'''
    
def process_gene_list(GO_map, cnag_list):
    '''Processes a given CNAG list assigning each GO group (key) a number of genes from the list (value).
    The GO_map is initially empty dictionary of all GO groups, get filled with the unique cnag_list profile.'''
    
def create_all_genes_control():
    '''Creates a list of all CNAGs from the file prepared from the UniProt source file.'''

def find_enriched_groups(sample_test, sample_control, number_of_control_annotations,
                                           number_of_test_annotations, GO_map, definitions, significance)
                                           
def more_GO_info(term_of_interest, definitions, all_genes_control, sample_test, sample_control)