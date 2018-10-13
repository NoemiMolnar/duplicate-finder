#!/usr/bin/env python
"""
This module finds the filenames of duplicate files.
"""
import os

def find_duplicate_files(get_content, file_dir, output_duplicates):
    """Compares two files and returns the pairs of the duplicate files.

    Args:
        get_content (function): Algorithm that returns the content of a certain file.
        file_dir (list): The directory which we want to read the content of.
        output_duplicates (function): Algorithm that outputs the duplicates.

    Returns:
        list: The list of the duplicate file names
    """

    file_list = os.listdir(file_dir)
    if len(file_list) < 1:
        return []
    duplicates = []
    for file1 in file_list:
        for file2 in file_list:
            path1 = get_content(file_dir + '/' + file1)
            path2 = get_content(file_dir + '/' + file2)
            if file_list.index(file2) > file_list.index(file1) and \
                len(path1) == len(path2) and \
                hash(path1) == hash(path2):
                output_duplicates(duplicates, file1, file2)
                break
    return duplicates
    