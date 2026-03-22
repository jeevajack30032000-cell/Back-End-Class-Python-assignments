##Implement database connectivity for updater query and search query

##update

import mysql.connector

conn = mysql.connector.connect(host="localhost",database="collage_db",user="root",password="jeevajack@30032000",use_pure=True)

cursor1 = conn.cursor()

old_course=input("enter old course: ")
new_course=input("enter new course: ")

query ="update students_db SET course=%s where course=%s;"
values =(new_course,old_course)
cursor1.execute(query,values)

conn.commit()

conn.close()

print("updated successful")


##search

import mysql.connector

conn = mysql.connector.connect(host="localhost",database="collage_db",user="root",password="jeevajack@30032000",use_pure=True)

cursor1 = conn.cursor()

roll_no=int(input("enter the rool_no: "))
query ="SELECT * FROM students_db WHERE roll_no=%s"
values =(roll_no,)
cursor1.execute(query,values)

rows =cursor1.fetchall()

for row in rows:
    print(row)
    
cursor1.close()
conn.close()
