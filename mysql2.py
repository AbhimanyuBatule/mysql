import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="Pass@123")
cursor = mydb.cursor()
# s = cursor.execute("insert into abhimanyu.persons values('101', 'batule', 'abhi', 'shevgaon', 'nagar')")
# cursor.execute(s)
mydb.commit()
cursor.execute("select * from abhimanyu.persons")
for i in cursor.fetchall():
    print( i)