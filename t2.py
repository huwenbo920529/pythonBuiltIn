# coding:utf-8
class Foo(object):
    def __init__(self, value):
        self.value = value


class Foo2(object):
    def __init__(self, value, filename):
        self.value = value
        self.logfile = file(filename, 'w')

    def __getstate__(self):
        """Return state values to be pickled."""
        f = self.logfile
        return self.value, f.name, f.tell()

    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        self.value, name, position = state
        f = file(name, 'w')
        f.seek(position)
        self.logfile = f


