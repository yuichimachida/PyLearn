#経産省RSSのうち、新着情報のテキストをとってくる処理
#BeautifulSoupの解析の仕方が悪いので、MetiJournalのURLだと動かないけど、MetiJournalっているんだっけ。

#TODO
#実行時間で新規ファイル作ってとってくるだけなので、前回取得からの差分取得に修正する必要あり。


import os, datetime, sys
import feedparser #RSS(xml)解析
import urllib #URL接続
from bs4 import BeautifulSoup #HTML解析

#実行時刻を取得する
def getDT():
        now = datetime.datetime.now()
        dt = "{0:%Y%m%d-%H%M%S}".format(now)
        return dt

#各ページのURLをもとにテキストを返す処理
def getPageTxt(targetUrl):
        # 記事のHTMLを取得
        htmlData = urllib.request.urlopen(targetUrl).read().decode('utf-8')
        # 解析用のBeautifulSoupオブジェクト
        soup = BeautifulSoup(htmlData,'html.parser')
        # 以下テキスト化処理
        title = soup.find(id='MainContentsArea') #タイトル, このidで全部うまくいくのか不明
        bodyText = soup.findAll('p') #本文、Soupのリストオブジェクト
        plainText = title.string + '\n' #戻り値用のテキストにタイトルを書き込む
        for i in bodyText:
                if i.string is not None:
                        plainText += str(i.string) + '\n' #Bodyのテキストを順次書き込み
        print(targetUrl + " Text extracted.")
        return plainText

#URLのリストをもとにTextに書き込みに行く処理（Soupでのテキスト抽出はgetPageTxt()）
def writPageTxt(Links):
        base = os.path.dirname(os.path.abspath(__file__))
        path = base + '\\' + 'METI_NR_' + getDT() + '.txt'
        with open(path, mode='w', encoding='utf-8') as file:
                for eachUrl in Links:
                        file.write(getPageTxt(eachUrl) + '\n')
        print("Saved at " + path)

#RSSの中のLinkをリストで取得する
def getRssLinks():
    rssUrls = [
        "http://www.meti.go.jp/ml_index_release_atom.xml",
        #「RSSのURLはここに追加」にしようとおもったけど、新着情報しかテキスト化できてないからあまり意味がない
        ]
    rssLinks = [] #URL格納用空リスト
	upDated = [] #??差分取得用のリストでも作ったらどうだろうか。
    for rssUrl in rssUrls:
        rssDic = feedparser.parse(rssUrl) #feedparserでひとつのRSSを辞書化
        for entry in rssDic.entries:
            rssLinks.append(entry.link) #RSSの中のLinkをリストに追加

    print("URL lists are corrected.\nURLs are")
    for i in rssLinks:
            print(i)
    return rssLinks #リストを返す

#メイン処理
urlList = getRssLinks()
print("Text extracting...")
writPageTxt(urlList)
print("Done.")
