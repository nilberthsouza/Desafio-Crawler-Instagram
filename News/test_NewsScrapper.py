import unittest
from NewsScrapper import Page
from NewsScrapper import Feed

class TestPage(unittest.TestCase):

    def test_title(self):
        test_page = Page('https://g1.globo.com/bemestar/')
        result = test_page.title()
        self.assertEqual(type(result),str)

class TestConvert(unittest.TestCase):

    def test_from_string_to_text(self):
        test_feed = Feed('https://g1.globo.com/bemestar/')
        result = test_feed.post()
        self.assertEqual(type(result),list)



