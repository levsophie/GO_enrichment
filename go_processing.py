def process_ontology():
    '''Processes go-basic.obo file to extract higher GO terms'''
    f = open("go-basic.obo", "r")
    f_associated = open('go_associations.txt', 'w')
    # f = open("test_go.txt")
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
    print(f'processed {counter} terms')
    print(f'size of GO_association is {len(GO_association.keys())}')
    return GO_association

def list_names_for_terms():
    '''Processes go-basic.obo file to extract all names'''
    f = open("go-basic.obo", "r")
    f_def = open("GO_names.txt", "w")
    # f = open("test_go.txt")
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
    print(f'wrote {len(GO.keys())} GO terms and names')
    f_def.close()
    f.close()
    return GO


if __name__ == '__main__':
    GO_association = process_ontology()
    GO = list_names_for_terms()
    # print(GO_association)
    # print(GO)