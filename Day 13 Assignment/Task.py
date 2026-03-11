##create set of objects using LIST datatype

class hotelreception:
    def __init__(customer, name, age, location, mobilenumber):
        customer.name = name
        customer.age = age
        customer.location = location
        customer.mobilenumber = mobilenumber


cus_1 = hotelreception("jeeva", 25, "kundharthur", "9094195156")
cus_2 = hotelreception("arun", 30, "chennai", "9876543210")
cus_3 = hotelreception("raja", 28, "bangalore", "9123456780")
cus_4 = hotelreception("vishwa", 29, "kk nagr", "9187657476")
cus_5 = hotelreception("jawahar", 30, "telugana", "9187654567")
cus_6 = hotelreception("santhosh", 28, "delhi", "9124637298")

cus = [cus_1, cus_2, cus_3,cus_4,cus_5,cus_6]

for customer in cus:
    print("customer details:", customer.name, customer.age, customer.location, customer.mobilenumber)

