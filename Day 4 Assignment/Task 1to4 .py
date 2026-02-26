##task 1:

multiple = 5
count = 1
while count<=10:
    print(multiple,"x", count,"=",multiple*count)
    count+=1



##Task 2:

num = 1

while num <= 20:
    if num % 3 == 0:
        num += 1
        continue
    print(num, end=" ")
    num += 1



##Task 3:

i = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(j,"",end="")
    print()


##Task 4:

i = 1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,"",end="")
    print()

