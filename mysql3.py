import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="Pass@123")
cursor = mydb.cursor()
# s = cursor.execute("insert into abhimanyu.bank_details values(58,'management','married','tertiary','no',2143,'yes','no','unknown',5,'may',261,1,-1,0,'unknown','no')")
# cursor.execute(s)
mydb.commit()
cursor.execute("select age, job from abhimanyu.bank_details where age= 58 and job = 'retired'")
# cursor.fetchall()
for i in cursor.fetchall():
    print( i)
