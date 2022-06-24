import pandas as pd
import sys
import os
import numpy as np

if len(sys.argv) != 3:
    print("\n")
    print("Usage:")
    print("$ python ./sum-columns.py <path-to-file.csv> <column-number>")
    print("\n")
    exit(0)

file_name = (str(sys.argv[1]))  
column_number = (int(sys.argv[2]))

file_path = (os.path.dirname(os.path.realpath(sys.argv[0]))+(str(sys.argv[1])))
#reduce filepath to ./sum-columns-csv-samples/<filename>

csv_file=pd.read_csv(file_name)

_colname=[]

for _var in csv_file.columns:
    _colname.append(_var)
    _len = len(_colname)

if int(sys.argv[2]) < 0 or int(sys.argv[2]) > (_len-1) :
    print ("Column number is invalid !")
    exit(0)
    
if csv_file.dtypes[(_colname[column_number])] == np.int64 or csv_file.dtypes[(_colname[column_number])] == np.float64 :
    # print (csv_file.dtypes[(_colname[column_number])])
    _result=csv_file[_colname[column_number]].sum()
    print (f"The table has {_len} columns")
    print (f"The sum of {_colname[column_number]} is {_result}")

else:
     print ("Data type is not correct !")
