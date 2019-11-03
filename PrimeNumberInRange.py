# Write a program to display PRIME NUMBERS from 1 to n?

def isPrime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
        return True

def primeInRange(number):
    list = []
    isPrime = True
    for number in range(1,number):
        for n in range(2,number):
            if number % n == 0:
                isPrime = False
                break
        if isPrime == True:
            list.append(number)
    return list
# print(isPrime(8))
print(primeInRange(54))