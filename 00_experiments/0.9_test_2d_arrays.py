# Create a 2D array
rows, cols = (5, 5)
# TO DO!!! Figure out why below construction of creating array works improperly
arr = [[None]*cols]*rows
# arr = [[None for i in range(cols)] for j in range(rows)]
print(f'array before editing: {arr}')
arr[0][0] = 9
print(f'array AFTER editing: {arr}')

