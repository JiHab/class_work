def counter(n=0):

    def func():
        nonlocal n
        print(n+1)
        n += 1
    return func

f1 = counter(4)
f2 = counter(-10)
f1()
f1()
f2()
f1()
f1()
f2()

def averager(n=1):
    x = 0

    def func(y):
        nonlocal n
        nonlocal x
        z = (x+y)/n
        print(z)
        x += y
        n += 1

    return func

F = averager()
F(10)
F(15000)
F(10751)