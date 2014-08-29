用于笨手机网站（www.benshouji.com）提供的激活码自动领取。
脚本由python 2.7编写，请先安装python 2.7环境，
依赖于PIL，BeautifulSoup，pyocr，simplejson，selenium，opencv这几个第三方库，
需要有tesseract（用于验证码识别）和firefox浏览器两个软件。

使用时命令行运行 python run.py
游戏列表在gameList.txt文件中，
注册的用户用户名存放在userlist.txt中，密码为123456789
获取的邀请码在与游戏名同文件名的文本文件中
=====================================
0.0.1beta版
=====================================
实现功能：
1.获取全部提供激活码的游戏列表及页面地址
2.自动注册帐号
3.自动领取激活码

待改进：
1.稳定性较差
2.单线程，效率较低
3.验证码识码率低，识码率在20%-30%之间，不过可通过自己训练tesseract提高识码率（参考：http://my.oschina.net/lixinspace/blog/60124）
4.无图形界面
5.采用文件存储，未使用数据库
6.领码需要弹出浏览器