# every day coding test 2018.07.30 [!]
'''
Q : Given a list of intervals, merge intersecting intervals.
'''

DUMMY = [
    [[2, 4], [1, 5], [7, 9]],
    [[3, 6], [1, 3], [2, 4]]
]

def get_merged_result(lists):
    front_num = None
    result_list = []
    for i, v in enumerate(lists):
        if front_num == None:
            front_num = v
        elif lists[i-1]+1 != v:
            result_list.append([front_num, lists[i-1]])
            front_num = v
        elif i+1 == len(lists):
            result_list.append([front_num, v])
    return result_list

if __name__ == '__main__':
    for sample in DUMMY:
        sets = set()
        for list_v in sample:
            sets |= set(range(list_v[0], list_v[1]+1))
        print ('Q list = %s, A list = %s ') % (sample, get_merged_result(list(sets)))