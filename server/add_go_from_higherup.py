import sys 
sys.path.append('.')
from go_processing import process_ontology
from from_uniprot_get_go import create_all_go_map
import copy 


def enrich_cnag_map(go_basic, uniprot_proteome, CNAG_to_func, CNAG_to_GO):
    '''Creates a dictionary and a file with CNAG IDs as keys and GO terms
    as values; includes higher GO categories. Returns CNAG_map['CNAG_XXXXX'] = (GO1, GO2...)'''
    f = open(CNAG_to_GO, "w")  
    counter = 0
    GO_association = process_ontology(go_basic)
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
        f.write(cnag + '\t' +  str(CNAG_map[cnag]) + '\n')
    # print(f'added {counter} terms')
    f.close()
    
    return CNAG_map

def enrich_go_map(go_basic, uniprot_proteome, CNAG_to_func, GO_to_CNAG):
    '''Creates a dictionary and a file with GO terms as keys and CNAG IDs 
    as values; includes higher GO categories'''
    f = open(GO_to_CNAG, "w")
    counter = 0
    GO_association = process_ontology(go_basic)
    GO_map, _ = create_all_go_map(uniprot_proteome, CNAG_to_func)
    # print(f'length of GO_map before enrichment {len(GO_map.keys())}') 
    existing_gos = copy.deepcopy(list(GO_map.keys()))
    for go in existing_gos: # GO_map[GO] = (CNAG1, CNAG2... )
        try:
            for additional_go in GO_association[go]:
                try:
                    GO_map[additional_go] = set.union(GO_map[additional_go], GO_map[go])
                    f.write(additional_go + '\t' + str(GO_map[additional_go]) + '\n')
                    counter += 1
                except: 
                    GO_map[additional_go] = GO_map[go]
                    f.write(additional_go + '\t' + str(GO_map[additional_go]) + '\n')
                    counter += 1
            f.write(go + '\t' + str(GO_map[go]) + '\n')
            counter += 1
        except:
            print(f'{go} not found in association table keys')
    # print(f'length of GO_map after enrichment {len(GO_map.keys())}, counted {counter} lines') 
    return GO_map
    
if __name__ == '__main__':
    enrich_cnag_map("GO-basic.obo", "uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt", "CNAG_to_GO.txt")
    enrich_go_map("GO-basic.obo", "uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt", "GO_to_CNAG.txt")