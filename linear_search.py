# linear_search.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index != None:
        print(f"Target Found in index {index}")
    else:
        print("Target Not Found")
        