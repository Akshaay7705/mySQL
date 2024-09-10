import mysql.connector 

conn = mysql.connector.connect( username="root",password="Akshaay@1234!", database="learning")

# ins = "insert into student (s_id, s_name) values (%s, %s)"
# val = (2, "Sameera")
# ins = "delete from student where s_id = %s"
# val = [1]


my_cursor = conn.cursor()

ins = "select * from student;"
my_cursor.execute(ins)
res = my_cursor.fetchall()
for i in res:
    print(i)
conn.commit()
conn.close()
print("Connected successfully")
