### we have  this file day-12-server.conf, in that file , i want to change "MAX_CONNECTIONS=" this data.
###


def update_server_config(file_path,key,value):  # we first def/write function  for this , we give these details for the file later 
    with open(  file_path,"r") as file :        # we just assign "alias" for this
        lines = file.readlines( )   # readlines is inbuilt function to  read and copy all data in that file and assign to  variable that we assigned "lines"
        
    with open (file_path, "w") as file :
        for line in  lines:     # it   check each line and check whihc line it need to update
            if key in line:
                file.write(key + "=" + value + "\n")    # if condition is match  then update with that key and value and move to new line
            else:
                file.write(line)    # it means just print same lines if condition is not matches

update_server_config("day-12-server.conf","MAX_CONNECTIONS", "1000")

### now run this script and the data is updated in ay-12-server.conf file.
        
    
