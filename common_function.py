# map
#Iterable: list, tuple, set, dictionary, string

"""nums =[20, 30, 50, 40]
print(map(lambda x: x **3 , nums))"""

##################################################

"""nums =[20, 30, 50, 40]
print(list(map(lambda x: x **3 , nums)))"""
####################################################
"""nums = [20, 30, 40, 50]
print(list(map(lambda x: x * 2, nums)))"""
################################################
"""def multiply(a):
    return a * 2
nums = [200, 30, 50, 40]
print(list(map(multiply, nums)))
"""

######################################################################
############### Filter Function ##############################
###########################################################
"""nums = [2, 3, 50, 4]
print(list(filter(lambda x: x % 5 == 0, nums)))
"""

######################################################################
############### Reduce ##############################
###########################################################

from functools import reduce

"""num_list = [2, 3, 4, 5]
print(reduce(lambda x,y: x + y, num_list))"""

####################
"""num_list = [2, 3, 4, 5]
print(reduce(lambda x, y: x * y, num_list, 100))"""
# last value depend on x * y 
# if this is * . then 100 will be multiply with the result
# if this is + then 100 will be adding with the result


###### Range
print(list(filter(lambda x: x % 5 == 0, range(1,20))))

