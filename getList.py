# -*- coding:utf-8 -*- 
import urllib
import urllib2
import re
import string
from BeautifulSoup import BeautifulSoup
import codecs
import time
def getNum():
	item=urllib.urlopen('http://fahao.benshouji.com/lingqu').read().decode('utf-8','ignore').encode('utf-8','unicode').lower()
	num=re.search('共找到<em>.*?</em>',item)
	Num=re.search('\d+',num.group()).group()
	return string.atoi(Num,10) 
def getList():
	pageNum=getNum()
	fp=codecs.open('gameList.txt','w','utf-8')
	fp2=codecs.open('urllist.txt','w','utf-8')
	count=0
	for i in range(pageNum/8):
		time.sleep(5)
		item=urllib.urlopen('http://fahao.benshouji.com/lingqu/0_0_0_0_'+str(i+1)).read().decode('utf-8','ignore').encode('utf-8','unicode').lower()
		soup=BeautifulSoup(item)
		listTag=soup.find('div',{"class":'zmrv_lst'})
		listTag=listTag.findAll('dl')
		for i in listTag:
			name=i.dd.div.h3.a.contents[0]
			gameName=i.dd.div.p.contents[0]
			gameArea=i.dd.div.p.em.contents[0]
			link=i.dd.div.h3.a['href']
			fp.write(str(count)+' '+name+' '+gameName+' '+gameArea+' '+link+'\n')
			fp2.write(link+'\n')
			count+=1
	fp.close()
	fp2.close()
if __name__=='__main__':
	getList()