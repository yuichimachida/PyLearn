import MeCab
import zipfile
import sys
import os.path, urllib.request as req

# Download zip file
url = "https://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
if not os.path.exists(local):
    print("Zip Download")
    req.urlretrieve(url, local)

# Read Text in zip
zf = zipfile.ZipFile(local, 'r') #Read Zipfile
fp = zf.open('gingatetsudono_yoru.txt', 'r') #Read text in Archeive
bindata = fp.read() #
txt = bindata.decode('shift_jis') #Shift_jis decode

# Object
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

# Txt analysis 1 line by 1 line
word_dic = {}
lines = txt.split("/r/n")
for line in range(100):
    node = mecab.parseToNode(txt) #このへんからよくわからん
    while node:
        word = node.surface
        print(word)
        '''
        ps = node.feature #品詞
        if ps.find('名詞-一般') < 0:
            node = node.next #名詞でなければ次のwhile
        if word in word_dic:
            word_dic[word] += 1 #word_dicにカウント
        else:
            word_dic[word] = 1'''
        node = node.next
        '''

#　よく使われる単語を表示
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word,cnt in keys[:50]:
    print("{0}({1}) ".format(word,cnt), end="")

'''
