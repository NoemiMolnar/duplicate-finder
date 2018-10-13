#!/usr/bin/env python
"""
This module outputs the filenames of duplicate files.
"""

def output_grouped_list(duplicate_file_list, file1, file2):
    """Gets a list of duplicate filenames and outputs them

    Args:
        duplicate_file_list (list): Empty list.
        file1 (srting): The name of one of the duplicate files.
        file2 (string): The name of one of the duplicate files.
    Returns:
        list: A grouped list of the duplicate file names
    """
    if len(duplicate_file_list) < 1:
        duplicate_file_list.append([file1, file2])
    for i in duplicate_file_list:
        if file1 in i and file2 not in i:
            i.append(file2)
        elif file2 in i and file1 not in i:
            i.append(file1)
        elif file1 in i and file2 in i:
            break
        else:
            duplicate_file_list.append([file1, file2])
        break
    return duplicate_file_list
    