x = y = z = 5

print(x)

values = [1,2,3,4,5]
first, *rest = values

a = b = first

a +=2

print(rest)
print(a)

values_second = (10,20,30)

a,b,c = values_second
print(c)

values_third = [1,2,3,4,5]
a,*b = values_third
print(b)

a,b = 10,20
c = a + b
print(c)

