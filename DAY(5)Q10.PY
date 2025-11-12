# Using functools.reduce()
from functools import reduce
a = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

b = [ele for sub in a for ele in sub] 
res = reduce(lambda x, y: x * y, b)
print(res)