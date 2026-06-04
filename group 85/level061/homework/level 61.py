nums = [1, 2, 3, 5.5, 6.2, 10.1, 7]
result = round(sum(nums)) 

import math
nums = [33, 23, 3, 2.3, 9.2, 14.1, 7]
result = math.floor(sum(nums)) 

import math
nums = [21, 7, 3, 3.1, 2.2, 10.1, 7]
result = math.ceil(sum(nums)) 

import math
nums = [1.0111, 2.2229, 5.01341, 10.000003]
result = math.trunc(sum(nums)) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -5, -2, 20, 15, -20, 7]
final_list = []

for x in numbers:
    if x < 0:
        final_list.append(x ** 2)
    elif 0 < x < 10:
        final_list.append(x ** 3)
    else:
        final_list.append(x ** 5)

print(final_list)