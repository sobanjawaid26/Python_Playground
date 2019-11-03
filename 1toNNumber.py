###  Write a program to Print 1 to N numbers?
def print1ToN(number):
    for num in range(1,number + 1):
        print(num, end = ' ')

### Write a program to Print REVERSE of N to 1 numbers?
def printRevNTo1(number):
    for num in range(number, 0, -1):
        print(num, end = ' ')

printRevNTo1(9)
print()
print1ToN(9)