# The correct solution.
numIceCream = int(input())
iceCreams = [int(x) for x in input().split()] # This is how you can take an array of integers as input. 
# Do not forget that inputs are given as strings. Hence you have to convert them.

print(sum(iceCreams) - min(iceCreams))

"""
DO NOT USE THIS ONE
This is only for the sake of example. It is used to show "time limit exceed" problem.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break

    return arr

numIceCream = int(input())
iceCreams = [int(x) for x in input().split()]

iceCreams = bubbleSort(iceCreams)

print(sum(iceCreams) - iceCreams[0])
"""
