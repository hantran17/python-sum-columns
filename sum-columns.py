# Your code
import sys
import pandas as pd #Middle child syndrome?


# Check if no parameters
if len(sys.argv) <= 1:
    print("\n")
    print("Usage:")
    print("$ python ./sum-columns.py <path-to-file.csv> <column-number>")
    print("\n")
    exit(0)


file_name = (str(sys.argv[1]))
column_number = (int(sys.argv[2]))


#Read csv file
df = pd.read_csv(file_name)
column_headers = list(df.columns.values)  #Get the list of all column names from headers


#Sum of inputed column number
for line in df[column_headers[column_number]]:
    if line is not str:
        final = df[column_headers[column_number -1]].sum()
    else:
        continue


#people may come and go, but string must stay
print("The total 'amount' is " + str(final))
