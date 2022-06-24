import pandas as pd
import sys

# region Module Variables

csv_path = None
# Column index of file begin at 1 for the first column
col_index = None

# endregion

# region Utilities functions

# Verify one index exists or not in the list
def index_in_list(a_list, index):
    return index < len(a_list)


# endregion

# Main function
try:
    if not index_in_list(sys.argv, 1):
        csv_path = input("Please providing the csv file path: ")
    else:
        csv_path = sys.argv[1]

    if not index_in_list(sys.argv, 2):
        col_index = int(input("Please providing the column index: "))
    else:
        col_index = int(sys.argv[2])

    df = pd.read_csv(csv_path)

    # Converting the col_index inputted by user to python index and get it column name
    df_col_name = df.columns[col_index - 1]

    # Covert the column to numeric, in case if this colum contain the string value
    df[df_col_name] = pd.to_numeric(df[df_col_name], errors="coerce")

    print("The total '{}' is {}".format(df_col_name, df[df_col_name].sum(skipna=True)))

except FileNotFoundError:
    print("The csv file doesn't exist")
except IndexError:
    print("Column index doesn't exist")
except ValueError:
    print("Colum index need to be number")

