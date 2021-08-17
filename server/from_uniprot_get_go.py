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
    for contents in f:
        described = False      
        l1 = contents.split(' ')
        for e in l1:
            e = e.split('\t')
            for element in e:
                element = element.strip('\t')
                element = element.strip('\n')
                element = element.strip(',')
                element = element.rstrip(';')

                if element.startswith('CNAG') and not described:
                    cnag = element[:10]
                    counter += 1
                    CNAG_map[cnag] = set()
                    try:
                        f_func.write(cnag + '\t' + contents.split('\t')[3] + '\n')
                        described = True
                    except:
                        print("Parsing of the gene function failed")

                if element.startswith('GO:'):
                    term = element[:10]
                    try:
                        GO_map[term].add(cnag) 
                    except:
                        GO_map[term] = set()
                        GO_map[term].add(cnag)
                    # if term == 'GO:0006796':
                    #     print(cnag)
                    CNAG_map[cnag].add(term)
    f_func.close()
    f.close()
    # print(f'processed {counter} genes')
    # print(f'size of GO_map is {len(GO_map.keys())}')
    # print(f'size of CNAG_map is {len(CNAG_map.keys())}')
    return GO_map, CNAG_map
    
if __name__ == '__main__':
    GO_map, CNAG_map = create_all_go_map("uniprot-proteome_UP000010091.tab", "CNAG_to_func.txt")
