import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#for name_1 in names_1:
#        if name_1 in names_2:
#            duplicates.append(name_1)

binary = BinarySearchTree('')
for name in names_1:
    binary.insert(name)
for name in names_2:
    if binary.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# The original runtime complexity is O(n^2) because it loops through the name_1 list n times (length of name_2) for each n.