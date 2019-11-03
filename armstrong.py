### 123 = 1**3 + 2**3 + 3**3

number = int(input("enter the number"))

temp = number
sum = 0
while(temp > 0):
    c = temp % 10
    sum += c ** 3
    temp = temp // 10
if number == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")