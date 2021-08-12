import unittest
import sys 
sys.path.append('..')

from GO_enrichment.from_uniprot_get_go import create_all_go_map 

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
    
    
if __name__ == "__main__":
    unittest.main()