##assignment
##  1. write a own program for each concepts below   [ marks 30 ]


## 1. if else

temp = 10.0

if temp>5.0:
    print("warning : fridge too warm")
else:
    print("normal temperature")


## 2. match case

menu_card =input("enter the option for order: ").upper()

match menu_card:
    case "A":
        print("chicken tikka masala")
    case "B":
        print("gralic naan")
    case "C":
        print("panneer butter masala")
    case "D":
        print("chicken Briyani")
    case _:
        print("error:choose correct option")


## 3. while loop

iphone = 20

while iphone>0:
    print("remaining stock: ",iphone)
    iphone-=1

print("sold out, notify me to get update if item reloaded")


## 4. for loop

letter = "mississippi"
for L in letter[::-1]:
    print(L,end="")
print()


## 5. list datatype [ write some data and display the data ]

insurance = ["jeeva",200000,3,"jawahar",150000,4,"kishore",300000,5]

insurance[5]= 2
insurance.pop()
insurance.append("anand")

print("updated data:",insurance)


## 6. function with parameter and with return type

def cardboard(length,width):
    rectangle=length*width
    return rectangle
length =50
width =65
result =cardboard(length,width)
print("the result is: ",result)

