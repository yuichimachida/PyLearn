import pyperclip, re

# Phone Regex
phoneRegex = re.compile(r'''(   #TODO 正規表現は後で見直す
    (\d{1,3}|\(\d{1,3}\))?  #市外局番
    (\s|-)?                 #区切り
    (\d{2,4})               #市内
    (\s|-)                  #区切り
    (\d{4})                 #番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #内線番号
    )''', re.VERBOSE)

# Mail Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy
