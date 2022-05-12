# Recursive Function
# If a function calls himself the that is called recursive function.

"""def add(a, b):
    return a + b

print(add(2, 3))"""
########
# Factorial
"""print(1 * 2 * 3 * 4)""" # which is the 4's factorial
###########################################################
###################### Factorial Find By Python ##########
##########################################################

"""def factorial(numb):
    if numb == 1:
        return 1
    else:
        return numb * factorial(numb-1)

x = int(input("please give me a value for find factorial: "))
y = factorial(x)
print(f"Factorial value of {x}! is: {y}")
"""
######################## 
"""def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(4))"""

####################################
"""def factorial(num):
    if num == 1:
        return 1
    
    else:
        current_num = (num-1)
        return num * factorial(current_num)

print(factorial(4))"""
#################################################
############# Recursive #####################
##########################################

"""def recursive():
    print("I am from recursion")
    return recursive()
recursive()
"""

###############################################
################################################
###############################################
def factorial(numb):
    if numb == 1:
        return 1
    else:
        return numb * factorial(numb-1)

x = int(input("please give me a value for find factorial: "))
y = factorial(x)
print(f"Factorial value of {x}! is: {y}")