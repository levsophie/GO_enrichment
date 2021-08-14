import sys 
sys.path.append('.')


def process_ontology(go_basic):
    '''Processes go-basic.obo file to extract higher GO terms'''
    f = open(go_basic, "r")
    f_asc = open("GO_association.txt", "w")
    counter = 0
    GO_association = {}
    for contents in f:
        contents = contents.split(': ')
        if contents[0] == 'id':
            alt_id = False
            alt_ids = []
            id = contents[1].strip('\n')
            assert(id.startswith('GO'))
            GO_association[id] = set()
            counter += 1
        if contents[0] == 'alt_id':
            alt_id = contents[1].strip('\n')
            assert(alt_id.startswith('GO'))
            GO_association[alt_id] = set()
            alt_ids.append(alt_id)
        if contents[0] == 'is_a':
            term = contents[1].split(' ! ')[0]
            GO_association[id].add(term)
            if alt_ids:
                for alt_id in alt_ids:
                    GO_association[alt_id].add(term)
    # print(f'processed {counter} terms')
    # print(f'size of GO_association is {len(GO_association.keys())}')
    for item in GO_association:
        line = item
        for term in GO_association[item]:
            line = line + '\t' + term
        f_asc.write(line + '\n')
    f.close()
    f_asc.close()
    return GO_association

def list_names_for_terms(obo_file, go_names):
    '''Processes go-basic.obo file to extract all names'''
    f = open(obo_file, "r")
    f_def = open(go_names, "w")
    GO = {}
    for contents in f:
        contents = contents.split(': ')
        if contents[0] == 'id':
            id = contents[1].strip('\n')
        if contents[0] == 'name':
            name = contents[1].strip('\n')
            GO[id] = name
            f_def.write(id + '\t' + name + '\n')
        if contents[0] == 'alt_id':
            alt_id = contents[1].strip('\n')
            GO[alt_id] = name
            f_def.write(alt_id + '\t' + name + '\n')
        if contents[0] == 'is_a':
            term = contents[1].split(' ! ')[0]
            additional_name = contents[1].split(' ! ')[1].strip('\n')
            GO[term] = additional_name
            f_def.write(term + '\t' + additional_name + '\n')
    # print(f'wrote {len(GO.keys())} GO terms and names')
    f_def.close()
    f.close()
    return GO


if __name__ == '__main__':
    GO_association = process_ontology("go-basic.obo")
    GO = list_names_for_terms("go-basic.obo", "GO_names.txt")
