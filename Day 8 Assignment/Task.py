students =[
    {"name": "Arun", "marks": [78, 82, 90]},
    {"name": "Bala", "marks": [65, 70, 60]},
    {"name": "Chitra", "marks": [88, 92, 95]}
     ]
#1.Each student average mark

for student in students:
    student["average"]= sum(student["marks"])/len(student["marks"])
    print(student["name"],student["average"]) 


#o/p
#Arun 83.33333333333333
#Bala 65.0
#Chitra 91.66666666666667


#2.Highest average mark
    
highest_average = 0
for student in students:
    if student["average"]> highest_average:
        highest_average = student["average"]
        name = student["name"]
print("highest_average :",name,highest_average)


#o/p  highest_average : Chitra 91.66666666666667


#3.above 80 average

for student in students:
    if student["average"]>80:
        print(student["name"])
        
# Arun
# Chitra
