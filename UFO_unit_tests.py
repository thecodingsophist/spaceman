import pytest
import io
import sys
import UFO_game

#HELPER FUNCTIONS

# def capture_console_output(function_body):
#     # _io.StringIO object
#     string_io = io.StringIO()
#     sys.stdout = string_io
#     function_body()
#     sys.stdout = sys.__stdout__
#     return string_io.getvalue()

#TEST FUNCTIONS

def test_random_word_chosen():
    chosen_word = load_word()
    assert chosen_word != null

    
