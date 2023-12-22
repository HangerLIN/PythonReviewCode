tuple1 = (i ** 2 for i in range(100))
print(type(tuple1))
print(tuple1)

x, y, z = sorted([1, 3, 2])
print(x, y, z)

t = (1,2,3)
t += (4,5,6)
print(t)
print(t[1:3])

# t = (1,2,3)
# t.append((4,5,6))
# print(t)

print( list(zip([1,2], [3,4])))

x = 3==3, 5
print(type(x))

x,y,z = map(str, range(3))
print(y)

