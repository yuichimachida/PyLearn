while True:
    print('What your name?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is your password?')
    password = input()
    if password == 'swordfish':
          break
print('Certified')
