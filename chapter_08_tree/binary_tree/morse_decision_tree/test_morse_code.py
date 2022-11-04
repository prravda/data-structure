from unittest import TestCase
from chapter_08_tree.binary_tree.morse_decision_tree.morse_code_mockups import morse_testsuite
from chapter_08_tree.binary_tree.morse_decision_tree.morse_code_table import morse_code_table


class MorseCodeTest(TestCase):
    def test_morse_code_encoding_basic(self):
        raw_str, morse_converted_str = morse_testsuite
        morse_code_converted_result: list[str] = []

        for c in raw_str:
            if c in morse_code_table:
                morse_code_converted_result.append(morse_code_table[c])

        self.assertEqual(morse_converted_str, morse_code_converted_result)
