import urllib.request as request
import json
import threading
def ApiBase(basenumber=1):
	baseapi='http://api.bilibili.com/archive_stat/stat?aid='
	jsonurl=baseapi+repr(basenumber)
	jsonres=request.urlopen(jsonurl)
	jsondata=(json.loads((jsonres.read()).decode('utf-8'))).get('data')
	jsondata.update({'videonum':basenumber})
	return jsondata
def ApiUp(lenth=100,begin=0,back=[]):
	zipdata=[]
	for i in range(begin,begin+lenth):
		if i !=0:
			zipdata.append(ApiBase(i))
	back.extend(zipdata)
def ApiTh(num):
	num=num*10
	wth=10
	threads = []
	backdata=[]
	t1 = threading.Thread(target=ApiUp,args=(wth,num*wth,backdata))
	threads.append(t1)
	t2 = threading.Thread(target=ApiUp,args=(wth,num*wth+wth,backdata))
	threads.append(t2)
	t3 = threading.Thread(target=ApiUp,args=(wth,num*wth+2*wth,backdata))
	threads.append(t3)
	t4 = threading.Thread(target=ApiUp,args=(wth,num*wth+3*wth,backdata))
	threads.append(t4)
	t5 = threading.Thread(target=ApiUp,args=(wth,num*wth+4*wth,backdata))
	threads.append(t5)
	t6 = threading.Thread(target=ApiUp,args=(wth,num*wth+5*wth,backdata))
	threads.append(t6)
	t7 = threading.Thread(target=ApiUp,args=(wth,num*wth+6*wth,backdata))
	threads.append(t7)
	t8 = threading.Thread(target=ApiUp,args=(wth,num*wth+7*wth,backdata))
	threads.append(t8)
	t9 = threading.Thread(target=ApiUp,args=(wth,num*wth+8*wth,backdata))
	threads.append(t9)
	t10 = threading.Thread(target=ApiUp,args=(wth,num*wth+9*wth,backdata))
	threads.append(t10)
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	return backdata