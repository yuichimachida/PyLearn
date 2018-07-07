import sys

while True:
    print('To exit, input Exit')
    response = input()
    if response == 'Exit':
        sys.exit()
    print(response + ': you input')
