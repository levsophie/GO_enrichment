## Workflow for GO analysis for Cryptococcus neoformans var. grubii Serotype A strain H99

Download GO annotations for Cryptococcus neoformans from Uniprot [a link](https://www.uniprot.org/uniprot/?query=yourlist:M202108126320BA52A5CE8FCD097CB85A53697A3510768EK&sort=yourlist:M202108126320BA52A5CE8FCD097CB85A53697A3510768EK&columns=yourlist(M202108126320BA52A5CE8FCD097CB85A53697A3510768EK),isomap(M202108126320BA52A5CE8FCD097CB85A53697A3510768EK),id,genes,genes(ALTERNATIVE),protein%20names,genes(PREFERRED),genes(ORF),genes(OLN),entry%20name)   
uniprot-proteome_UP000010091.tab

Download GO structure from GENEONTOLOGY [a link](http://geneontology.org/docs/download-ontology/#go_basic)   
go-basic.obo


1. Uniprot GO annotation was supplemented with manual annotation (GO:0006796 phosphate metabolic process)

2. From Uniprot record, find GO terms for each CNAG; map GO groups to CNAG IDs and CNAG IDs to GO groups.

3. From GO generic structure associate GO terms with additional terms higher in the hierarchy (is_a relationship).

4. Combine 1 and 2.

5. GO term enrichment is calculated using Fisher test [a link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html#scipy.stats.fisher_exact)

## Running the development server
prior to modification of the ports (api.py), url (GoDataGathering.jsx) and starting script (package.json)   
From ./server run:  
make test - runs series of tests  
make init - has to be run after tests prior to running the server. Creates essential files.  
make run - starts the server at port 5000  

## Deployment on App Engine
from ./frontend gcloud app deploy node-app.yaml   
from ./server gcloud app deploy python-app.yaml  