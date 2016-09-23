import sqlite3
conn = sqlite3.connect('bili.db')
cursor = conn.cursor()
getlist=cursor.execute('select * from bilivideo order by view desc limit 100;')
getone=getlist.fetchall()
for items in getone:
	print('av'+repr(items[0])+'    views'+repr(items[1])+'\n')
cursor.close()
conn.close()