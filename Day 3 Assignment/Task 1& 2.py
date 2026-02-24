#Task 2:

mark = int(input ("enter the mark"))
if mark>=90 and mark<=100:
    print("Grade A")
elif mark>=80 and mark<=89:
    print("Grade B")
elif mark>=70 and mark<=79:
    print("Grade C")
elif mark>=60 and mark<=69:
    print("Grade D")
else:
    print("Invalid mark")

#Task 1:

level1 =int(input("enter the level1score"))

if level1>7:
    print("level1round is clear")
    
    level2 =int(input("enter the level2score"))
    if level2>8:
        print("you are selected")
    else:
        print("rejected in level2")
    
else:
    print("rejected in level1")
