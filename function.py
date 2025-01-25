names = ["anmol","aka","adi","paddi","harsh","singh"]

def print_list(list):
    for l in list:
        print(l,end=(" "))


print_list(names) 

##########################################

def fact(num):
    factt=1
    while num!=0:
        factt*=num
        num-=1
    return factt   

print("the fact",fact(5)) 

###############################################
def sumnatural(num):
    
    if(num==0):
        return 0
    
    return num+sumnatural(num-1)


print(sumnatural(5))
# #################################
def sumnatural(num):
    
    if(num==0 or num == 1):
        return 1
    
    return num*sumnatural(num-1)


print(sumnatural(4))