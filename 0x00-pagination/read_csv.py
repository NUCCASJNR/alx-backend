#!/usr/bin/python3
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    page = 2
    page_size = 10
    
    # Initialize a list to store the data for the page
    paged_data = []
    
    # Iterate through rows and collect data for the specified page
    for i, row in enumerate(reader):
        if i >= (page - 1) * page_size and i < page * page_size:
            paged_data.append(row)
    
    # Display the paged data
    for row in paged_data:
        print(row)
