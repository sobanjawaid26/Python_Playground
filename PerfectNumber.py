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

print(isPerfect(496))