from sqlite3 import *
conn=connect("info.db")
cursor=conn.cursor()
cmd="create table users(uid integer primary key autoincrement unique,name varcher(30),email varchar(30)unique,phone varchar(15) unique)"
try:
     cursor.execute(cmd)
except Exception as ex:
     print(ex)
else:
     conn.close()
