#!/usr/bin/env python3
"""module to filter logs"""
from typing import List
import re


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

def filter_datum(
    fields: List[str], rdaction: str,
    message: str, separator: str):
    pass
