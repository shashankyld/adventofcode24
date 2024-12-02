import numpy as np
import pandas as pd
import bisect

# Read the input file and access the two lists as python lists 
df = pd.read_csv("input.txt", sep=r'\s+', header=None, names=["List1", "List2"])

#Checking the success of df read
# print("df \n", df)
# print ("List1 \n", df["List1"])

# Arrange the Lists in assending order
List1 = sorted(df["List1"].tolist()) # Uses Time sort - Read about this (Merge + Insertion sort combo)
List2 = sorted(df["List2"].tolist())


# Checking the success of sorting
print("List1: ", List1)
print("List2: ", List2)

# Final Distance calculation
distance = 0
for i in range(len(List1)):
    distance += abs(List1[i] - List2[i])

# Answer for Part 1
print("Distance between two lists is: ", distance)

# Part2 : Similarity score

def count_occurances(x, List):
    # Binary search for item x in the List
    left_index = bisect.bisect_left(List, x)
    right_index = bisect.bisect_right(List, x)
    print("X_Left_Right_Index: ",x, left_index, right_index)
    if right_index-left_index == 0:
        return 0
    else: 
        # print(x, List[left_index-1:right_index+ 1])
        return(right_index - left_index )

similarity = 0
for i in List1:
    # Check # of occurances in List2 
    occurances = count_occurances(i, List2)
    similarity += occurances * i


print("Similarity between two lists: ", similarity)   