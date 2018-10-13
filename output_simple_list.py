#!/usr/bin/env python
"""
This module outputs the filenames of duplicate files.
"""

def output_simple_list(duplicate_file_list, file1, file2):
    """Gets a list of duplicate filenames and outputs them

    Args:
        duplicate_file_list (list): Empty list.
        file1 (srting): The name of one of the duplicate files.
        file2 (string): The name of one of the duplicate files.
    Returns:
        list: A list of the duplicate file names.
    """
    duplicate_file_list.append(file2)
    if file1 not in duplicate_file_list:
        duplicate_file_list.append(file1)
        