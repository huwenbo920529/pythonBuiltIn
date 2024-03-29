# coding:utf-8
import decimal
from decimal import Decimal as D
from decimal import getcontext
print getcontext()
print getcontext().prec

print D(1) / D(3)


fmt = '{0:<25} {1:<25}'
print fmt.format('Input', 'Output')
print fmt.format('-' * 25, '-' * 25)

# Integer
print fmt.format(5, decimal.Decimal(5))

# String
print fmt.format('3.14', decimal.Decimal('3.14'))

# Float
f = 0.1
print fmt.format(repr(f), decimal.Decimal(str(f)))
print fmt.format('%.23g' % f, str(decimal.Decimal.from_float(f))[:25])
