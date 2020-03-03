from urllib import request,parse                                # urllib 网络需要使用的模块  python3 urllib urllib2 urllib3 requests                                          # 配置文件
import chardet,re,requests                               # chardet 检测网页的字符集（有时候不准）
import logging                                                  # 日志模块
import os,sys
class spider():                                                 # spider 爬虫框架
    def __init__(self,word):
        self.word = word                                        # 要爬取的图片的关键字
        self.url = f'https://image.baidu.com/search/index?tn=baiduimage&'         # 定义基础url
        logging.basicConfig(filename=f'message.log', level=logging.INFO, format='%(asctime)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')        # 日志模块，定义日志的内容模板
    def urld(self):
        word = self.word
        word = {
            "word": word
        }
        self.word = parse.urlencode(word)                        # 使用 parse 将关键字进行编码
        self.url = self.url + self.word                          # 基础url  和关键字进行拼接
        return self.url
    def data(self,path):                                         # 定义爬取的功能函数
        if not os.path.exists(path):                             # 判断路径是否存在 如果不，打印日志 退出程序
            self.logd('路径无法找到，请检查')
            sys.exit(3)
        rsps = request.urlopen(self.url)                         # 打开rul（访问url）
        if rsps.getcode() == 200:                                # 判断返回的状态码是什么
            html = rsps.read()                                   # 获取html代码
            code = chardet.detect(html)                          # 检测字符集
            html = html.decode(code.get('encoding', 'utf-8'))    # 解码过程
            data = re.findall(r'http[s]://.*?\.jpg', html)       # 使用正则匹配网页内的图片信息
            data = list(set(data))                               # 去重
            n = 1
            path = path+os.sep
            print(path)
            for i in data:
                d = requests.get(i).content                          # 读取图片内容，将内容写到文件中，以二进制的方式
                f = open(f'{path}{n}.jpg', 'wb')
                self.logd(f'url{n}:ok--{i}')
                print('正在爬取。。。')
                print(f'url{n}:ok--{i}')
                f.write(d)
                f.close()
                n += 1
        else:
            self.logd('访问错误，请检查网络是否连接')
            #sys.exit(4)

    def logd(self,log, level='error'):
        if level == 'error':
            logging.error(log)
        else:
            logging.critical(log)

if __name__ == '__main__':
    path='/Users/mac/Desktop/a/'
    a = spider('美女')
    a.urld()
    a.data(path=path)