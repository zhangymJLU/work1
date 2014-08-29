#-*-coding:utf-8-*-
from register import register
from getList import getList
from getCode import getCode
import codecs
def doRegister():
	for i in range(1000):
		time.sleep(1)
		try:
			register()
		except:
			pass
	print u'自动注册结束'
def doGetList():
	getList()
	print u'列表更新结束'
def doGetCode():
	urlfp=codecs.open('urllist.txt','r','utf-8')
	url=urlfp.readline()
	while url:
		count=0
		userfp=codecs.open('userlist.txt','r','utf-8')
		user=userfp.readline()
		while user:
			if count>250:
				break
			try:
				getCode(url=url,username=user)
			except:
				print "error"
			count+=1
			user=userfp.readline()
		print url+u'领取结束'
		url=urlfp.readline()
	print u'领取结束'
def showAction():
	print u'请选择要进行的动作'
	print u'1.更新列表'
	print u'2.自动注册用户'
	print u'3.领码'
	print u'0.退出'
def main():
	print u'笨手机领号系统'
	showAction()
	tip=raw_input()
	while tip:
		if tip=='0':
			exit()
		if tip=='1':
			try:
				doGetList()
			except:
				print u'更新失败，请重试'
		if tip=='2':
			try:
				doRegister()

			except:
				print u'注册失败，请重试'
		if tip=='3':
			#try:
			doGetCode()
			#except:
			#	print u'领码失败，请重试'
		showAction()
if __name__ == '__main__':
	main()






