import unittest 

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Byte'),'Byte')
    
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('AuRevoir'),'AuRevoir')

if __name__ == "__main__":
    unittest.main()