def a():
    b()
    print("a") 
    c()
    b()

def b():
    c()
    print("b")

def c():
    print("c")

a()
'''
When a() is executed, Python uses a call stack to keep track of which function is currently running and which function should run next after each call finishes. First, a() is placed on the stack. Inside a(), the program calls b(), so b() is pushed onto the stack. Since b() calls c(), c() is added to the top of the stack. After c() prints "c", it finishes and is removed from the stack, returning control to b(), which then prints "b". When b() ends, it is popped off the stack, and execution returns to a(). Next, a() prints "a" and calls c(), which is pushed onto the stack, prints "c", and then pops off. Finally, a() calls b() again, repeating the same process: b() pushes c() onto the stack, c() prints "c", returns, then b() prints "b" and returns. After all steps finish, a() is popped from the stack, and the program ends.
'''