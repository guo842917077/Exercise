import requests
# 引入cookielib 可以把本地cookie解析
import http.cookiejar as  cookielib
import re

# 1.在网页上登陆知乎
# 2.查看知乎post请求的url以及需要携带的数据，将参数拷贝出来，不能拷贝的参数使用request模拟请求，获取到response后，解析出来
# 3.如果需要一些数据无法获得，那么可以使用request先请求一下整个网页，然后解析出需要的字段
# 4.设置agent 表示是浏览器
url = "https:/www.zhihu.com"
# 5.表示客户端的类型，模拟成浏览器登陆
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": agent
}
##表示某一次连接
session=requests.session()
#指定cookie类型
session.cookies=cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_expires=True)
except:
    print("cookie未能加载")

def parseXrf():
    reponse_txt = requests.get(url, header=header)
    text = 'match params'
    match_txt = re.match('.*name="')
    if match_txt:
        return match_txt.group(1)
    else:
        return ""

def zhihu_login(account,password):
    post_data={
        "phone_num":account,
        "password":password
    }
    #使用session 的方式登陆
    response=session.post(url,data=post_data,header=header)
    #保存session
    session.cookies.save()


#检验是否登陆的思路：在没有登陆的情况下 访问其它页面会重定向到其它页面
#我们可以随便取一个url，使用session进行访问，查看它的返回值是否是200
#1。注意设置allow_redirects 防止重定向，如果重定向code也会是200，不会是302
#所以设置为进制重定向
def isLogin():
    url="sssss"
    reponse=session.get(url,header=header,allow_redirects=False)
    if reponse.status_code==200:
        return True
    else :
        return False