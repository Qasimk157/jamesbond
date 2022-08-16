""" Utility function written here"""
import re


def camelcase_to_sentence(string):
    """
    :param string: camelCase string = mySampleText
    :return: My sample text
    """
    if string != '':
        result = re.sub('([A-Z])', r' \1', string)
        return result[:1].upper() + result[1:].lower()
    return string


