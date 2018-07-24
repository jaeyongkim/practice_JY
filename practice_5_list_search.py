# every day coding test 2018.07.24 [!]
'''
Q : Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.
'''

DUMMY = [(8, [2, 5, 6, 1, 10]), (3, [1, 9, 3, 2, 0])]



if __name__ == '__main__':
    for sample in DUMMY:
        result_list = []
        pair_dict = {}
        for i, v in enumerate(sample[1]):
            if not v > sample[0]:
                if v in pair_dict:
                    result_list.append((pair_dict[v], i))
                else:
                    pair_dict.update({(sample[0]-v):i})
        print ("search V : %d, list : %s, resulst : %s") % (sample[0], sample[1], result_list)

