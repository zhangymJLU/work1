# -*- coding:utf-8 -*-
from ghost import Ghost
from toString import toString
import codecs
import time
ghost=Ghost(wait_timeout=60)
page,resources=ghost.open('http://login.benshouji.com/')
ghost.wait_for_page_loaded()
result, resources = ghost.fill("form", {"uname": "0a1rzbqwjfhg85","pwd": "123456789"})
page,resources=ghost.click("#loginbtn", expect_loading=True)
print 'login succeed'
page,resources=ghost.open('http://fahao.benshouji.com/holiday/5605004484/')
ghost.wait_for_page_loaded()
#ghost.click('#linghao')
result, resources=ghost.evaluate('document.getElementById("linghao").click();')
#ghost.fill('')
result,resources=ghost.evaluate('document,getElementById("")')
time.sleep(30)
print result
print resources
print type(ghost.cookies)
fp=codecs.open('test.html','w','utf-8')
fp.write(ghost.content)
#print ghost.content