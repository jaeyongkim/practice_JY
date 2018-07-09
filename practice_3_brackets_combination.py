#every day coding test 2018.07.02 [!]
'''
Q : Given an integer N, find the number of possible balanced parentheses with N opening and closing brackets.
'''

import copy

# DUMMY = [1, 2, 3, 4, 5, 6, 10]
DUMMY = [1, 2, 3]
G_list = []
G_Question = None

def combination_rule(past_list):
    '''
     1. just condition check.
       1. exit condition.
       2. can be add 1
       3. can be add 2
       4. can be add both.
        1. 1 > 2
            both
        2. 1 == 2
            only 1
    '''
    if past_list.count(1) == G_Question:
        if past_list.count(2) == G_Question:
            G_list.append(map(lambda x: '(' if x==1 else ')', past_list))
            return
        else:
            past_list.append(2)
            combination_rule(past_list)
    else:
        if past_list.count(2) == G_Question:
            past_list.append(1)
            combination_rule(past_list)
        else:
            cron_list = copy.copy(past_list)
            if past_list.count(1) > past_list.count(2):
                cron_list.append(2)
                combination_rule(cron_list)
            past_list.append(1)
            combination_rule(past_list)

if __name__ == '__main__':
    for sample in DUMMY:
        G_list = []
        G_Question = sample
        combination_rule([1])
        print ('%s --> %s --> %s') % (G_Question, G_list, len(G_list))