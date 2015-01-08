#!/usr/bin/env python

import subprocess
import unittest

import brew


class BrewTest(unittest.TestCase):
    def patch_call(self, expected):
        subprocess._check_call = subprocess.check_call
        subprocess.check_call = lambda args: self.assertEqual(expected, args)

    def unpatch_call(self):
        subprocess.check_call = subprocess._check_call

    def test_fetch(self):
        self.patch_call(['brew', 'fetch', '--deps', 'foobar', 'baz'])
        brew.fetch(['foobar', 'baz'])
        self.unpatch_call()
