import pandas as pd
import numpy as np

# Read the text file
data = open("input.txt", "r").read()
print("data: ", data)

# Example dkjlangdfmul(12,34)sdggsd
# Idea is to use "mul(",    ",",     ")" as the separators
seps = ["mul(",    ",",     ")"]

parts = data.split(seps[0])
# print("parts: ", parts)
# In each part, if there is a,b) pattern immedietly at the start then it counts
total_sum = 0
for part in parts:
    parts_2 = part.split(seps[1])
    parts_2_l = parts_2[0]
    # This parts_2_l should be a int with less than three digits
    if len(parts_2_l) > 3:
        continue 
    try: 
        left_number = int(parts_2_l)
    except:
        continue
    # Same logic for this, where pattern should be "a)", where a has less than 3 digit and be an int
    parts_2_r = parts_2[1].split(seps[2])[0]
    if len(parts_2_r)>3:
        continue
    try: 
        right_number = int(parts_2_r)
    except:
        continue
    # print(part, parts_2_l, parts_2_r)
    total_sum += left_number * right_number
    # print("left number, right number, product and totalsum: ", left_number, right_number, left_number*right_number, total_sum)
print("total_sum: ", total_sum)

# Part 2
# Addition of do() and dont() logic,
# For every part, look at the previous part and see if there is any logic present and switch the flag, by default the logic is do()

flag = True
previous_part = ""
total_sum = 0

def check_logic(part, logic):
    ''' 
    Given a part, checks the last updated logic
    '''
    sub_parts = part.split("()")
    print("sub parts: ", sub_parts)
    # Iterate through sub parts from the end and check if there is a logic unit 
    for i in range(len(sub_parts)):
        last_subpart = sub_parts[-1-i]
        print("last_subpart: ", last_subpart)
        print(last_subpart[-2:], last_subpart[-5:])
        if last_subpart[-2:] == "do":
            logic = True
            print("do")
            break
        elif last_subpart[-5:] == "don't":
            logic = False
            print("don't")
            break
    return(logic)



for part in parts:
    print("previous_part =", previous_part)
    flag = check_logic(previous_part, flag)
    print("flag: ",flag)
    previous_part = part
    

    parts_2 = part.split(seps[1])
    parts_2_l = parts_2[0]
    # This parts_2_l should be a int with less than three digits
    if len(parts_2_l) > 3:
        continue 
    try: 
        left_number = int(parts_2_l)
    except:
        continue
    # Same logic for this, where pattern should be "a)", where a has less than 3 digit and be an int
    parts_2_r = parts_2[1].split(seps[2])[0]
    if len(parts_2_r)>3:
        continue
    try: 
        right_number = int(parts_2_r)
    except:
        continue
    # print(part, parts_2_l, parts_2_r)

    
    if flag == True:
        total_sum += left_number * right_number
    print("left number, right number, product and totalsum: ", left_number, right_number, left_number*right_number, total_sum)
print("total_sum: ", total_sum)




'''
# NOT A GOOD APPROACH

print("seps: ", seps)
total_sum = 0
for i in range(len(data)):
    left_num = None
    right_num = None 

    while i+4 < len(data):
        if data[i:i+4] == seps[0]:
            # Likely a good subpart
            # Check for next ","
            j = 0
            comma_flag = False
            while not comma_flag:
                # Check if the index is possible
                try:
                    index_test = data[i+4+j]
                except: 
                    continue
                if data[i+4+j] == seps[1] and j<=2:
                    comma_flag = True
                    # You found a comma, check the string between these two seperators is an int and has less thn 3 digits
                    try:
                        left_num = int(data[i+4:i+4+j]) 
                    except:
                        continue
                elif j>2:
                    continue
                j+=1
            print("left number: ", left_num)

            # # Now check for the next sep which is ")" and see if the number in between is an int
            # k = 0
            # end_braces_flag = False
            # while not end_braces_flag:
                # 

'''



