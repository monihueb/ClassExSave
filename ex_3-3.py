user_list = int(input("please enter number")) # creating list by user
for element in user_list:
    while element == 0 or element > 0:
        append(int(input("please enter another number"))) # add elements to list until negativ number is given

import math
        first_result=sum(user_list) #sum up list
        print(first_result)