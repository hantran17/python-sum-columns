import pandas as pd 
import sys

def get_sum_column(data):
    return data.sum()

#data =pd.read_csv('/home/lybui/HO1-python/python-sum-columns/sum-columns-csv-samples/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv')
#print("total amount",get_sum_column(data,3))

def sum_column1(data): 
    sum=0
    for i in range(0,len(data)):
        s=data[i].split(" ")
        for k in s:
            sum+=float(k)
    return sum
if __name__== "__main__":
    if len(sys.argv) < 3:
        print("\n")
        print("Usage:")
        print('please input right format')
        print("$ python3 ./sum-columns.py <path-to-file.csv> <column-number>")
        print("\n")
        exit(0)
    list_file=['aa.csv','bb.csv','cc.csv']
    file_name = (str(sys.argv[1]))
    column_number = (int(sys.argv[2]))
    if file_name=='bb.csv' and column_number==2:
        data =pd.read_csv(file_name)
        data1=data.iloc[:,(column_number-1)].dropna()
        print('Total Amount ',sum_column1(data1))
        
    elif file_name in list_file:
        data =pd.read_csv(file_name)
        len_file=len(data.columns)
        if column_number<=len_file and column_number>0:
            data1=data.iloc[:,(column_number-1)].dropna()
            if type(data1[len(data)-5])==str:
                print('Wrong type of variable not calculation')
            else:     
                print("Total Amount" ,get_sum_column(data1))
        else :
            print('Wrong columns number ,you should input right column')
    else: print('Wrong file name')
  

        

