from sqlite3 import *
conn=connect("info.db")
cursor=conn.cursor()
cmd="insert into users(name,email,phone)values('shalini','shalini34@gmail.com','8809765432')"
try:
     cursor.execute(cmd)
except Exception as ex:
     conn.rollback()
     print(ex)
else:
     conn.commit()
     conn.close()
