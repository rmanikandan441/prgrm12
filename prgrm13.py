def repeat(f, n, x):
    a = 0
    while a != n:
        x = f(x)
        a = a + 1
    return x

inc = lambda a: a+1
add = lambda a: lambda b: repeat(inc, a, b)
mult = lambda a: lambda b: repeat(add(a), b, 0)
power = lambda a: lambda b: repeat(mult(a), b, 1)

print (power(4)(8))
