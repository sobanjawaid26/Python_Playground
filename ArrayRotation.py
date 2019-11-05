list = [3,6,4,2,9]

### single rotaion

# last = list[0]
# rotated = []
# for i in range(1, list.__len__()):
#     rotated.append(list[i]);
# rotated.append(last)
# print(rotated)

### rotation by n element

def rotateByN(list, n):
    firstHalf= []
    for i in range(n + 1, list.__len__()-1):
        firstHalf.append(list[i])
    for i in range(0,n):
        firstHalf.append(list[i])
    return firstHalf
print(rotateByN(list, 2))