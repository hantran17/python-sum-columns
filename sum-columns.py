import pandas as pd
import numpy as np
import sys

def convert_list(num,df):
    a=(df.columns).to_list()
    col=df[a[num-1]].to_list()
    return col

def check_word(text):
    if type(text) == str:
        return 1
    else:
        return 0

def check_word_list(col):
    rm=[]
    for i in range(len(col)):
        if check_word(col[i]) ==1:
            rm.append(col[i])
    return rm

def del_word(col):
    rm=check_word_list(col)
    for i in range(len(rm)):
        col.remove(rm[i])
    return col

def sum_col(col):
    sum=0
    # a=(df.columns).to_list()
    for i in col:
        sum+= i
    return sum

# def main():
if __name__ == '__main__':
    # Check if no parameters
    if len(sys.argv) <= 1:
        print("\n")
        print("Usage:")
        print("$ python ./sum-columns.py <path-to-file.csv> <column-number>")
        print("\n")
        exit(0)

    file_name = (str(sys.argv[1]))
    num = (int(sys.argv[2]))
    df= pd.read_csv(file_name)
    df=df.dropna()
    col=convert_list(num,df)
    col=del_word(col)
    print('The total: ' +str(sum_col(col)))

