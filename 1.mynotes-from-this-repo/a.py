def cf(num1,num2):
    n=[]
    for i in range(1, min(num1, num2)+1): 
        if num1%i==num2%i==0: 
            n.append(i)
    return n

print(cf(6,12))

# ====================================
 

a=8
a+=2
b=a
b+=3
c=b
print(c)
 
 
# ====================================
import sys
type = sys.argv[1]
if type == "t2.micro":
    print("we create instance")
elif type =="t3":
    print("ok")
elif type == "t4":
    print("ok")
else:
    print("we can not create instance ")

