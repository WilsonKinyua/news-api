import unittest
from app.models import Sources


class NewsSourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources(
            'bbc-news', 'BBC News', 'Children killed during cold war', "https://abcnews.go.com", 'general', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
