import unittest
from instagram import Convert
from instagram import Publications

class TestConvert(unittest.TestCase):

    def test_from_key_to_link(self):
        result = Convert.from_key_to_link('dev')
        self.assertEqual(type(result),str)

class TestPublications(unittest.TestCase):

    def test_showPublications(self):
        test_pub= Publications()
        test_pub.link = Convert.from_key_to_link('dev')
        result = test_pub.showPublications()
        self.assertEqual(type(result),str)


