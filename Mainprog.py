import random
import csv
import time
import tracemalloc

rows = []
csv_files = ['ingredient_6L.csv']
encodings = ['utf-8', 'iso-8859-1', 'cp1252']
headers = ['name']

print("Available row limits:")
row_limits = [1000, 3000, 9000]
for i, limit in enumerate(row_limits, 1):
    print(f"{i}. {limit}")
limit_choice = int(input("Enter the number of the row limit you want to select: ")) - 1

if limit_choice < 0 or limit_choice >= len(row_limits):
    print("Invalid choice. Exiting the program.")
    exit()

row_limit = row_limits[limit_choice]
if row_limit != 'all':
    row_limit = int(row_limit)
else:
    row_limit = float('inf')

row_count = 0

for file, header in zip(csv_files, headers):
    for encoding in encodings:
        try:
            with open(file, 'r', encoding=encoding) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if header in row and row[header] is not None:
                        rows.append(' '.join(row[header].split()))
                        row_count += 1
                    if row_count >= row_limit:
                        break
            if row_count >= row_limit:
                break
        except UnicodeDecodeError:
            pass
        if row_count >= row_limit:
            break
    if row_count >= row_limit:
        break

rows.sort()

def ternaryfunc(key):
    
    tracemalloc.start()

    start_time = time.perf_counter()
    start_memory = tracemalloc.take_snapshot()
    
    # Search the key using ternarySearch
    p = ternarySearch(1, len(rows), key, rows)
    # Print the result
    print("Index of", key, "is", p)
    
    end_memory = tracemalloc.take_snapshot()
    end_time = time.perf_counter()

    time_consumed = end_time - start_time
    memory_used = end_memory.statistics('lineno')[0].size

    print(f"Time consumed: {time_consumed} seconds")
    print(f"Memory used: {memory_used} bytes")

    tracemalloc.stop()

def ternarySearch(l, r, key, ar):

    if (r >= l):
        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        # Check if key is present at any mid
        if (ar[mid1] == key):
            return mid1
        
        if (ar[mid2] == key):
            return mid2
        
        # Since key is not present at mid,check in which region it is present
        # then repeat the Search operationnin that region
        if (key < ar[mid1]):
            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
        elif (key > ar[mid2]):
            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
        else:
            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1,
                                mid2 - 1, key, ar)
    # Key not found
    return -1

def skiplistfunc(target_value):
        
    # Create a skip list
    skip_list = SkipList()

    # Insert the sorted items into the skip list
    for row in rows:
        skip_list.insert(row)

    # Start time and memory counter
    tracemalloc.start()

    start_time = time.perf_counter()
    start_memory = tracemalloc.take_snapshot()

    # Search for the target value in the skip list
    if skip_list.contains(target_value):
        print(f"Found '{target_value}' in the skip list")
    else:
        print(f"'{target_value}' not found in the skip list")

    # End time and memory counter
    end_memory = tracemalloc.take_snapshot()
    end_time = time.perf_counter()

    time_consumed = end_time - start_time
    memory_used = end_memory.statistics('lineno')[0].size

    print(f"Time consumed: {time_consumed} seconds")
    print(f"Memory used: {memory_used} bytes")

    tracemalloc.stop()

def linearsearchfunc(target):
    
    tracemalloc.start()
    start_time = time.perf_counter()
    start_memory = tracemalloc.take_snapshot()
        
    # Perform linear search
    index = linear_search(rows, target)
    print(f"Searching for '{target}':")
    if index == -1:
        print(f"{target} not found.")
    else:
        print(f"{target} found at index {index}.")
        
    end_memory = tracemalloc.take_snapshot()
    end_time = time.perf_counter()

    time_consumed = end_time - start_time
    memory_used = end_memory.statistics('lineno')[0].size

    print(f"Time consumed: {time_consumed} seconds")
    print(f"Memory used: {memory_used} bytes")

    tracemalloc.stop()

def linear_search(data, target):
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1

def fibofunc(target):
    
    tracemalloc.start()

    start_time = time.perf_counter()
    start_memory = tracemalloc.take_snapshot()
    
    index = fibonacci_search(rows, target)

    if index != -1:
        print(f"Found at index {index}.")
    else:
        print("Not found.")
        
    end_memory = tracemalloc.take_snapshot()
    end_time = time.perf_counter()

    time_consumed = end_time - start_time
    memory_used = end_memory.statistics('lineno')[0].size

    print(f"Time consumed: {time_consumed} seconds")
    print(f"Memory used: {memory_used} bytes")

    tracemalloc.stop()

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

class Node:
    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [None]*height

class SkipList:
    def __init__(self):
        self.head = Node()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def find(self, elem, update=None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.elem == elem:
                return item
        return None

    def contains(self, elem, update=None):
        return self.find(elem, update) != None

    def randomHeight(self):
        height = 1
        while height < self.maxHeight and random.randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def insert(self, elem):
        _node = Node(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(_node.next))
        while len(self.head.next) < len(_node.next):
            self.head.next.append(None)

        update = self.updateList(elem)

        if self.find(elem, update) == None:
            x = self.head
            for i in range(len(_node.next)):
                while x.next[i] != None and x.next[i].elem < elem:
                    x = x.next[i]
                _node.next[i] = x.next[i]
                x.next[i] = _node
            self.len += 1
            
            
            
            
            
def main():
    print("Welcome to the program!")
    print("Please select an option:")
    print("1. Ternary Search")
    print("2. SkipList")
    print("3. Linear Search")
    print("4. Fibonacci Search")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            print("You selected Ternary Search.")
            target = input("Enter what string to search: ")
            ternaryfunc(target)
        elif choice == '2':
            print("You selected SkipList.")
            target = input("Enter what string to search: ")
            skiplistfunc(target)
        elif choice == '3':
            print("You selected Linear Search.")
            target = input("Enter what string to search: ")
            linearsearchfunc(target)
        elif choice == '4':
            print("You selected Fibonacci Search.")
            target = input("Enter what string to search: ")
            fibofunc(target)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()