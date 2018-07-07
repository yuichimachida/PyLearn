import random
def get_answer(answer_number):
    if answer_number == 1:
        return 'Exactly'
    elif answer_number == 2:
        return 'Quit Sure'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Not sure, try again'
    elif answer_number == 5:
        return 'Try again later'
    elif answer_number == 6:
        return 'Ask again concentrate'
    elif answer_number == 7:
        return 'My answer is No'
    elif answer_number == 8:
        return 'It\' not so good'
    elif answer_number == 8:
        return 'Very Doubtful'

#r = random.randint(1, 9)
#fortune = get_answer(r)
#print(fortune)

print(get_answer(random.randint(1,9)))
