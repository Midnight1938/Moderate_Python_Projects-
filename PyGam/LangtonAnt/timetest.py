from time import time

n = 100000000



"""
Remainder Method. Fastest
"""
value, start = 0, time()
for i in range(n):
    value = (value + 1) % 2

print(f'% 2 time:{time() - start}')


"""
XOR method
"""
value, start = 0, time()
for i in range(n):
    value = value ^ 1
print(f'XOR time:{time() - start}')

"""
NOT Method
"""
value, start = 0, time()
for i in range(n):
    value = not value
print(f'NOT time:{time() - start}')