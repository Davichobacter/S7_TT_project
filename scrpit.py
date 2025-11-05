import os

print('My working directory is', os.getcwd())

x = 10

if x % 2 == 0:
    print(f'{x} is an even number')
else:
    print(f'{x} is an odd number')
