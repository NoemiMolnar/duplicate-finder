#!/usr/bin/env python
"""
this module gets the files' content in a specific directory.
"""

def get_file_content(path):
    """Reads a file and gets its content.
    Args:
        path (string): The path of a file.

    Returns:
        string: The content of the file, which the path belongs to.
    """

    with file(path) as file_to_read:
        content = file_to_read.read()
        return content
