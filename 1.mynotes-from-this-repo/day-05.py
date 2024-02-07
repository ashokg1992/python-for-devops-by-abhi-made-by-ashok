import sys

def add(num1,num2):
    add = num1 +  num2
    return add

def mul (num1,num2):
    m= num1 * num2
    return m

num1 = float (sys.argv[1])
operation = sys.argv[2]
num2= float (sys.argv[3])

if operation == "add":
    output = add (num1, num2)
    print (output)
    
#  python Day-5.py 2 add 3    ; in the command line if we pass these values we get o/p

#  =====================================  ENVIRONMENTAL VARIALBES   ==============================================

# THESE ARE SENSTITVE DATA AND STAORED AS EnvironmenT VARAIBLES

# PASSWORDS
# API KEYS
# TOKENS
# CERTIFICATES

# in command line if we export this passwrd 
#  export password="ashok"
# - then write function to print and get this data 

import os
print (os.getenv("password"))
password = "ashok"

#  ================================================================









