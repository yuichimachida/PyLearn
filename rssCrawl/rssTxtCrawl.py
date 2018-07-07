import os, datetime, sys
import configparser #Configfile読み込み
import feedparser #RSS(xml)解析
import urllib #URL接続
from bs4 import BeautifulSoup #HTML解析
import re #正規表現処理

'''
実行日取得関数(文字列)
'''
# ファイル名用と、history.txtへの実行日メモ用に形式を分ける分岐処理を行っている。
def getDT(para):
    now = datetime.datetime.now()
    if para == 'filename':
        dt = "{0:%Y%m%d-%H%M%S}".format(now)
    if para == 'histline':
        dt = "{0:%Y-%m-%d}".format(now)
    return dt

'''
Txtファイル抽出、書き込み系処理
'''
# 各ページのURLをもとにテキスト抽出して返す処理
def extractPageTxt(targetUrl):
    # 記事のHTMLを取得
    htmlData = urllib.request.urlopen(targetUrl).read().decode('utf-8')
    # 解析用のBeautifulSoupオブジェクト
    soup = BeautifulSoup(htmlData,'html.parser')
    # 以下テキスト化処理
    # hタグ、pタグ、ulタグをリストオブジェクトとして取得
    TagTexts = soup.find_all([re.compile('h\d'), 'p', 'ul'])
    retText = ''
    for TagText in TagTexts:
        retText += str(TagText.text) + '\n' #Bodyのテキストを順次書き込み
    print(targetUrl + " ...Text extracted.")
    return retText

# 与えられたURLのリストをもとにText抽出を行い、ファイルに書き込む。
# ファイル名に実行日時が記載されるようにしている。
# 1件の抽出が終わったらhistoryに書き込む。
def writPageTxt(Links):
    textPath = basePath + r'/MetiText/' + 'METI_新着_' + getDT('filename') + '.txt'
    with open(textPath, mode='w', encoding='utf-8') as file:
        for eachUrl in Links:
            file.write(extractPageTxt(eachUrl[1]) + '\n\n')
            writeHistory(eachUrl)
    print("All texts are saved at " + textPath)

'''
履歴突合、履歴管理系処理
'''
# history.txtにテキスト抽出したURLの履歴を書き込む処理
def writeHistory(singleUrl):
    historyPath = basePath + r'/MetiText/history/'
    with open(historyPath + 'history.txt', mode='a') as addHistory:
        addHistory.writelines(singleUrl[0]+ ', ' + singleUrl[1] +'\n')

# 実行ごとにhistory.txtに区切り(open/close)を入れる。念のため。
def splitHistory(splitStr):
    historyPath = basePath + r'/MetiText/history/'
    with open(historyPath + 'history.txt', mode='a') as splitHistory:
        splitHistory.writelines(getDT('histline') + ' ' + splitStr +'\n')

# histroy.txtの中の更新日時・URLと今回取得したRSSのURLのリストを突合。
# 差分となるURL(と更新日)のリストを戻り値にする。
def checkHistory(DatesLinks):
    historyPath = basePath + r'/MetiText/history/'
    newUrls = [] #戻り値用差分格納リスト
    print("Matching URLs with History...")
    with open(historyPath + 'history.txt', mode='r') as history:
        histories = history.readlines()
        for DL in DatesLinks:
                DateUrlStr = DL[0] + ', ' + DL[1] + '\n'
                if not DateUrlStr in histories:
                        newUrls.append(DL)
    print(str(len(newUrls)) + " URLs are updated from latest fetch.")
    return newUrls

# history.txtに履歴が貯まりすぎていたら削除する。とりあえず14日としている。
# 現在のhistoryをcurrentHistoryとしてリスト化して、行の先頭の日付を実行日日付と突合する。
# 設定した日数未満なら、行をrefleshに退避してhistory.txtに全上書きする。
# もうすこしスマートなやり方があったかもしれないので改善できるならしたい。
def clearHistory():
    today = datetime.datetime.today()
    refleshHistories = []
    historyPath = basePath + r'/MetiText/history/'
    with open(historyPath + 'history.txt', mode='r') as history:
        currentHistories = history.readlines()
        for h in currentHistories:
            hisDate = datetime.datetime.strptime(h[:10], '%Y-%m-%d') #historyの行先頭から日付取得。
            dateDelta = today - hisDate
            if dateDelta.days >= 14:
                continue #refleshHistoriesへのappendなしに破棄
            else:
                refleshHistories.append(h) #if文の日数より新しければrefleshHistoriesに退避
    print('Old ' + str(len(currentHistories)-len(refleshHistories)) + ' lines are deleted from history.')
    with open(historyPath + 'history.txt', mode='w') as newHistory:
        for ref in refleshHistories:
            newHistory.writelines(ref)

'''
RSSから更新日とURLを取ってくる処理
'''
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

'''
メイン系
'''
#データを保存するフォルダを作成。
def folderDeploy():
    if not os.path.exists(basePath + r'/MetiText'):
        os.mkdir(basePath + r'/MetiText')
        print("MetiText folder is created...")
    if not os.path.exists(basePath + r'/MetiText/history'):
        os.mkdir(basePath + r'/MetiText/history')
        print("History folder is created...")
    if not os.path.exists(basePath + r'/MetiText/history/history.txt'):
        with open(basePath + r'/MetiText/history/history.txt', mode='w', encoding='utf-8'):
            pass
        print("History text is created...")

def loadConfig()
    config = configparser.ConfigParser
    config.read('./config.ini', 'UTF-8')



#メイン処理
def main():
    loadConfig()
    global basePath
    basePath = os.path.dirname(os.path.abspath(__file__)) #プログラム動作パス！グローバル変数！
    print("start...")
    folderDeploy() #動作に必要なフォルダを作る
    clearHistory() #履歴が古ければ消しちゃう
    urlsinRSS = fetchRssDatesLinks() #RSSからURLとかをとってきて
    updatedURLs = checkHistory(urlsinRSS) #history.txtと突合して差分を残す
    if len(updatedURLs) == 0:
            print("No update, see you.") #差分がなければ終了
    else:
            splitHistory('...Open...')
            writPageTxt(updatedURLs) #差分があれば履歴に実行日を記録しながらページの情報をtxt化
            splitHistory('...Close...')

#メインルーチン
if __name__ == '__main__': main()
