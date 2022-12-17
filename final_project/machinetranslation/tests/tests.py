import unittest
from translator import english_to_french, french_to_tnglish


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        # self.assertEqual(english_to_french(""), "") 
        self.assertEqual(english_to_french('Hello') , 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        # self.assertEqual(french_to_tnglish(""), "") 
        self.assertEqual(french_to_tnglish('Bonjour') , 'Hello')

unittest.main()