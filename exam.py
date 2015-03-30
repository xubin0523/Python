class A:
	def __init__(self):
		self.health = 100
class B(A):
	def __init__(self):
		A.__init__(self)


def check_test():
    import ipdb; ipdb.set_trace() # BREAKPOINT
    y = B()
    print y.health

if __name__ == "__main__":
    x = B()
    check_test()
