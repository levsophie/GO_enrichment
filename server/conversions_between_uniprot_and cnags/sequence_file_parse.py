
'''Parses the whole list of Cryptococcal proteins from GeneBank to 
extract matches between CMAG number and Accession number in GeneBank'''

genes = {}
f = open("conversion_from_cnag_to_genebank.txt", "a")
fa = open("all_accession_numbers.txt", "a")
counter = 0
with open ('sequence.gp', 'rt') as myfile:  
    isCNAG = False
    isAccession = False
    for line in myfile:                
        line = line.strip(' ')
        if line[0:10] == '/locus_tag':
            cnag = line[12:22]
            isCNAG = True
        if line[0:9] == 'ACCESSION':
             line = line.split(' ')
             accession = line[3][:12]
             isAccession = True
        if (line[0:2] =='//'):
            if (isCNAG and isAccession): 
                genes[cnag] = accession 
                info = cnag + '\t' + accession + '\n'
                print(info)
                f.write(info)
                fa.write(accession+ '\n')
                counter += 1
            else:
                print("Missing info")

print(f'Counted {counter} genes')
f.close()
myfile.close()