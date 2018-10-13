#!/usr/bin/env python
"""
This module runs the duplicate finder.
"""
from get_file_content import get_file_content
from find_duplicate_files import find_duplicate_files
from output_simple_list import output_simple_list

PATH = '/media/noemi/96667C6D667C504B/files'

print find_duplicate_files(get_file_content, PATH, output_simple_list)
