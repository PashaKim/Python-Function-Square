print ("This function(square(side)) return perimeter, shape and diagonal of square")
a = int(input('a:'))
def square (a):
    p = a*4
    s = a**2
    d = a*(2**0.5)
    return p,s,("%.2f" % d)
print(square(a))