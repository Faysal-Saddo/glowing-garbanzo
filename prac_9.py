num_1 = float(input())
num_2 = float(input())
added = num_1+num_2
added_type = added
added_type_1 = added_type.is_integer()  #is_integer() method. ⁠ This returns True if the float represents a whole number
if added_type_1  == True :
    added_1 = int(added)
    print(added_1)
else:
    print(added)