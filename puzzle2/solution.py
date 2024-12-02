import numpy as np
import pandas as pd

pd = pd.read_csv("input.txt", sep = r"\s+", header = None, names = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"])
print(pd.iloc[0].tolist())

n_rows = len(pd["c1"])
print("Number of rows: ", n_rows)



n_safe = 0
for i in range(n_rows):
    # print("##############START##############")
    # Check monotonic property
    flag = True
    row = pd.iloc[i]
    # print("row:", row)

    if row[1] - row[0] > 0:
        # Increasing
        for j in range(8):
            # print(row[j+1]-row[j])
            if row[j+1]-row[j] <= 0 or row[j+1]-row[j] >= 4:
                flag = False
    
    elif row[1] - row[0] < 0:
        # Decreasing
        for j in range(8):
            # print(row[j+1]-row[j])
            if row[j]-row[j+1] <= 0 or row[j]-row[j+1] >= 4:
                flag = False

    else: 
        flag = False
    # print("Flag: ", flag)
    # print("##############END##############")

    if flag==True:
        n_safe += 1

print("Number of safe observations: ", n_safe)

# Part 2 (Brute Force)

# Wrap the above into simple function

def is_row_safe(row):
    size = len(row)
    flag = True
    if row[1] - row[0] > 0:
            # Increasing
            for j in range(size-1):
                if row[j+1]-row[j] <= 0 or row[j+1]-row[j] >= 4:
                    flag = False
        
    elif row[1] - row[0] < 0:
            # Decreasing
            for j in range(size-1):
                if row[j]-row[j+1] <= 0 or row[j]-row[j+1] >= 4:
                    flag = False

    else: 
            flag = False
    return flag


def num_safe(pd):
    n_rows = len(pd["c1"])
    n_safe = 0
    for i in range(n_rows):
        # Check monotonic property
        
        row = pd.iloc[i]
        flag = is_row_safe(row)
        if flag==True:
            n_safe += 1

    print("Function Wrapper - Number of safe observations: ", n_safe)

                
# Testing the function
print(num_safe(pd))

# Brute force remove each element in a row and check if the row becomes safe in atleast once of the cases

final_n_safe = 0
for i in range(n_rows):
    row = pd.iloc[i].tolist()
    
    if is_row_safe(row)==True:
         final_n_safe += 1

    else:
         # Check by removing each of the nine elements, if in any case it becomes safe, add it to the final count
         for j in range(9):
              # Remove jth item from row
            #   print("len of row, j", len(row), j)
              if row[j] == np.nan:
                   continue
              else:
                   test_row = row[0:j] + row[j+1:9]
                   if is_row_safe(test_row) == True:
                        final_n_safe += 1
                        break
         

print("Number of safe reports after problem dampener: ", final_n_safe)
                        
              
         


