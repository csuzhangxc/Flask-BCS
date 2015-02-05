#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Tests for Flask-BCS.'''

import unittest
import urllib
from flask import Flask
from flask_bcs import BCS

BCS_HOST = 'BCS Host'
BCS_ACCESS_KEY = 'BCS Access Key'
BCS_SECRET_KEY = 'BCS Secret Key'
BCS_BUCKET_NAME = 'BCS Bucket Name'


class FlaskBCSTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(__name__)
        self.bcs = BCS(self.app)

    def test_save(self):
        data = 'test_save'
        filename = 'test_save'
        allow_referers = ['http://*.duapp.com/*', 'http://zhangxc.com/*']
        ret = self.bcs.save(data, filename, allow_referers)
        self.assertIsInstance(ret, dict)
        self.assertEqual(ret['status'], 200)

    def test_delete(self):
        data = 'test_delete'
        filename = 'test_delete'
        self.bcs.save(data, filename)
        ret = self.bcs.delete(filename)
        self.assertIsInstance(ret, dict)
        self.assertEqual(ret['status'], 200)

    def test_url(self):
        data = 'test_url'
        filename = 'test_url'
        self.bcs.save(data, filename)
        url = self.bcs.url(filename)
        resp = urllib.urlopen(url)
        self.assertEqual(data, resp.read())

if __name__ == '__main__':
    unittest.main()