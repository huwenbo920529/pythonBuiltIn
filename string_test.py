# coding:utf-8
# 使用模板进行操作
import string

values = {'var': 'foo'}
t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
 """)
print('TEMPLATE:', t.substitute(values))

# 使用%进行操作
s = """
Variable         :%(var)s
Escape           :%%
Variable in text: %(var)siable
"""
print "INTERPOLATION:", s % values




