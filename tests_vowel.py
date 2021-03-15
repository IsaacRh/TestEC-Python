import vowels
import unittest

class TestVowel(unittest.TestCase):

    def test_is_result(self):
        text = "Hello world"
        result = vowels.set_text(text)
        self.assertEqual(result, ('Hillu wurld', 3))
    
    def test_equal_count_vowel(self):
        text = "Hola MundO dEsdE PyThOn"
        result = vowels.set_text(text)
        self.assertEqual(result[1], 7)

if __name__ == '__main__':
    unittest.main()