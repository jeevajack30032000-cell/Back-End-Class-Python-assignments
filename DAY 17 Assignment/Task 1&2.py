#Implement multithreading for any real time example

import threading
import time

def prepare_food():
    print("Food preparation started...")
    time.sleep(3)
    print("Food prepared!")

def pack_food():
    print("Waiting for food to be prepared...")
    time.sleep(3)
    print("Packing food...")
    time.sleep(2)
    print("Food packed!")

def deliver_food():
    print("Waiting for food to be packed...")
    time.sleep(5)
    print("Delivering food...")
    time.sleep(2)
    print("Food delivered!")

t1 = threading.Thread(target=prepare_food)
t2 = threading.Thread(target=pack_food)
t3 = threading.Thread(target=deliver_food)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

#write studnet's rollno, name in a file and then display it on screen

file = open("C:\\Users\\CHARU\\Documents\\sample test for file.txt","w")

rollno = input("enter roll number: ")
name = input("enter name: ")
    
file.write(rollno + "," + name)
file.close()

file = open("C:\\Users\\CHARU\\Documents\\sample test for file.txt","r")
data = file.read()
file.close()

roll, name = data.split(",")

print("student rollno: ",roll)
print("student name: ",name)
