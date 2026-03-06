#find biggest number in the list

list_elements =[200,500,2000,800,700]

assign_big = 0

for big in list_elements:
    if big>assign_big:
        assign_big = big
print("biggest number is",assign_big)

#noparameter,noreturn_type

def biggestnumber():
    big_num = 0
    elements=[100,90,80,70,60]
    for big in elements:
        if big>big_num:
            big_num = big
    print("biggest number is",big_num)

biggestnumber()

#with parameter,noreturn_type

def biggestnumber(big_num,elements):
    for big in elements:
        if big>big_num:
            big_num = big
    print("biggest number is",big_num)

big_num = 0
elements=[23,36,4879,89]
biggestnumber(big_num,elements)
    

#with parameter,withreturn type

def biggestnumber(big_num,elements):
    for big in elements:
        if big>big_num:
            big_num=big
    return big_num
big_num = 0
elements=[1000,20000,2535456]
result=biggestnumber(big_num,elements)
print("biggest number is",result)

#no parameter,with return type

def biggestnumber():
    big_num = 0
    elements=[1000,2000,3000,5000]
    for big in elements:
        if big>big_num:
            big_num = big
    return big_num
result=biggestnumber()
print("highest number is",result)




