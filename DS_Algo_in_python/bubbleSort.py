list = [23,43,21,12,65,57,54,98]

def bubbleSort(list):
    for i in range(0, list.__len__() - 1):
        for j in range(0, list.__len__()-1-i):
           if list[j] > list[j + 1]:
               list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubbleSort(list))