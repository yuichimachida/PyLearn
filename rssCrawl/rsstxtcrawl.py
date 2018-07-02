#経産省RSSのうち、新着情報のテキストをとってくるプログラム
'''
フォルダ構成は以下の通り。
最初の実行のタイミングでBaseDirectoryの配下にhistoryとTextDataフォルダを作成。
history/history.txtに過去に取得したURLの更新日付とURLを保持。重くなったら対策を考える。
TextDataには実行のタイミングで差分がテキストデータとして追加される。

base directory  - rssTxtCrawl.py
                - histry d         - histry.txt
                - TextData d       - METI_新着_2018xxxxxxx.txt

'''
import os, datetime, sys
import feedparser #RSS(xml)解析
import urllib #URL接続
from bs4 import BeautifulSoup #HTML解析

#実行時刻を取得する（文字列で返す）
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
    titleText = soup.find(id='MainContentsArea') #タイトル
    bodyText = soup.findAll('p') #本文、Soupのリストオブジェクト
    urlAllText = titleText.string + '\n' #戻り値用のテキストにタイトルを書き込む
    for i in bodyText:
        if i.string is not None:
            urlAllText += str(i.string) + '\n' #Bodyのテキストを順次書き込み
    print(targetUrl + " ...Text extracted.")
    return urlAllText

#URLのリストをもとにText抽出を行い、ファイルに書き込む。ファイル名に実行日を記載。
def writPageTxt(Links):
    basePath = os.path.dirname(os.path.abspath(__file__))
    textPath = basePath + r'/TextData/' + 'METI_新着_' + getDT() + '.txt'
    with open(textPath, mode='w', encoding='utf-8') as file:
        for eachUrl in Links:
            file.write(getPageTxt(eachUrl[1]) + '\n')
    print("All texts are saved at " + textPath)

#Histroyテキストの中の更新日時・URLと今回取得したRSSのURLのリストを突合。
#差分となるURLリストをHistoryに追加し、戻り値にする。
#読み書き同時モードでの開き方がよくわからなかったのでwith Openをrとaで分けて実行。
def checkHistory(DatesLinks):
    basePath = os.path.dirname(os.path.abspath(__file__))
    historyPath = basePath + r'/history/'
    newUrls = [] #戻り値用差分格納リスト
    print("Matching URLs with History...")
    with open(historyPath + 'history.txt', mode='r') as history:
        histories = history.readlines()
        for DL in DatesLinks:
                DateUrlStr = DL[0] + ', ' + DL[1] + '\n'
                if not DateUrlStr in histories:
                        newUrls.append(DL)
    with open(historyPath + 'history.txt', mode='a') as addhistory:
        for newUrl in newUrls:
                addhistory.writelines(newUrl[0]+ ', ' + newUrl[1] +'\n')
    print(str(len(newUrls)) + " URLs are updated from latest fetch.")
    return newUrls

#RSSの中の更新日とLinkをリストinリストで取得する
def fetchRssDatesLinks():
    rssUrl = "http://www.meti.go.jp/ml_index_release_atom.xml"
    rssLinks = [] #URL格納用空リスト
    rssDic = feedparser.parse(rssUrl) #feedparserでひとつのRSSを辞書化
    print("Fetching RSS...")
    for entry in rssDic.entries:
        rssLinks.append([entry.updated, entry.link]) #RSSの中の更新日とLinkをリストinリストで追加
    print(str(len(rssLinks)) + " URLs are contained in fetched RSS.")
    return rssLinks

#RSSの取得履歴を保持するためのフォルダとテキストを作成
def folderDeploy():
    basePath = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(basePath + r'/history'):
        os.mkdir(basePath + r'/history')
        print("History folder is created...")
    if not os.path.exists(basePath + r'/history/history.txt'):
        with open(basePath + r'/history/history.txt', mode='w', encoding='utf-8') as histxt:
            histxt.write('This is xml update history list.' + '\n')
        print("History text is created...")
    if not os.path.exists(basePath + r'/TextData'):
        os.mkdir(basePath + r'/TextData')
        print("TextData folder is created...")

#メイン処理
def main():
    print("start...")
    folderDeploy()
    #プログラム動作パス
    urlsinRSS = fetchRssDatesLinks()
    updatedURLs = checkHistory(urlsinRSS)
    if len(updatedURLs) == 0:
            print("No update, see you.")
    else:
            writPageTxt(updatedURLs)

#メインルーチン
if __name__ == '__main__': main()
