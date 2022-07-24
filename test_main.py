import unittest
import os

import main
from main import get_clientlist,get_outputxml,arguments
from unittest import mock
import sys

class Get_Client_TestCase(unittest.TestCase):
    def test_get_client_list(self):
        result = get_clientlist('clients.csv')
        expected = ['Test_1','Test_3']
        self.assertEqual(result,expected)
    def test_empty_get_client_list(self):
        path = os.path.join('test_files','test_csv.csv')
        result = get_clientlist(path)
        expected = []
        self.assertEqual(result,expected)

class Get_Output_TestCase(unittest.TestCase):
    def test_get_outputxml(self):
        get_outputxml('clients.xml','clients.csv')
        expected = os.path.join('output.xml')
        self.assertTrue(os.path.exists(expected))
    @mock.patch('main.output_title',os.path.join('test_files','output.xml'))
    def test_get_outputxml_mock(self):
        # mocked_var = os.path.join('test_files','output.xml')
        get_outputxml('clients.xml','clients.csv')
        expected = os.path.join('test_files','output.xml')
        self.assertTrue(os.path.exists(expected))

class TestArgv(unittest.TestCase):
    def test_sysargv(self):
        sys.argv.append('clients.hujv')
        sys.argv.append('clients.xml')
        print(sys.argv)
        with self.assertRaisesRegex(TypeError,'csv path should be csv extension'):
            arguments()
    def test_sysargv_2(self):
        sys.argv.append('clients.csv')
        sys.argv.append('clients.huj')
        print(sys.argv)
        self.assertRaisesRegex(TypeError,'xml path should be xml extension',arguments)