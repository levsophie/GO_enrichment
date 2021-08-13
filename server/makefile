.ONESHELL:

.PHONY: run test

run:	
	python from_uniprot_get_go.py
	python go_processing.py
	python add_go_from_higherup.py
	python cnag_list_to_go.py

test:
	python test/base.py