import unittest
import cap # cap.py is there..

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
    def test_with_apostrophes(self):
        text = "monty python flying circus"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python Flying Circus")
        
if __name__ == '__main__':
    unittest.main()