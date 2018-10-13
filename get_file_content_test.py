#!/usr/bin/env python
"""
This module contains test(s) for the get file contet module.
"""

import unittest
import os
from get_file_content import get_file_content

class TestCompareFiles(unittest.TestCase):
    """
    Test class tests the files' content in a specific directory.
    """
    def test_with_content(self):
        """
        Test class tests the get_file_content function with a not empty file.
        """
        test_file = os.open('test_file', os.O_RDWR|os.O_CREAT)
        os.write(test_file, 'This is test')
        os.close(test_file)
        test_file = os.getcwd() + '/test_file'
        test_file_content = get_file_content(test_file)
        self.assertEqual('This is test', test_file_content)
        