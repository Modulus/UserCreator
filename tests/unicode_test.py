__author__ = 'JohnSigvald'

import unittest


class UnicodeTest(unittest.TestCase):

    def test_unicode(self):
        text = u'H\xd8NEFOSS\r\n'

        print text