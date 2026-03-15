##deliver free calculator (logical operators) :- using if else condition
##ConditionFeeDistance < 2km AND Order > $20$0 (Free)Distance < 5km$3.00Anything else$5.00

distance = 5
order_fees = 25

if distance<2 and order_fees>20:
    print("free delivery")
    
elif distance<5:
    print("deliery fee = $3.00")
    
else:
    print("delivery fee = $5.00")

##smart phone battery alert :- using the while loop statemnet

battery =int(input("Enter battery percentage: "))

while battery > 0:
    if battery <= 20:
        print("Low Battery! Charge your phone.")
        break
    else:
        print("current battery level:",battery,"%")
        break

#collection processing using for loop

item_prices =[12, 45, 8, 120, 3, 55]
total_sum = 0

for item in item_prices:
    if item>10:
        total_sum += item
        
print("total items price over 10 is : ",total_sum)



#Multi_level inheritance

class principle:
    def meeting(self):
        print("principle is going to meeting")
class vice_principle(principle):
    def takeover(self):
        print("vice principle is incharge now")
class Hod(vice_principle):
    def hod_meeting(self):
        print("hod meeting is going to happen its is vice principle call")

clg= Hod()
clg.meeting()
clg.takeover()
clg.hod_meeting()

#class and object

class Airport:
    def __init__(self, plane_count=0, passenger_count=0):
        self.plane = plane_count
        self.passenger = passenger_count

    def update_phase(self):
        self.plane = int(input("Enter total planes in lane 1: "))
        self.passenger = int(input("Enter total passengers in phase 1: "))

    def show_report(self):
        print("AIRPORT REPORT")
        print("Total Planes: ",self.plane)
        print("Total Passengers: ",self.passenger)
     

air = Airport()
air.update_phase()
air.show_report()


#list

movies = ["horror", "romance", "sci-fi", "comedy", "adventure"]

movies.append("action")
movies[3] = "fantasy"
movies.remove("horror")
print("Updated List: ",movies) 


#tuple

user_data = ("jeeva", "30-03-2000", 177, 93.5, "male")

print("Username: ",user_data[0])
print("Items in tuple: ",(user_data[0:5]))
print("Items in tuple: ",(user_data[::-1]))    
