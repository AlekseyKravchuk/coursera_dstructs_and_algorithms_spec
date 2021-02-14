a = [[1, 2], [3, 4]]
print(f'a = {a}, id(a) = {hex(id(a))}')

b = a
print(f'b = {b}, id(b) = {hex(id(b))}')

b.append([5, 6])

print(f'a = {a}'
      f'\tb = {b}')

c = a[:]
print(f'c = {c}, id(c) = {hex(id(c))}')

c.append([7, 8])
print()
print(f'a after appending [7, 8] to c: {a}')

c[0][0] = 111
print(f'a after appending modifying first element of c: {a}')
print(a)