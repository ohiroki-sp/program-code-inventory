i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =',j)
print('i =',i)


x = [1, 2, 3, 4, 5]
y = x.copy()
#y = x[:]
y[0] = 100
print('y =',y)
print('x =', x)

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(x)
print(y)

x = ['a','b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(x)
print(y)
