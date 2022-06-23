# Your code
import csv
import sys

file = sys.argv[1]
column_num = int(sys.argv[2])
sum=0
list_column = []
with open(file, 'rt') as f:
    read = csv.reader(f)
    header = []
    header =  next(read)
    if column_num <= len(header) and column_num >= 0:
        for row in read:
            list_column.append(row[column_num])
        for num in list_column:
            if num.isnumeric():
                sum+=int(num)
            else:
                continue
        print("Total is: " + str(sum))
    else:
        print("colum isn't exist")
        exit(0)