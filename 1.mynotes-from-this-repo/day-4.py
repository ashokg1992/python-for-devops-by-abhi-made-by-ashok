#  once we write logic in function , to get that output  , we need to call/invoke it.
a=10
b=20
def add():
    print(a+b)
def sub():
    print(a-b)

add()  
# i  write  fucntions   for both add, sub, . but i call only add, so it prints only add, not sub. 
#  to print sub, we call sub also.



# ====================================================================================

# these are adv of writing code in functions:
# -----------------------------------
# reusability
# readability
# debugging

# def name():	# defining fucntion  

# - MODULE:
# ------------
# - module is group of fucntions
# - once import a module , we need to call it.


# import calculator_new as basic_calc	## we import  tihs module in above
# basic_calc	                          # and in this line we call  that module 
# basic_calc.addition()           # it means we call only that function from that module 

# =====================================================================================


#  function is should like this :
# - 1. it takes input
# - 2. perform the required operation
# - 3. return the output

# def sub (num1,num2 ):
#     s=num1 - num2
#     return s


# def add (num1,num2 ):
#     a =num1 + num2
#     return a


# def mul (num1,num2 ):
#     m = num1 *  num2
#     return m

# print (add(5,10))
# print (sub(15,20))
# print (mul(30,40))
## like this by writing in moudlr way we can give with diff values  for each function 

### ====================================    # PACKAGES:   ====================================

#   COLLECTION OF MOUDLES IS PACKAGE
# 
