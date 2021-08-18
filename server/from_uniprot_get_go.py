import sys 
sys.path.append('..')


def create_all_go_map(uniprot_proteome, CNAG_to_func):
    '''Creates a dictionary of all GOs from the Uniprot file as keys
    and a dictionary of all CNAG IDs as keys'''
    f = open(uniprot_proteome, "r")
    f_func = open(CNAG_to_func, 'w')
    counter = 0
    GO_map = {}
    CNAG_map = {}
    CNAG_func = {}
    for contents in f:
        l1 = contents.split(' ')
        cnags = []
        terms = []
        for e in l1:
            e = e.split('\t')
            for element in e:
                element = element.strip('\t')
                element = element.strip('\n')
                element = element.strip(',')
                element = element.rstrip(';')

                if element.startswith('CNAG'):
                    cnag = element[:10]
                    counter += 1
                    func = contents.split('\t')[3]
                    CNAG_func[cnag] = func
                    cnags.append(cnag)
                    CNAG_map[cnag] = set()
  
                if element.startswith('GO:'):
                    term = element[:10]
                    terms.append(term)
                    GO_map[term] = set()
        for term in terms:
            for cnag in cnags:
                GO_map[term].add(cnag) 
                CNAG_map[cnag].add(term)
     
    for cnag in CNAG_func:
        f_func.write(cnag + '\t' + CNAG_func[cnag] + '\n')
    f_func.close()
    f.close()
    print(f'processed {len(CNAG_map.keys())} genes')
    print(f'size of GO_map is {len(GO_map.keys())}')
    print(f'size of CNAG_map is {len(CNAG_map.keys())}')
    return GO_map, CNAG_map
    
if __name__ == '__main__':
    GO_map, CNAG_map = create_all_go_map("uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt")
