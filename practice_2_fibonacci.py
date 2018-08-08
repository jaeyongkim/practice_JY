#every day coding test 2018.07.02 [!]
'''
Q : Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers.
Given an integer N, find the sum of all even fibonacci numbers.
'''

DUMMY = [81, 12, 5, 3, 90000, 6869]


if __name__ == '__main__':
    for sample in DUMMY:
        base_list = [0, 1]
        sum = 0
        while (True):
            new_one = base_list[-1] + base_list[-2]
            if new_one < sample:
                base_list.append(new_one)
                if new_one % 2 == 0:
                    sum = sum + new_one
            else:
                print(" input value : %s\n fibonacci list : %s\n even sum : %s\n\n") % (sample, base_list, sum)
                break
