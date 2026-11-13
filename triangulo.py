dim = 11
simbolo = '*'

for i in range(1, dim+1):
    print(i*simbolo)
for i in range(dim, 0, -1):
    print(i*simbolo)
for i in range(1, dim+1):
    print(f'{i*simbolo:>{dim}}')
for i in range(dim, 0, -1):
    print(f'{i*simbolo:>{dim}}')
for i in range(1, dim+1, 2):
    print(f'{i*simbolo:^{dim}}')
for i in range(dim, 0, -2):
    print(f'{i*simbolo:^{dim}}')