


def fab(n):
    f1, f2 = 1, 1
    for i in xrange(n):
        yield f1
        f1, f2 = f2, f1+f2
class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

if __name__ == "__main__":
    for n in Fab(5):
        print n
    for n in fab(5):
        print n
