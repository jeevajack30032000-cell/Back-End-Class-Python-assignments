#looping statement

#1. The for Loop: Fixed Range
#Question: Write a program that prints all multiples of 5 between 1 and 50 (inclusive).
#Key Concept: Using a start, stop, and "step" value to jump through numbers efficiently

count=1
for Num in range(5,51,5):
    print("multiple of ","5 X",count,"=",Num)
    count+=1

#2.The while Loop: Positive Only Adder
#This is a "sentinel-controlled" loop. It keeps running as long as the user doesn't type 0. We also use an if statement inside to ignore negative numbers.

total = 0
num = int(input("Enter a number: "))
while num != 0:
    if num > 0:
        total = total + num
    num = int(input("Enter a number: "))

print("Total of positive numbers:", total)

#3.The for each Loop: Array Filtering
#Question: Given a list of names ["Alice", "Bob", "Charlie", "David", "Eve"], use a for each loop to print only the names that have more than 4 letters.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    count = 0
    for ch in name:
        count = count + 1
    if count > 4:
        print(name)



#Decision Making Statements

#1.The Range Check: Write a program that takes a student's score (0–100) and prints "Distinction" for 90+, "Pass" for 40–89, and "Fail" for anything below 40.
#using ladder if with while

Mark = int(input("enter the mark: "))
while Mark<0 or Mark>100:
    print("invalid mark")
    Mark = int(input("enter the mark: "))
    if Mark>=90 and Mark<=100:
        print("distinction")
    elif Mark>=40 and Mark<=89:
        print("pass")
    else:
        print("fail")
        
        
#The nested if Statement: The Deep Validation     
#2.Question: Write a "Bank Withdrawal" simulator.
#First, check if the withdrawal_amount is greater than 0.
#If it is, check if the account_balance is sufficient to cover the withdrawal.
#If both are true, deduct the money and print the new balance.
#If the first check fails, print "Invalid amount." If the second fails, print "Inadequate funds."
#Key Concept: Placing one decision inside another to handle complex dependency logic.

account_balance = 100000
print("account_balance =",account_balance)
cash_withdrawal=int(input("enter the amount: "))

if cash_withdrawal>0:
    if account_balance>=cash_withdrawal:
        account_balance -= cash_withdrawal
        print("withdrawn: ",cash_withdrawal)
        print("available_balance = ",account_balance)
    else:
        print("tranction failed:not enough amount available in your account")
else:
    print("invalid amount:please enter valid amount")
    

#  The if-else Statement: The Binary Choice
#3.Question: Create a "Voting Eligibility" checker. Ask the user for their age. If they are 18 or older, print "You are eligible to vote." If they are younger, calculate and print exactly how many years they still have to wait.

Age = int(input("enter the age: "))
if Age>=18:
    print("eligible for voting")
else:
    print("not eligible")
    
