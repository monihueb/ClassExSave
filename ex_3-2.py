test_list = [1, 3, 4, 53, 2, 6, 78, 100] # basic list

import math
even_n_list = list()
even_numbers = 0
for element in test_list:
     if element % 2 == 0 :
         even_numbers = even_numbers + element
         even_n_list.append(element)

sum_even = sum(even_n_list)
print(sum_even)
print(even_numbers)