# binary_search.py
from linear_search import numbers

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index != None:
        print(f"Target Found in index {index}")
    else:
        print("Target Not Found")

verify(binary_search(numbers, 4))