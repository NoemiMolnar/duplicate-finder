#!/usr/bin/env python
"""
This module contains test(s) for the find duplicate files module.
"""

import unittest
from get_file_content import get_file_content
from find_duplicate_files import find_duplicate_files
from output_simple_list import output_simple_list
from output_grouped_list import output_grouped_list

class TestCompareFiles(unittest.TestCase):
    """
    This class contains test(s) for the find duplicate files module.
    """
    def test_simple_output(self):
        """
        This method tests the find suplicate files functions with the output simple list method.
        """
        directory_path = '/media/noemi/96667C6D667C504B/files'
        duplicate_files_test_data = ['603 (another copy)', '603', '603 (copy)']
        duplicate_files = find_duplicate_files(get_file_content, directory_path, output_simple_list)
        self.assertEqual(duplicate_files, duplicate_files_test_data)

    def test_grouped_output(self):
        """
        This method tests the find suplicate files functions with the output grouped list method.
        """
        directory = '/media/noemi/96667C6D667C504B/files'
        duplicate_files_test_data = [['603', '603 (another copy)', '603 (copy)']]
        duplicate_files = find_duplicate_files(get_file_content, directory, output_grouped_list)
        self.assertEqual(duplicate_files, duplicate_files_test_data)
    