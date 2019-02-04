import unittest
import UFO_game

class TestUFOMethods(unittest.TestCase):

    def test_is_guess_valid(self):
        self.assertTrue(UFO_game.is_guess_valid('a'))
        self.assertFalse(UFO_game.is_guess_valid('1'))

    def test_is_guess_original(self):
        self.assertTrue(UFO_game.is_guess_original('z', 'abc'))
        self.assertFalse(UFO_game.is_guess_original('a', 'abc'))

    def test_is_word_guessed(self):
        self.assertTrue(UFO_game.is_word_guessed('cat', 'cat'))
        self.assertFalse(UFO_game.is_word_guessed('cats', 'cat'))

    #OH NO! There's an error here that I didn't have time to get to. For future implementations I will definitely look into why this test failed. 
    def test_get_guessed_word(self):
        self.assertEqual(UFO_game.get_guessed_word('catacomb', 'ca'), 'ca_ac___')

    def test_word_reader(self):
        self.assertEqual(UFO_game.word_reader('cat'), {0:'c', 1:'a', 2:'t'})

    #SEE UFO_test_word_functions for tests regarding the word_searcher function, I used more of a trial and error method on the terminal for this function
    # def test_word_searcher(self):

    def test_get_available_letters(self):
        self.assertEqual(UFO_game.get_available_letters('abc'), 'defghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()
