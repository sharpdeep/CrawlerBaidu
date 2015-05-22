#coding=utf-8

import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS

baseUrl = 'http://www.baidu.com/s'
page = 1 #第几页
word = '穿戴设备'  #搜索关键词

data = {'wd':word,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
data = urllib.urlencode(data)
url = baseUrl+'?'+data

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
except urllib2.HttpError,e:
    print e.code
    exit(0)
except urllib2.URLError,e:
    print e.reason
    exit(0)

html = response.read()
soup = BS(html)
td = soup.find_all(class_='f')

for t in td:
    print t.h3.a.get_text()
    print t.h3.a['href']
    
    font_str = t.find_all('font',attrs={'size':'-1'})[0].get_text()
    start = 0 #起始
    realtime = t.find_all('div',attrs={'class':'realtime'})
    if realtime:
        realtime_str = realtime[0].get_text()
        start = len(realtime_str)
        print realtime_str
    end = font_str.find('...')
    print font_str[start:end+3],'\n'
    
