from sqlite3 import *
conn=connect("info.db")
cursor=conn.cursor()
cmd="select * from users"
try:
     cursor.execute(cmd)
except Exception as ex:
     print(ex)
else:
     records=cursor.fetchall()
     for record in records:
          for field in record:
                    print(field,)
          else:print("-"*30)
     conn.close()
