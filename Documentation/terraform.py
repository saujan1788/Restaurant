def syntax:
   if  data: 
       When pulling data from external source this keyword is used. 

        "aws_vpc" "my_vpc" : Here my_vpc is more for a local ref 
    
    if variable:
        We can have different types like list, map, number, bool so on. and then say what do you expect 

        type = list(string)

    if resource:
        This is like creating a resoruce itself and can ref above things here 

            vpc_id = data.aws_vpc.my_vpc.id

def Modules:
    Instead of writing everything in main.tf , I can have submodules and then refer it in main.tf

    if module "network"{
                source = "./network" This is the directory
            }
    That's it though'
