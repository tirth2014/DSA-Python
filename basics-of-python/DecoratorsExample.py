# DECORATORS EXAMPLE:
# LearnHere: https://book.pythontips.com/en/latest/decorators.html

def im_decorator(a_fun):
    def wrapperFun():
        print("I'm flower executed before a_fun()")
        a_fun()
        print("I'm flower executed after a_fun()")
    return wrapperFun

def fun_i_need_decoration():
    print("I'm the function that needs some beautiful flower decoration to remove my foul smell!")

fun_i_need_decoration = im_decorator(fun_i_need_decoration)
fun_i_need_decoration()
# That is what Decorators is in simple terms!

print("------------↑ and ↓ both are same!------------------")

@im_decorator
def fun_i_need_decoration():
    print("I'm the function that needs some beautiful flower decoration to remove my foul smell!")
    
fun_i_need_decoration()

print(fun_i_need_decoration.__name__) # prints wrapperFun...which is not what we expected...it should have printed fun_i_need_decoration
# Well, our function was replaced by wrapperFun. It overrode the name and docstring of our function. Luckily, Python provides us a simple function to solve this problem and that is functools.wraps.

print("--------------Solution------------------")
from functools import wraps

def im_decorator(a_fun):
    @wraps(a_fun)
    def wrapperFun():
        print("I'm flower executed before a_fun()")
        a_fun()
        print("I'm flower executed after a_fun()")
    return wrapperFun
    
@im_decorator
def fun_i_need_decoration():
    print("I'm the function that needs some beautiful flower decoration to remove my foul smell!")
    
fun_i_need_decoration()
print(fun_i_need_decoration.__name__)  # prints fun_i_need_decoration
    
