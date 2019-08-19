# _*_coding:utf-8_*_

from mysplit import my_split

# def my_split(line, types=None, delimiter=None):
#     """
#     splits a line of test and optionally performs type conversion
#     :param line:
#     :param types:
#     :param delimiter:
#     :return: list
#     """
#     fields = line.split(delimiter)
#     if types:
#         fields = [ty(val) for ty, val in zip(types, fields)]
#     return fields

if __name__ == '__main__':
    print my_split('GOOD 100 490.50', [str, int, float])
    # pass

