# list =  ["a", "b", "c"]
# print(list)


# # =========================

# list =  ["a", "b", "c"]
# print(list)
# print(type(list))


# # =================== adding new element to list           ===============================

# user_names=["a","b"]
# user_names.append("c")  ## added new user to existing list
# print(user_names)


# # ===================removing one  element to list           ===============================

# user_names=["a","b","c"]
# user_names.remove("c")  ## removing c  user  from existing list
# print(user_names)


# ## ===================  tuple does not allowin to add new elemlent ====================

# user_names=("a","b")
# user_names.append("c")  ## added new user to existing list
# print(user_names)

# # o/p ;   AttributeError: 'tuple' object has no attribute 'append'

# ## ===================    ====================


# user_names=["a","b","c","d"]
# print(user_names[2])
# print(len(user_names))
# user_names.append("e")
# print(len(user_names))

### ===================  SLICE  ====================

# a= ["a", "b","c","d","e"]
# print(a[2:4])       ##  O/P: ['c', 'd']


### ===================  SORT  ====================


# a= ["a", "b","c", "f", "d","e"]
# a.sort()   
# print(a)        ## o/p : ['a', 'b', 'c', 'd', 'e', 'f']


### =================== CONCATING   ====================

a= ["a", "b","c", "f", "d","e"]
 
print(a[0]+a[1] +a[2])        ## o/p :  abc
print(a[0]+a[1]+"--" +a[2])        ## o/p :   ab--c


### ===================    ====================


