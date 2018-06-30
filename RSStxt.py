import os, datetime, sys
import feedperser
import urllib
from bs4 import BeautifulSoup

#これは動いた
#RSS単位でディクショナリをテキストに書き込む
def rssTxt(rssDictionary):
    path = '/tempp/rssTextTest.txt'
    with open(path, mode='w', encoding='utf-8') as file:
        for entry in rssDictionary.entries:
            file.write(str(entry))

#未確認
#urlからテキスト化？
def getPageTxt(targetUrl):
    htmlData =
    urllib.request.urlopen(targetUrl).read().decode('utf-8')
    #解析用のBeautifulSoupオブジェクト
    soup = BeautifulSoup(htmlData, 'html')
    #テキスト化
    allText = soup.findAll('p', attrs={'class' : 'ymDetailText'})

#
