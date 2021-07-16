#!/usr/bin/env python3

import unittest
import os
import time
import requests

from hw import RecRead, readem, loadem, get_colorz

class RecReadTest(unittest.TestCase):

    def setUp(self):
        self.rawrecord = 'McWiggins,Mark,mark@pythonsoftwarewa.com,06/26/1977,blue';
        self.record = RecRead(',')
        self.record.parse(self.rawrecord)
        readem()
        loadem()
        
    def test_parse(self):
        self.assertEqual(self.record.lastname.decode(), 'McWiggins')
        self.assertEqual(self.record.favcolor.decode(), 'blue')

    def test_record(self):

        r = requests.post('http://127.0.0.1:5000/records/', self.rawrecord.encode('utf-8'))
        assert r.status_code == 200
        return r

    def test_colors(self):
        r = requests.get('http://127.0.0.1:5000/records/color')
        assert r.status_code == 200
        return r

    def test_dob(self):
    
        r = requests.get('http://127.0.0.1:5000/records/birthdate')
        assert r.status_code == 200
        return r
    

if __name__ == '__main__':
    unittest.main()
