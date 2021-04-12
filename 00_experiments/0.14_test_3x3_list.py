import numpy as np

n_layers = 3
n_rows = 3
n_cols = 4
nd_lst = np.arange(n_layers * n_rows * n_cols).reshape(n_layers, n_rows, n_cols)

# lst = [[[5 if k == 0 else 0 for k in range(n_cols)]for j in range(n_rows)]for i in range(n_layers)]
lst = [[[(i * n_rows * n_cols) + (j * n_cols) + k + 1 for k in range(n_cols)] for j in range(n_rows)] for i in range(n_layers)]
nd_lst = np.array(lst)
lst_transposed = nd_lst.transpose().copy()
print(nd_lst)

# the same without list comprehension
# for i in range(n_layers):
#     for j in range(n_rows):
#         for k in range(n_cols):
#             if k == 0:
#                 lst[i][j][k] = 5
#                 continue
#             if i == 0 and k != 0:
#                 lst[i][j][k] = 8
#                 continue
#             lst[i][j][k] = 0
# print(lst)
