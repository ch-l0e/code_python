# 1. read names from names.txt and store in variable
names = [] #declares an empty list that can store our name string values

with open("./names.txt", "r") as data_file: #with is used for file input output read right. period means in relation to where the python file is located, within the same directory, look for name.txt. r means read the file
    #print(data_file.readlines()) #we printed list to see what happens
    for line in data_file.readlines():
        value = line.replace("\n", "")
        names.append(value) #.append() to add to back list
#print(names)

# 2. sort names alphabetically using selection sort algorithm
'''
Selection Sort Algorithm
    1. start with the first elemnt as the intial position
    2. find the smallest element in the unsorted portion of the array
    3. Swap this smallest element with the first unsorted element
    4. move the boundary of the sorted portion on element forward
    5. repeat steps 2.4 for the remailing unsorted elements until the entire array is sorted
'''

i = 0
while i < len(names):
    j = i + 1
    smallest_name = names[i]
    smallest_index = j
    while j < len(names):
        if names[j] < smallest_name:
            smallest_name = names[j]
            smallest_index = j
        j += 1
    if smallest_name < names[i]:
        names[i], names[smallest_index] = names[smallest_index], names[i]
    i += 1
print(f"Sorted names: \n{names}")

# 3. write names in new file called sortednames.txt
with open("sortedfile.txt", "w") as data_file: # w means write in file
    for line in names:
        data = f"{line}\n"
        data_file.write(data)
    print("sortednames.txt completed")