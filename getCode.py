#-*-coding:utf-8-*-
from selenium import webdriver
import time
from toString import toString
import cv
from PIL import Image
import codecs
def getCode(url,username):
	c=webdriver.Firefox()
	#time.sleep(5)
	c.get("http://login.benshouji.com/")
	time.sleep(1)
	c.find_element_by_id('uname'). send_keys(username)
	c.find_element_by_id('pwd').send_keys('123456789')
	c.find_element_by_id('loginbtn').click()
	time.sleep(15)
	c.get(url)
	c.execute_script('document.getElementById("linghao").click()')
	time.sleep(5)
	c.save_screenshot('screenshot.png')
	img = c.find_element_by_id("verifyImg2")
	loc = img.location
	image = cv.LoadImage('screenshot.png', True)
	out = cv.CreateImage((60,25), image.depth, 3)
	cv.SetImageROI(image, (loc['x'],loc['y'],60,25))
	cv.Resize(image, out)
	cv.SaveImage('out.png', out)
	image=Image.open('out.png')
	text=toString(image).decode('utf-8','ignore').encode('utf-8','unicode')
	c.find_element_by_name('verify').send_keys(text)
	c.find_element_by_id('lingqu').click()
	time.sleep(5)
	try:
		text=c.find_element_by_id('card').text
		fp=codecs.open(c.title,'a','utf-8')
		fp.write(text+'\n')
		fp.close()
	except:
		print 'error'
	c.quit()
	print text
if __name__ == '__main__':
	getCode('http://fahao.benshouji.com/holiday/5605003683/','6iy8lk2b')


'''cookie = cookielib.CookieJar()
for s_cookie in c.get_cookies():
    cookie.set_cookie(cookielib.Cookie(domain=s_cookie[u'domain'], name = s_cookie[u'name'], value = s_cookie[u'value'],path=s_cookie[u'path'],secure=s_cookie[u'secure'],rest=None,version =0,port=None,port_specified=False,domain_specified=False,domain_initial_dot=False,path_specified=True,expires=None,discard=True,comment=None, comment_url=None, rfc2109=False))
#print c.get_cookies()
#cookie.set_cookie(c.get_cookies())
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
register=urllib2.urlopen('http://fahao.benshouji.com/index.php?mod=verifyimg')
fp=open('image.png','wb')
fp.write(register.read())
fp.close()
image=Image.open('image.png')
text=toString(image).decode('utf-8','ignore').encode('utf-8','unicode')
print text
#c.close()'''