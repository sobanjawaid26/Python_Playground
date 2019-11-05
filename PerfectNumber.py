### Write program weather the number is PERFECT NUMBER or not?

def isPerfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False

# print(isPerfect(496))

# Write a program to display RANGE of PERFECT NUMBERS?

def listOfPerfectNumber(limit):
    list = []
    for i in range(1, limit):
        sum = 0
        for j in range(1, limit):
            if i % j == 0:
                sum += j
        if sum == i:
            list.append(i)
    return list

print(listOfPerfectNumber(100))