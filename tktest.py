#!/usr/bin/env python3
#-*-coding: utf-8-*-

from tkinter import *
from a import *
def test():
    var= entry1.get()
    path = entry2.get()
    b = spider(var)
    b.urld()
    b.data(path=path)
# 构造窗口
root = Tk()
root.title('python爬虫')
Label(root, text='关键字|路径\n').pack()
entry1 = Entry(root,width=20)
entry2 = Entry(root,width=20)
but = Button(root,text='确认',command=test)
# 添加元素
entry1.pack()
entry2.pack()
but.pack()
# 循环运行
root.mainloop()


