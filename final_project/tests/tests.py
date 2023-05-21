import unittest

from ..translator import Watson

WATSON = Watson()

class TestEnglishFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(WATSON.english_to_french(''), '') 
        self.assertEqual(WATSON.english_to_french('Hello'), 'Bonjour') 
        

class TestFrenchEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(WATSON.french_to_english(''), '')
        self.assertEqual(WATSON.french_to_english('Bonjour'), 'Hello')
        
        
unittest.main()