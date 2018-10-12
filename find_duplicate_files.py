#!/usr/bin/env python
"""
This module finds the filenames of duplicate files.
"""

def find_duplicate_files(get_content, file_dir):
    """Compares two files and returns the pairs of the duplicate files.

    Args:
        get_content: Algorith that returns the content of a certain file.
        file_dir: The directory which we want to read the content of.

    Returns:
        list: The list of the duplicate file names
    """

    file_list = get_content(file_dir)
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
                duplicates.append(file2)
                if file1 not in duplicates:
                    duplicates.append(file1)
                break
    return duplicates