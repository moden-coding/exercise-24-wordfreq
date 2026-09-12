#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from src.word_frequencies import word_frequencies


class WordFrequencies(unittest.TestCase):

    def test_first(self):
        d = word_frequencies("src/alice.txt")
        self.assertEqual(
            d['creating'], 3,
            msg="word_frequencies('src/alice.txt')['creating'] should be 3: "
            "'creating' appears three times in the text.")
        self.assertEqual(
            d['Carroll'], 3,
            msg="word_frequencies('src/alice.txt')['Carroll'] should be 3: "
            "'Carroll' appears three times in the text.")
        self.assertEqual(
            d['sleepy'], 2,
            msg="word_frequencies('src/alice.txt')['sleepy'] should be 2: "
            "'sleepy' appears twice in the text.")
        self.assertEqual(
            d['Rabbit'], 28,
            msg="word_frequencies('src/alice.txt')['Rabbit'] should be 28: "
            "'Rabbit' appears 28 times in the text.")
        self.assertEqual(
            len(d), 2424,
            msg="word_frequencies('src/alice.txt') should contain 2424 "
            "distinct words. Got %d." % len(d))

    def test_calls(self):
        with patch('builtins.open', wraps=open) as o:
            word_frequencies("src/alice.txt")
            self.assertTrue(
                o.called,
                msg="word_frequencies must actually open the given file "
                "with the built-in open().")


if __name__ == '__main__':
    unittest.main()
