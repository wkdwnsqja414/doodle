import urllib

import urllib2

url = "http://b10s.org"
user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
req = urllib2.Request(url)

################        POST data 있을때
#data = {'id':'J4ckP4rd', 'pw':'password'}
#data = urllib.urlencode(data)
#req = urllib2.Request(url, data)
###########################################

req.add_header("User-agent", user_agent) # 헤더추가
req.add_header("Cookie", "UserArr="+user_arr) # 쿠키 추가

response = urllib2.urlopen(req)
headers = response.info().headers #응답 헤더
the_page = response.read()

print the_page