#message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#count = {}

#for character in message:
#    count.setdefault(character, 0)
#    count[character] = count[character] + 1

#print(count)

message = '臣安萬侶言。夫、混元既凝、氣象未效。無名無爲。誰知其形。然、乾坤初分、參神作造化之首、陰陽斯開、二靈爲群品之祖。所以、出入幽顯、日月彰於洗目、浮沈海水、神祇呈於滌身。故、太素杳冥、因本教而識孕土産嶋之時、元始綿bak[之繞貌]、頼先聖而察生神立人之世。寔知、懸鏡吐珠、而百王相續、喫劔切蛇、以萬神蕃息歟。議安河而平天下、論小濱而清國土。是以、番仁岐命、初降于高千嶺、神倭天皇、經歴于秋津嶋、化熊出川、天劔獲於高倉、生尾遮徑、大烏導於吉野。列[イ舞]攘賊、聞歌伏仇。即覺夢而敬神祇。所以、稱賢后。望烟而撫黎元。於今傳聖帝。定境開邦、制于近淡海、正姓撰氏、勒于遠飛鳥。雖歩驟各異、文質不同、莫不稽古以繩風猷於既頽、照今以補典教於欲絶。'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

import pprint

pprint.pprint(count)

# message is valiable to keep Kojiki
# count is void dictionary

# "for character is message", repeat below 
