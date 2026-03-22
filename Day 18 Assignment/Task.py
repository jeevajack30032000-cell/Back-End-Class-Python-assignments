##1.write simple programs for the following topic


#function with para, with return
#temperature_convertor


def temperature_convertor(c):
    F=(c*9/5)+32
    return F
c=25
Fahrenheit=temperature_convertor(c)
print("temperature=",Fahrenheit,"°F")


# while loop
#Sum of Digits Until Single Digit

NUM = int(input("enter the number: "))

while NUM>9:
    total= 0
    while  NUM>0:
        digit=NUM%10
        total+=digit
        NUM = NUM//10
    NUM=total
print("final single digit:",NUM)


# for

n = int(input("Enter rows: "))

for i in range(1, n+1):
    print("*" * i)

# list, set, tuple, dictionary

numbers =[10,20,30,40,50,60]
numbers.append(70)
numbers.remove(60)
print("updated list: ",numbers)

numbers =(60,90,70,80,50)
print("sliced tuple:",numbers[-2:])

numbers =numbers ={60,90,70,80,50}
numbers.add(40)
print("updated set:",numbers)

profile ={"name":"jeeva","age":25}
profile["age"]=22
print(profile)

# lambda function

def lambda_function(n):
    return lambda x: x*n
double=lambda_function(2)
print(double(5))
