import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="Pass@123")
print(mydb)
cursor = mydb.cursor()

q1 = cursor.execute("select * from abhimanyu.persons")
print(q1)
