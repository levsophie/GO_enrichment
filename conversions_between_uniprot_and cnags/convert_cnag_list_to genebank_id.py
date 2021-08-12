'''Converts a list of CNAG identifiers to Accession numbers (GeneBank)'''

genes = {}
with open ('conversion_from_cnag_to_genebank.txt', 'rt') as myfile:  
    for line in myfile: 
        line = line.strip('\n')
        line = line.split('\t')
        genes[line[0]] = line[1]

myfile.close() 

with open ('text_cnag_list.txt', 'rt') as cnag_list: 
    for line in cnag_list:
        if line[:4] == "CNAG":
            try:
                print(genes[line[:10]])
            except:
                print("Failed to find match")