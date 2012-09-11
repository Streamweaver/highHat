__author__ = 'Streamweaver'

import unittest, os
from xml.etree.ElementTree import Element

from hathitrustclient.api.data_api import HtResource

class TestHtResource(unittest.TestCase):

    def setUp(self):
        self.id = 'uva.x001037769' # The Three Musketeers
        self.resource = HtResource(self.id)
        self.location = os.getcwd() # for testing binary downloads

    def test_meta(self):
        # Simiple test to ensure default return is an Element object instance
        result_etree = self.resource.meta()
        self.assertIsInstance(result_etree, Element, msg="Return was not etree Element as expected!")

        # Test parsing of a JSON return instead.
        result_json = self.resource.meta(json=True)
        self.assertIsInstance(result_json, dict)

    def test_structure(self):
        # Simiple test to ensure default return is an Element object instance
        result_etree = self.resource.structure()
        self.assertIsInstance(result_etree, Element, msg="Return was not etree Element as expected!")

        # Test parsing of a JSON return instead.
        result_json = self.resource.structure(json=True)
        self.assertIsInstance(result_json, dict)

    def test_pagemeta(self):
        # Simiple test to ensure default return is an Element object instance
        result_etree = self.resource.pagemeta(1)
        self.assertIsInstance(result_etree, Element, msg="Return was not etree Element as expected!")

        # Test parsing of a JSON return instead.
        result_json = self.resource.pagemeta(1, json=True)
        self.assertIsInstance(result_json, dict)

# TODO: Implement a OAuthTokenRetriever to get this test to work.
#    def test_aggregate(self):
#        # Tests the aggregate file.
#        self.resource.aggregate(self.location)
