import requests,re
import time

def func(url):
    data = requests.get(url)
    data.encoding = 'UTF-8'
    data = data.text
    strd = re.search(r'<p>(.*)</p>',data)
    strd = strd.group().replace('<p>','----').replace('</p>','\n')
    return strd
def func2(url):
    data = requests.get(url)
    data.encoding = 'UTF-8'
    data = data.text
    s = re.search(r'(http://book.zongheng.com/chapter.*?\d{8}.html).*?下一章',data)
    return s.group(1)
url = ''
while True:
    time.sleep(5)
    if url == '':
        url = url = 'http://book.zongheng.com/chapter/557195/27125898.html'
    data = func(url)
    f = open('a.txt','a+')
    f.write(data)
    url = func2(url)
    print(url)
f.close()



