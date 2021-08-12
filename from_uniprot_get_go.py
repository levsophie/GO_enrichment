

def create_all_go_map(uniprot_data, output):
    '''Creates a dictionary of all GOs from the Uniprot file as keys
    and a dictionary of all CNAG IDs as keys'''
    f = open(uniprot_data, "r")
    f_func = open(output, 'w')
    counter = 0
    GO_map = {}
    CNAG_map = {}
    for contents in f:
        isCNAG = False
        l = contents.split(',')
        l1 = l[0].split('\t')
        for e in l1:
            if e.startswith('CNAG'):
                cnag = e[:10]
                isCNAG = True
                counter += 1
                CNAG_map[cnag] = set()
                f_func.write(cnag + '\t' + l1[3] + '\n')
                break
        
        l2 = l1[-1].split('\t')
        go_terms = l2[-1].split('; ')
        for term in go_terms:
            term = term.strip('\n')
            if (isCNAG) and (term[:2] =='GO'):
                try:
                    GO_map[term].add(cnag) 
                except:
                    GO_map[term] = set()
                    GO_map[term].add(cnag)
                CNAG_map[cnag].add(term)
    f_func.close()
    print(f'processed {counter} genes')
    print(f'size of GO_map is {len(GO_map.keys())}')
    print(f'size of CNAG_map is {len(CNAG_map.keys())}')
    return GO_map, CNAG_map
    
if __name__ == '__main__':
    GO_map, CNAG_map = create_all_go_map()
