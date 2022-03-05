import random


def get_random():
    with open('data/quests_answers/answers.txt') as f:
        list_of_ans = f.readlines()
    rand_numb = random.randint(0, len(list_of_ans) - 1)

    return rand_numb, int(list_of_ans[rand_numb])
