import requests,re
'''
思路：获取网页的前端页面，通过正则方法获取到页面中的静态资源地址，下载地址。
'''
first_url = "http://www.xiaohuar.com/2014.html"  # 定义url
reponse = requests.get(first_url)      # 获取网页对象
reponse.encoding = 'GBK'  # 定义编码方式
html = reponse.text   # 获取html 代码
img_urls = re.findall(r'src="(/d/file/\w+\.jpg)"', html)  #正则匹配图片地址
img_num = len(img_urls)
for i in range(img_num):  # 拼接url
    img_urls[i] = "http://www.xiaohuar.com%s" % img_urls[i]

for img_url in img_urls:  # 下载图片并保存
    img_file_name = img_url.split('/')[-1]
    img_data = requests.get(img_url).content
    with open(img_file_name, "wb") as f:
        f.write(img_data)
    print(img_url)