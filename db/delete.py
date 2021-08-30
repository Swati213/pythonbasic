from sqlite3 import *
conn=connect("info.db")
cursor=conn.cursor()
cmd="delete from users where email='shalini34@gmail.com'"
try:
     cursor.execute(cmd)
except Exception as ex:
     conn.rollback()
     print(ex)
else:
     conn.commit()
     conn.close()
