import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles('The Associated Press',
                                    'Man attacked by alligator in Hurricane Idas floodwaters',
                                    'The U.S. and its allies are working together to crush the North Korean leader, Kim Jong-un, and to confront the growing tensions between the United States and China.',
                                    'https://www.nytimes.com/2019/09/04/us/politics/trump-kim-north-korea.html',
                                    'https://static01.nyt.com/images/2019/09/04/us/04kim-north-korea-1/04kim-north-korea-1-facebookJumbo.jpg',
                                    '2019-09-04T14:00:00Z',
                                    "SLIDELL, La. -- A man was attacked by a large alligator while walking through floodwaters from Hurricane Ida and is now missing, a Louisiana sheriff said.\r\nThe 71-year-old mans wife told sheriffs dep… [+1041 chars]"
                                    )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
