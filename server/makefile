.ONESHELL:

.PHONY: init run test

init:
	python from_uniprot_get_go.py
	python go_processing.py
	python add_go_from_higherup.py

run:
	python api.py

test:
	python test/base.py