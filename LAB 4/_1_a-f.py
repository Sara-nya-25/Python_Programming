print("Program 1a")
print("It will print test as the argument passed is not printed")
def foo(t):
    print("test")

foo("hej")

print("Program 1b")
print("It will print 3 5 as it didn't call the function and pass the arguments")
def fun1(x, y):
    return x * y

print(3, 5)

print("Program 1c")
print("It wiill print 15 as output as the function is called and the arguments are passed")
def fun1(x, y):
    return x * y

print(fun1(3, 5))

print("Program 1d")
print("It will print 125 as the function fun2 is called for x and also for y where it multiplies the arguments by 5 and again for the sum 25")
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

print("Program 1e")
print("It will print 7 as the function is not called and 2 is added to 'a' that is 5")
a = 5
def fun3(a):
    a += 1

a += 2
print(a)

print("Program 1f")
print("It outputs 18")
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)
