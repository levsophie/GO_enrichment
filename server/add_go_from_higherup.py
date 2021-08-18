import sys 
sys.path.append('.')
from go_processing import process_ontology
from from_uniprot_get_go import create_all_go_map
import copy 


def enrich_cnag_map(go_basic, uniprot_proteome, CNAG_to_func, CNAG_to_GO, GO_to_CNAG, go_association):
    '''Creates a dictionary and a file with CNAG IDs as keys and GO terms
    as values; includes higher GO categories. Returns CNAG_map['CNAG_XXXXX'] = (GO1, GO2...)'''
    f = open(CNAG_to_GO, "w")  
    counter = 0
    GO_association = process_ontology(go_basic, go_association)
    # print("GO_association", GO_association)
    _, CNAG_map = create_all_go_map(uniprot_proteome, CNAG_to_func)
    # print("CNAG_map", CNAG_map)
    for cnag in CNAG_map:  # CNAG_map[CNAG] = (GO1, GO2...)
        temp = set() # temporary set to be added to the existing go
        for go in CNAG_map[cnag]:
            try:
                for additional_go in GO_association[go]:
                    temp.add(additional_go)
                    counter += 1
            except:
                print(f'{go} not found in association table keys')
        CNAG_map[cnag] = set.union(CNAG_map[cnag], temp)
        set_elements = cnag
        for e in  CNAG_map[cnag]:
            set_elements = set_elements +  '\t' + e
        f.write(set_elements + '\n')
    # print(f'added {counter} terms')
    f.close()
  

    '''Creates a dictionary and a file with GO terms as keys and CNAG IDs 
    as values; includes higher GO categories'''
    f = open(GO_to_CNAG, "w")
    f_cnag = open(CNAG_to_GO, "r")
    GO_map = {}
    # GO_map, _ = create_all_go_map(uniprot_proteome, CNAG_to_func)  # GO_map[term] = cnag from Uniprot
    # print(f'length of GO_map before enrichment {len(GO_map.keys())}') 
    # existing_gos = copy.deepcopy(list(GO_map.keys()))
    for line in f_cnag: # GO_map[GO] = (CNAG1, CNAG2... )
        line = line.split('\t')
        # print(line)
        for element in line[1:]:
            try:
                GO_map[element.strip('\n')].add(line[0].strip('\n'))
            except:
                GO_map[element.strip('\n')] = set()
                GO_map[element.strip('\n')].add(line[0].strip('\n'))
    for go in GO_map:
        f.write(go + '\t' + str(GO_map[go])[1:-1] + '\n')  
    f.close()
    f_cnag.close()
    # print(f'length of GO_map after enrichment {len(GO_map.keys())}, counted {counter} lines') 
    return GO_map, CNAG_map



# def enrich_go_map(go_basic, uniprot_proteome, CNAG_to_func, GO_to_CNAG):
#     '''Creates a dictionary and a file with GO terms as keys and CNAG IDs 
#     as values; includes higher GO categories'''
#     f = open(GO_to_CNAG, "w")
#     GO_association = process_ontology(go_basic)
#     GO_map, _ = create_all_go_map(uniprot_proteome, CNAG_to_func)  # GO_map[term] = cnag from Uniprot
#     # print(f'length of GO_map before enrichment {len(GO_map.keys())}') 
#     existing_gos = copy.deepcopy(list(GO_map.keys()))
#     for go in existing_gos: # GO_map[GO] = (CNAG1, CNAG2... )
#         try:
#             for additional_go in GO_association[go]:
#                 try:
#                     GO_map[additional_go] = set.union(GO_map[additional_go], GO_map[go])
#                 except: 
#                     GO_map[additional_go] = GO_map[go]
#         except:
#             print(f'{go} not found in association table keys')
#     for go in GO_map:
#         f.write(go + '\t' + str(GO_map[go])[1:-1] + '\n')  
#     f.close()
#     # print(f'length of GO_map after enrichment {len(GO_map.keys())}, counted {counter} lines') 
#     return GO_map
    
if __name__ == '__main__':
    enrich_cnag_map("GO-basic.obo", "uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt", "CNAG_to_GO.txt", "GO_to_CNAG.txt", "GO_association.txt")
    # enrich_go_map("GO-basic.obo", "uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt", "GO_to_CNAG.txt")