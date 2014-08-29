# -*- coding:utf-8 -*-
import codecs
import urllib
import urllib2
import cookielib
from toString import toString
from PIL import Image
import string, random
import re
import simplejson as json
def register():
	userFile=codecs.open('userlist.txt','a')
	header={'Host':'login.benshouji.com',
		'Origin':'http://login.benshouji.com',
		'Referer':'http://login.benshouji.com/?tn=passports&ac=reg',
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
	}
	cookie=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	urllib2.install_opener(opener)
	register=urllib2.urlopen('http://login.benshouji.com/?tn=passports&ac=reg')
	register=urllib2.urlopen('http://login.benshouji.com/index.php?mod=verifyimg')
	fp=open('image.png','wb')
	fp.write(register.read())
	fp.close()
	image=Image.open('image.png')
	text=toString(image).decode('utf-8','ignore').encode('utf-8','unicode')
	alist='qwertyuiopasdfghjklzxcvbnm1234567890'
	username=string.join(random.sample(alist,random.randint(8,15)),sep='')
	data={'username':username,
	'password':'123456789',
	'email':username+'@163.com',
	'repass':'123456789',
	'verify':text}
	postData=urllib.urlencode(data)
	request=urllib2.Request('http://login.benshouji.com/index.php?tn=passports&ac=doReg',postData,header)
	register=urllib2.urlopen(request)
	page=register.read()
	#print json.loads(page)['result']
	#print page
	if json.loads(page)['result']==1:
		print username+' regist succeed!'
		userFile.write(username+'\n')
	else:
		
		print username+' regist fail!'
	userFile.close()
if __name__=='__main__':
	register()