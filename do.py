from register import register
import time
for i in range(2000):
	time.sleep(1)
	try:
		register()
	except:
		pass
