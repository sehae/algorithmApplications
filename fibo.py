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

csv_files = ['cleaned_ingredients.csv', 'ingredient_6L.csv', 'unique_indexed_ingredients.csv']
encodings = ['utf-8', 'iso-8859-1', 'cp1252']
target = "Pinch of asafoetida salt, to taste"
headers = ['Descrip', 'name', 'descrip']

for file, header in zip(csv_files, headers):
    for encoding in encodings:
        try:
            with open(file, 'r', encoding=encoding) as csvfile:
                reader = csv.DictReader(csvfile)
                descriptions = [' '.join(row[header].split()) for row in reader if header in row and row[header] is not None]
            descriptions.sort()
            index = fibonacci_search(descriptions, target)
            if index != -1:
                print(f"Found in {file} at index {index}.")
            else:
                print(f"Not found in {file}.")
            break
        except UnicodeDecodeError:
            pass