
class A:
    def display(self):
        print "A"
class B:
    def display(self):
        print "B"
class C(A):
    pass
class D(C, B):
    pass
    pass
    pass

d = D()
d.display()#A

O = object

class X(O): pass
class Y(O): pass
class F(X, Y): pass
class G(Y, X): pass
class H(F, G): pass

