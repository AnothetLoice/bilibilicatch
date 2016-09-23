import sqlite3
import apibase
conn=sqlite3.connect('bili.db')
cursor=conn.cursor()
cursor.execute('create table bilivideo(videonum int primary key,view int,danmaku int,reply int,favorite int,coin int,share int,now_rank int,his_rank int)')
beginning=0
ending=1000
while True:
	valuesinput=apibase.ApiTh(beginning)
	for items in valuesinput:
		valuesinput=[items.get('videonum'),items.get('view'),items.get('danmaku'),items.get('reply'),items.get('favorite'),items.get('coin'),items.get('share'),items.get('now_rank'),items.get('his_rank')]	
		cursor.execute('insert into bilivideo values (?,?,?,?,?,?,?,?,?)',valuesinput)
		print(valuesinput)
	beginning=beginning+1
	if beginning>ending:
		break
cursor.close()
conn.commit()
conn.close()
