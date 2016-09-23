import urllib.request as request
def VideoGet(videourlnumber):
	videourl="""http://www.bilibili.com/video/av"""+repr(videourlnumber)+"""/"""
	videoresponse=request.urlopen(videourl)
	if videoresponse.getcode()==200:
		videohtml=(videoresponse.read()).decode('utf-8','ignore')
	return videohtml