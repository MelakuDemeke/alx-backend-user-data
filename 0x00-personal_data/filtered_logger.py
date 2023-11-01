#!/usr/bin/env python3
"""module to filter logs"""
from typing import List
import re


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

import re
from typing import List

def filter_datum(
    fields: List[str], rdaction: str,
    message: str, separator: str) -> str:

    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
