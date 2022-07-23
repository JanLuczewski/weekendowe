import unittest
from main import get_clientlist

class Get_Client_TestCase(unittest.TestCase):
    def test_get_client_list(self):
        result = get_clientlist('clients.csv')
        expected = ['Test_1','Test_3']
        self.assertEqual(result,expected)
