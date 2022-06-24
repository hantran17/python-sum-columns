#!/usr/bin/python3
from cmath import nan
import csv
import sys
from fileinput import filename

# Check if no parameters
if len(sys.argv) <= 2:
    print("\n")
    print("Usage:")
    print("$ python ./sum-columns.py <path-to-file.csv> <column-number>")
    print("\n")
    exit()

file_name = (str(sys.argv[1]))
column_number = (int(sys.argv[2]))

total = 0

with open(file_name) as csv_file:

    csv_reader = csv.reader(csv_file)
    columns = next(csv_reader)
    
    if len(columns) < column_number:
        print("\n")
        print("Invalid column")
        print("\n")
        exit()

    
    for row in csv_reader:
        if row[column_number] is not nan:
            try:
                total = total + float(row[column_number])
            except ValueError:
                pass

    if total != 0:
        print("The total '", columns[column_number], "' is ", "{:,.2f}".format(total),sep="")
    else:
        print("Column ", columns[column_number], " is not calculable",sep="")
