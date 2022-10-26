
import numpy as np
import pandas as pd



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
            assert abs(num) <= 9
        except:
            print("We found an issu with the file keypad")
            break
    
    #get the array
    keypad = np.array(keypad)
    new_keypad = keypad.reshape((3,3))


    #
