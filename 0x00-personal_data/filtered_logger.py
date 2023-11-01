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
    message: str, separator: str) -> str:
    """
    Replaces all occurrences of certain fields in a message with a given
    redaction string.

    Args:
        fields (List[str]): A list of fields to be filtered.
        rdaction (str): The string to replace filtered fields with.
        message (str): The message to be filtered.
        separator (str): The separator used to split the message into fields.

    Returns:
        str: The filtered message.
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
