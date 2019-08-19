# -*- coding: utf-8 -*-
import json


s = """[{"name":"\u9648\u5cf0\u54e5","phones":["13468675609"]},{"name":"\u5b5f\u519b\u52c7","phones":["13087526045"]}]
"""
# s = s.replace('[{', '{').replace('}]', '}').split('},{')
# if len(s) > 0:
#     s[0] += '}'
#     for i in range(1, len(s)):
#         s[i] = '{' + s[i]
# print s[0]
# print s[-1]
#
# a = json.loads(s[0])
# print a


# from ast import literal_eval
# my_list = literal_eval(s)
# print type(my_list)
# print type(my_list[0]), my_list[1]


# b = 'shuai wqej asui'
# b = b.split(' ', 1)[0]
# print b

# def func1(k):
#     k['hah'] = 1
#
# a = dict()
# b = dict()
# func1(a)
# b['a'] = a
# print b


import chardet
qq = "\u534e\u54e5\u54e5"
qq = 'u"{}"'.format(qq)
qqq = u"\u534e\u54e5\u54e5"
aa = "\xe5\x8d\x8e\xe5\x93\xa5\xe5\x93\xa5"
print qq
print eval(qq) == qqq
# print chardet.detect(qq)
# print chardet.detect(aa)
# print unicode(aa.decode('utf-8'))
print eval(qq) == aa.decode('utf-8')
# qqq = qq.decode("ascii")
# print type(qq.decode("ascii"))
# print type(aa.decode('utf-8'))
print aa == "华哥哥"
# print qq.decode("ascii").encode('utf-8')[0]
# print type(aa), aa[0]
# print type(unicode(qq.decode("ascii").encode('utf-8'))), aa.decode('utf-8')
# print unicode(qq.decode("ascii").encode('utf-8')) == aa.decode('utf-8')

