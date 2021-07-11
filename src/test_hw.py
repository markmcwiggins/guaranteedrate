#!/usr/bin/env python3

import unittest

from hw import RecRead


class RecReadTest(unittest.TestCase):

    def setUp(self):
        self.record = RecRead(',')
        self.record.parse('McWiggins,Mark,mark@pythonsoftwarewa.com,06/26/1977,blue')

    def test_parse(self):
        self.assertEqual(self.record.lastname, 'McWiggins')
        self.assertEqual(self.record.favcolor, 'blue')

if __name__ == '__main__':
    unittest.main()
