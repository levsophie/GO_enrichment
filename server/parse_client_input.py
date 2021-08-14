def parse(input):
    unwanted_symbols = (',', ':', ';', '\n', '\t')
    cleaned_input = ''
    for symbol in input:
        if symbol in unwanted_symbols:
           cleaned_input = cleaned_input + ' ' 
        else:
            cleaned_input = cleaned_input + symbol
    genes = set()
    gene_list = cleaned_input.split(' ')
    for gene in gene_list:
        if gene.startswith('CNAG_'):
           genes.add(gene[:10]) 
    return list(genes)