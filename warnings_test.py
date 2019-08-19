# coding:utf-8
import warnings
warnings.filterwarnings("ignore")


warnings.simplefilter('always')


def fxn():
    warnings.warn("this is a warning", Warning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


with warnings.catch_warnings(Warning):
    warnings.warn("this is s warnings2", Warning)


warnings.warn("this is a warning3", Warning)


def fxn2():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter('always')
    fxn2()
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert "deprecated" in str(w[-1].message)
