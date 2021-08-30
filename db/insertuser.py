from sqlite3 import *
conn=connect("info.db")
cursor=conn.cursor()
n=input("enter your name")
e=input("enter your email")
p=input("enter your phone")
cmd="insert into users(name,email,phone) values('&n','&e','&p')"
try:
     cursor.execute(cmd)
except Exception as ex:
     conn.rollback()
     print(ex)
else:
     conn.commit()
     conn.close()
