import unittest
import sys 
sys.path.append('..')
from scipy.stats import hypergeom, fisher_exact
import numpy as np
from server.from_uniprot_get_go import create_all_go_map 
from server.go_processing import process_ontology
from server.add_go_from_higherup import enrich_cnag_map
from server.cnag_list_to_go import find_enriched_groups
class BaseTestCase(unittest.TestCase):
    
    
    def test_create_all_go_map(self):
        '''Creates a dictionary of all GOs from the Uniprot file as keys
        and a dictionary of all CNAG IDs as keys'''
        GO_map, CNAG_map = create_all_go_map("test/test_uniprot.txt", "test/uniprot_output.txt")
        test_go_map = {'GO:0005886': {'CNAG_07636'},
                    'GO:0008047': {'CNAG_07636'}, 
                    'GO:0005774': {'CNAG_00025'}, 
                    'GO:0015369': {'CNAG_00025'}}
        test_cnag_map = {'CNAG_07636': {'GO:0008047', 'GO:0005886'},
                        'CNAG_00025': {'GO:0005774', 'GO:0015369'}}
        self.assertEqual(GO_map, test_go_map)
        self.assertEqual(CNAG_map, test_cnag_map)
    
    def test_create_all_go_map_one_go(self):
        '''Creates a dictionary of all GOs from the Uniprot file as keys
        and a dictionary of all CNAG IDs as keys'''
        GO_map, CNAG_map = create_all_go_map("test/test_go_uniprot.txt", "test/uniprot_output.txt")
        test_go_map = {'GO:0000001': {'CNAG_07636'}, 
                    'GO:0006594': {'CNAG_00025'}, 
                    'GO:0006871': {'CNAG_07724'}, 
                    'GO:0048308': {'CNAG_05655'}, 
                    'GO:0048311': {'CNAG_05449'}, 
                    'GO:0000002': {'CNAG_00156'}, 
                    'GO:0007005': {'CNAG_07701'}}
        test_cnag_map = {'CNAG_07636': {'GO:0000001'},
                        'CNAG_00025': {'GO:0006594'}, 
                        'CNAG_07724': {'GO:0006871'}, 
                        'CNAG_05655': {'GO:0048308'}, 
                        'CNAG_05449': {'GO:0048311'}, 
                        'CNAG_00156': {'GO:0000002'}, 
                        'CNAG_07701': {'GO:0007005'}}
        self.assertEqual(GO_map, test_go_map)
        self.assertEqual(CNAG_map, test_cnag_map)
    
    def test_process_onthology(self):
        '''Processes go-basic.obo file to extract higher GO terms'''
        GO_association = process_ontology("test/test_go.txt", "test/test_go_association.txt")
        test = {'GO:0000001': {'GO:0048311', 'GO:0048308'},
                'GO:0006594': {'GO:0048311', 'GO:0048308'}, 
                'GO:0006871': {'GO:0048311', 'GO:0048308'}, 
                'GO:0000002': {'GO:0007005'}}
        self.assertEqual(GO_association, test)

    def test_enrich_cnag_map(self):
        '''Creates a dictionary and a file with CNAG IDs as keys and GO terms
        as values; includes higher GO categories. Returns CNAG_map['CNAG_XXXXX'] = (GO1, GO2...)'''
        go_basic = "test/test_go.txt"
        uniprot_proteome = "test/test_go_uniprot.txt"
        CNAG_to_func = "test/test_cnag_to_func.txt"
        CNAG_to_GO = "test/test_cnag_to_go.txt"
        GO_to_CNAG = "test/test_go_to_cnag.txt"
        go_association = "test/test_go_association.txt"
        GO_map, CNAG_map  = enrich_cnag_map(go_basic, uniprot_proteome, CNAG_to_func, CNAG_to_GO, GO_to_CNAG, go_association)
 
        test_cnag_map = {'CNAG_07636': {'GO:0048308', 'GO:0000001', 'GO:0048311'}, 
                                'CNAG_00025': {'GO:0048308', 'GO:0048311', 'GO:0006594'}, 
                                'CNAG_07724': {'GO:0006871', 'GO:0048308', 'GO:0048311'}, 
                                'CNAG_05655': {'GO:0048308'}, 
                                'CNAG_05449': {'GO:0048311'}, 
                                'CNAG_00156': {'GO:0000002', 'GO:0007005'}, 
                                'CNAG_07701': {'GO:0007005'}}
                                
        test_go_map = {'GO:0048311': {'CNAG_05449', 'CNAG_07724', 'CNAG_07636', 'CNAG_00025'},
                        'GO:0000001': {'CNAG_07636'}, 
                        'GO:0048308': {'CNAG_07724', 'CNAG_07636', 'CNAG_05655', 'CNAG_00025'},
                        'GO:0006594': {'CNAG_00025'},
                        'GO:0006871': {'CNAG_07724'}, 'GO:0000002': {'CNAG_00156'},
                        'GO:0007005': {'CNAG_07701', 'CNAG_00156'}}
        
        self.assertEqual(test_cnag_map, CNAG_map)
        self.assertEqual(test_go_map, GO_map)

    def test_find_enriched_groups(self):
        sample_test = 8
        sample_control = 2
        number_of_test_annotations = 1
        number_of_control_annotations = 5      
        _, p = fisher_exact(np.array([[sample_test, sample_control],[number_of_test_annotations, 
            number_of_control_annotations]]))                           
        self.assertEqual(round(p, 4), 0.035)  # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html#scipy.stats.fisher_exact
        
if __name__ == "__main__":
    unittest.main()