#!/usr/bin/python3
import math
dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 34, 9, 87, 69, 34, 65, 78, 89, 43, 34]
print(len(dataset))
print(dataset[18])
# Parameters
page = 3
page_size = 6  # Number of items per page
print(math.ceil(len(dataset)) / page_size)
# Calculate the starting and ending indices for the requested page
start_index = (page - 1) * page_size
end_index = start_index + page_size
print(start_index)
print(end_index)
# Slice the dataset to get the desired page
paged_data = dataset[start_index:end_index]

# Print the paged data
print(paged_data)

# Paginating list of names
names = ['Al-Areef', 'Ayompo', 'Adegbite', 'Aa`isha', 'Al-Ameen', 'Biggie', 'Brr tob', 'Nuccas']
name = ('Al-Areef', 'Ayompo', 'Adegbite', 'Aa`isha', 'Al-Ameen', 'Biggie', 'Brr tob', 'Nuccas')

print(len(name))
page = 1
page_size = 5
start = (page -1) * page_size
end = start + page_size
data = name[start:end]
print(data)