
from numpy import append




def entryTime(s, keypad):
    list_of_number_to_add = []
    #verify Function constraints
    for num in s:
        try:
            assert abs(num) <= 9
        except:
            print("We found an issu with the file S")

    #verify Function constraints
    for num in keypad:
        current_location = num
        try:
            abs(num) <= 9
        except:
            print("We found an issu with the file keypad")
            break
    
    entry_time = keypad

    for num in keypad:
        current_location = num
        if current_location == keypad[0]:
            entry_time[1], entry_time[3], entry_time[4] = 1
            list_of_number_to_add.append[1]
            continue
        else:
            entry_time[2], entry_time[5], entry_time[6], entry_time[7], entry_time[8] = 2
            list_of_number_to_add.append[2]
            continue

        if current_location == keypad[1]:
            list_of_number_to_add.append[1]
            entry_time[0], entry_time[2], entry_time[3], entry_time[4], entry_time[5] = 1
            continue
        else:
            entry_time[6], entry_time[7], entry_time[8] = 2
            list_of_number_to_add.append[2]
            continue
        
    
        """
        example for the rest

        if current_location == keypad[3]:
            list_of_number_to_add.append[1]
            entry_time[0]
            continue
        else:
            entry_time[6]
            continue
        """
    

    #lopp for add each element of the list list_of_number_to_add
    time_taken = 0
    for number in list_of_number_to_add :
        time_taken += number
    
    return time_taken

s = [4,2,3,6,9,2  ]         
keypad = [9,2,3,8,5,7,6,1,4]
entryTime(s, keypad)
