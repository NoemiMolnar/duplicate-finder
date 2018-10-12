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