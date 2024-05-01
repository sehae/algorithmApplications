import csv
def fibonacci_search(arr, x):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2

    while fib < len(arr):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_minus_2, len(arr) - 1)

        if arr[i] < x:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            offset = i
            

        elif arr[i] > x:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1

        else:
            return i

    if fib_minus_1 and offset < len(arr) - 1 and arr[offset + 1] == x:
        return offset + 1

    return -1

with open('cleaned_ingredients.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    next(reader, None)

    descriptions = []

    for row in reader:
        descriptions.append(row[1])

descriptions.sort()
target = "butter oil anhydrous"
index = fibonacci_search(descriptions, target)

if index != -1:
    print(f"Found at index {index}.")
else:
    print("Not found.")