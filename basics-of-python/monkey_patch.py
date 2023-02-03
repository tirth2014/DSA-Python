# In Python, the term "MONKEY PATCH" refers to dynamic (or run-time) modifications of a class or module. 
# In Python, we can actually change the behavior of code at run-time.

class A:
    def sayHi(self):
        print('I say Hi to everyone!')
        
        
def sayHello(self):
    print('hello there!')

A.sayHi = sayHello  # Changed the location of function sayHi() with location of function sayHello()

obj = A()
obj.sayHi() # hello there!
