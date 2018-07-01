#経産省RSSのうち、新着情報のテキストをとってくる処理
'''
フォルダ構成は以下の通り、BaseDirectoryの配下にhistoryとTextDataを作ってください。
base directory  -
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
        titleText = soup.find(id='MainContentsArea') #タイトル, このidで全部うまくいくのか不明
        bodyText = soup.findAll('p') #本文、Soupのリストオブジェクト
        urlAllText = titleText.string + '\n' #戻り値用のテキストにタイトルを書き込む
        for i in bodyText:
                if i.string is not None:
                        urlAllText += str(i.string) + '\n' #Bodyのテキストを順次書き込み
        print(targetUrl + " Text extracted.")
        return urlAllText

#URLのリストをもとにTextに書き込みに行く処理（テキスト抽出はgetPageTxt()）
def writPageTxt(Links):
    textPath = savePath + 'METI_新着_' + getDT() + '.txt'
    with open(textPath, mode='w', encoding='utf-8') as file:
        for eachUrl in Links:
            file.write(getPageTxt(eachUrl[1]) + '\n')
    print("Saved at " + textPath)

#RSSの中のLinkとUpdateをリストinリストで取得する
def getRssLinks():
    rssUrl = "http://www.meti.go.jp/ml_index_release_atom.xml"
    rssLinks = [] #URL格納用空リスト
    rssDic = feedparser.parse(rssUrl) #feedparserでひとつのRSSを辞書化
    for entry in rssDic.entries:
        rssLinks.append([entry.updated, entry.link]) #RSSの中のLinkをリストに追加

    print("URL lists are corrected.\nURLs are")
    for i in rssLinks:
        print(i[0]+', '+i[1])
    return rssLinks #リストを返す

#Historyテキストがなければ作成
def createHistory():
    pathExist = False
    if os.path.exists(historyPath):
        if not os.path.exists(historyPath + 'history.txt'):
            with open(historyPath + 'history.txt', mode='w', encoding='utf-8') as file:
                file.write('This is xml update history list.' + '\n')
            print('History text is created.')
            pathExist = True
        else:
                print('History text is found.')
                pathExist = True
    else:
        print('''
        Create directories as below
        base directory  - rssTxtCrawl.py
		        - histry d         - histry.txt
                        - TextData d       - METI_
                        ''')
    return pathExist

#Histroyテキストの中のUpodateとURLのリストを突合する
def checkHistory(urls):
    newUrls = []
    with open(historyPath + 'history.txt', mode='r') as f:
        lines = f.readlines()
        for url in urls:
                print(url[1])
                checkDateUrl = url[0] + ', ' + url[1] + '\n'
                if checkDateUrl in lines:
                        print('True, ' + url[1] + ' is exist.')
                else:
                        print('Else, ' + url[1] + ' is appended.')
                        newUrls.append(url)
    with open(historyPath + 'history.txt', mode='a') as add:
        for newUrl in newUrls:
                add.writelines(newUrl[0]+ ', ' + newUrl[1] +'\n')
    return newUrls

#プログラム動作パス
#任意のパスの場合
#basePath = 'ここにパスを書く'
basePath = os.path.dirname(os.path.abspath(__file__)) #デフォルトはこの.pyの実行フォルダ
historyPath = basePath + r'/history/'
savePath = basePath + r'/TextData/'

#メイン処理
if createHistory():
    urlList = getRssLinks()
    print("Historyと突合中...")
    updatedURL = checkHistory(urlList)
    if len(updatedURL) == 0:
            print('新着情報はありません')
    else:
            writPageTxt(updatedURL)
    print('Done.')
else:
    print('履歴ファイルを保持するフォルダを作成してください。')
