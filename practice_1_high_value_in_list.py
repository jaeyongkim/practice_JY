#every day coding test 2018.06.30 [!]
'''
Q : Given an integer array, find the largest consecutive sum of elements.
'''

DUMMY = [
    [-1, 3, -1, 5],
    [-5, -3, 1],
    [2, 3, -2, -3, 8],
    [2, 0, 1, 3, 5, -2],
    [100, 2, -900, 22, 33, 0],
    [100, 2, -900, 22, 33, 0, 2, 0, 1, 3, 5, -2, 2, 3, -2, -3, 8, -5, -3, 1]
]

def queue_three_sum(list, newone):
    list.pop(0)
    list.append(newone)
    return list, list[0]+list[1]+list[2]

if __name__ == '__main__':
    for samples in DUMMY:
        top = None
        result = 0
        list = [0, 0, 0]
        for i, v in enumerate(samples):
            list, current = queue_three_sum(list, v)
            if (top is None or current > top) and (i > 1):
                top = current
        print ('in %s answer is %s') % (samples, top)
