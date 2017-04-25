#coding:utf-8
import re

import urllib2
def download(url, user_agent = 'GoodCrawler', num_retries = 2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries - 1)
    return html

h = download('http://www.pku.edu.cn/about/lrld/lrxz/index.htm#sjn')
#print h
#l1 = re.findall(' <td><p>(.*)(\s*)\n(.*)</td>',h)
l1 = re.findall(' <td><p>(.*)\n(.*)</td>',h)
nameintrolist = re.findall('</td>\n.*<td><span style="font-size:1.3em; color:#9b0000"><a name=".*"></a>(.*)</span></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n \t\t\t\t\t    <td><p>(.*)\n.*</td>', h)
#for l in l1:
# for i in l1:
#     print i
nilist = []
# for l in nameintrolist:
#     for i in l:
#         nilist.append(i)

for l in nameintrolist:
    l = list(l)
    #l[1] = l[1] + ("@")
    nilist.append("#".join(l))
#print nilist
ni = "@".join(nilist)
print ni
ni = "".join(ni.split(" "))

#print l1
# al = []
# for l in l1:
#     for i in l:
#         al.append(i)

# s = "#".join(al)
# print s



