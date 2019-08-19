# _*_coding:utf-8_*_


def my_split(line, types=None, delimiter=None):
    """
    splits a line of test and optionally performs type conversion
    :param line:
    :param types:
    :param delimiter:
    :return: list
    for example:
    >>> my_split('GOOD 100 495.0')
    ['GOOD', '100', '495.0']
    >>> my_split('GOOD,100,495.0', delimiter=',')
    ['GOOD', '100', '495.0']
    >>> my_split('GOOD 100 495.0', [str, int, float])
    ['GOOD', 100, 495.0]
    """
    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty, val in zip(types, fields)]
    return fields
