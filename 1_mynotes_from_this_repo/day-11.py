 
### ==========================================

# student_info = {
#     "name" : "ashok",
#     "age" : "30" ,
#     "city" : "bangalore"
    
    
# }
# print(student_info["name"])
# print(student_info["age"])

### ================= MULTIPLE DICTIONALRIES =================

# ec2_instances = [
#     {
#         "id" : "instance-000",
#         "type" : "t1"
#     },
      
#     {
#            "id" : "instance-002",
#         "type" : "t2"
#     },
#     {
#          "id" : "instance-003",
#         "type" : "t3"
#     },
# ]
# print(ec2_instances[2]["type"]) # if we want instance-003 is what type , then we do this 

# print(ec2_instances[1]["type"]) # if we want instance-002 is what type , then we do this 
# print(ec2_instances[0]["id"])  

### ======================  GET  PULL REQUESTS INFORMATION ON A REPO USING PYTHON ==========================

### pip install requests  # install in command line
# "api.github.com/repos/org_name/accoount_name/pulls"

# "api.github.com/repos/kubernetes/kubernetes/pulls"
# "api.github.com/repos/gashok1992"


# import requests
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response) # it prints above api request information
# print(response.status_code) # it prints status code of above api requests, if it success , code =200, fail=400, aunthenticaionfailed=403


### ========================= 


# import requests
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# complete_details = response.json()
# print(complete_details[0]["id"])        # it means we get in the above json data, we get first user [0] of id
# print(complete_details[0]["user"] ["login"]) 

### =================================================

# import requests
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# complete_details = response.json()
# for i in range(len(complete_details)):  # it prints all users names 
    
#     print(complete_details[i]["user"] ["login"]) 


### =========================== SET ================================

