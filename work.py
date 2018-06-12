#total = 0
#for num in range(101):
#    total = total + num
#    print(str(num) + '  ' + str(total))
#print('fin ' + str(num) +' ' + str(total))

#print('How many numbers?')
#num = int(input())
#num = round((num + 1)*num/2)
#print(num)

#for i in range(100, 1, -1):
#    print(i)

#import random
#for i in range(10):
#    print(random.randint(1,10))

while True:
    spam = input()
    if spam == '1':
        print('Hello')
    elif spam == '2':
        print('Howdy')
    elif spam == 'END':
        break
    else:
        print('Greetings!')
