def nFib(n):
    if n == 0 or n == 1:
        return n
    else:
        return (nFib(n-1) + nFib(n-2))

def nFibList(n):
    f = [1]
    if n == 0 or n == 1:
        return f[n]
    for i in range(2, n+1):
        f.append(nFib(i))
    return f

print(nFibList(5))


def nthFib(n, x=1, y=1, ls=[1]):
    if y == 1:
        n -= 2
    ls.append(y)
    if n == 0:
        return ls
    return nthFib(n-1, y, x+y, ls)



# Eficienta spatiu = O(1)
# Eficienta timp = O(n)
def nFibIterativ(n):
    if n <= 2:
        return 1
    x = y = 1
    n -= 2
    while n:
        x,y = y,(x+y)
        n -= 1
    return y

print(nFibIterativ(5))

