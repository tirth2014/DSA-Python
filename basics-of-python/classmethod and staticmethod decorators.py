class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")

a = A()

a.foo(1)
a.class_foo(1)
a.static_foo(1)

A().foo(2)      #2
A().class_foo(2)  #2
A().static_foo(2)  #2

A.foo(2) # TypeError: foo() missing 1 required positional argument: 'x'
A.class_foo(2) #2