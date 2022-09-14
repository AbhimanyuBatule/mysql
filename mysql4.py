import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Pass@123")
cursor = mydb.cursor()
# cursor.execute("show databases")
# print(cursor.fetchall())

# q1 = cursor.execute("select * from abhimanyu.persons")
# print(cursor.fetchall())

# cursor.execute("use abhimanyu")
# cursor.execute("drop table abhimanyu.persons")
# print(cursor.fetchall())

# cursor.execute("select * from abhimanyu.persons")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM abhimanyu.TABLES ")
# print(cursor.fetchall())

cursor.execute("use abhimanyu")
# cursor.execute("create table ass2(names varchar(30), email varchar(30))")
# cursor.execute("select * from ass2")
# print(cursor.fetchall())

# cursor.execute("insert into ass2 values('Abhi', 'Cartoon')")
# cursor.execute("select * from ass2")
# print(cursor.fetchall())
# mydb.commit()

# cursor.execute("insert into ass2 value('rupesh', 'gaikwad@gmail.com')")
# cursor.execute("select * from ass2")
# # print(cursor.fetchall())
# # mydb.commit()
#
# for i in cursor.fetchall():
#     print(i)