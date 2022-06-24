
import pandas as pd
import sys
# Check if no parameters
if len(sys.argv) != 3:
    print("\n")
    print("Usage:")
    print("$ python ./sum-columns.py <path-to-file.csv> <column-number>")
    print("\n")
    exit(0)

file_name = (str(sys.argv[1]))
col_number = (int(sys.argv[2]))

df = pd.read_csv(file_name)
col_list=list(df.columns.values)

Total=0
for i in  df[col_list[col_number]]:
  if type(i) == int or float:
    Total=df[col_list[col_number]].sum()
  else:
    continue
print("The total is" ,str(Total))