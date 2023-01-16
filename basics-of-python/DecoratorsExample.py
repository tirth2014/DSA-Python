# DECORATORS EXAMPLE:
# LearnHere: https://book.pythontips.com/en/latest/decorators.html


def im_decorator(a_fun):
    def wrapperFun():
        print("I'm flower executed before a_fun()")
        a_fun()
        print("I'm flower executed after a_fun()")
    return wrapperFun()

def fun_i_need_decoration():
    print("I'm the function that needs some beautiful flower decoration to remove my foul smell!")

fun_i_need_decoration = im_decorator(fun_i_need_decoration)   # Decorator in simple terms
# Now, fun_i_need_decoration() is wrapped inside the wrapperFun()

print("------------↑ and ↓ both are same!------------------")

@im_decorator
def fun_i_need_decoration():
    print("I'm the function that needs some beautiful flower decoration to remove my foul smell!")
