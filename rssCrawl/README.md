# 経産省RSSから、新着情報のテキストをとってくるプログラム

フォルダ構成はとりあえず以下の通り。
basePath  - (rssTxtCrawl.py)
          - d MetiText    - d histry                  - histry.txt
                          - METI_新着_2018xxxxxxx.txt

実行のタイミングでMetiText、history, history.txtが存在しなければそれぞれを作成。

RSSのデータはfeedparserで取得。更新日とURLで過去に取得した履歴（history.txt）と突合。
突合結果に応じてMetiTextフォルダには差分のテキストデータが追加される。
テキストが書き込まれたらhistory.txtに更新日付とURLを追加書き込み。

なお、上記実行前にhistory.txtから古い履歴を削除する処理が走る。履歴の保持はとりあえず14日で設定。
history.txtの履歴は手動で削除もできるが、余計な改行などが入るとエラーになるので注意。

HPからのテキスト抽出Beautifulsoupは、<h>系と<p>タグのほか、<ul>タグを抽出する。
本文の一部を構成している場合もあるためだが、末尾のリンク集なども取れてしまうので、
<ul>が不要ならばbeautifulsoupのfind_allの取得対象リストから<ul>タグを削除。

## TODO
環境に応じてbasePathを設定できるようにグローバル変数で代入一回だけにしている。
フォルダ構成が違う形になるようなら、そのときに他のPath変数（historyPathなど）もグローバル変数に修正したほうがいいかも。

保存先も.iniに入れて、FileNotFoundError
