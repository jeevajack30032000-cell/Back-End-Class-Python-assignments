'''
task 1:
'''

number1 =float(input("enter the 1number"))
number2 =float(input("enter the 2number"))
number3 =float(input("enter the 3number"))
if number1>number2 and number1>number3:
    print("number one is the biggest number",number1)
elif number2>number1 and number2>number3:
    print("number two is the biggest number",number2)
else:
    print("number three is the biggest number",number3)

#another method
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 
num3 = float(input("Enter third number: "))

print("Biggest number is:", max(num1, num2, num3))

'''
task 2:
'''
username = input("enter the username: ")
password = input("enter the password: ")
if username == "admin" and password == "pass@123":
    print("valid user")
else:
    print("invalid user")
    
