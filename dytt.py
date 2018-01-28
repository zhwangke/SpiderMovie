# -*- coding:utf-8 -*-
# Author: Wang Ke
# Version : 3.6
"""
功能：获取IMDB热门电影的迅雷下载链接

"""
import urllib
from urllib import request
import re
from bs4 import BeautifulSoup
import time

def getUrl(url):
    """
    Step1：获取当前排行电影详情页的Html

    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk','ignore')
    #print(html)

    """
    bs4同样可以获取到电影的详情页：
    soup = BeautifulSoup(html,'lxml')
    links = soup.find('div',class_="co_content8")
    for link in links.findAll('a', class_= "ulink"):
        fullurl = 'http://www.ygdy8.net'+link['href']
        print(fullurl)
    """
    pattern = re.compile('<table.*?>.*?<b>.*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</b>.*?</table>',re.S)
    links = re.findall(pattern,html)
    print('正在获取第{}页的链接，请稍等！'.format(i))
    for link in links:
        fullurl = 'http://www.ygdy8.net'+link[0]
        name = link[1]
        ftpUrl(fullurl,name)
        time.sleep(1)
    print('第{}页链接获取完成!'.format(i)+'\n')

def ftpUrl(fullurl,name):
    """
    Step2:清洗数据，取出各个电影的真实下载地址

    """
    request = urllib.request.Request(fullurl)
    response = urllib.request.urlopen(request)
    f_html = response.read().decode('gbk','ignore')
    #print(f_html)

    pattern = re.compile('<td style="WORD-WRAP.*?><a href="(.*?)">.*?</td>')
    f_links = re.findall(pattern,f_html)
    #print(f_links)

    list_url = [name] + f_links
    print(list_url)
def writeFile():
    """
    Step3:把链接存储到本地保存为Json格式

    """
    filename = 'IMDB.txt'
    with open(filename,'w') as f:
        f.write(list_url)


if __name__ == '__main__':
    for i in range(1,12):
        url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
        getUrl(url)


