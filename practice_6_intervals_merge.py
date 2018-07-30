# every day coding test 2018.07.30 [!]
'''
Q : Given a list of intervals, merge intersecting intervals.
'''

DUMMY = [
    [[2, 4], [1, 5], [7, 9]],
    [[3, 6], [1, 3], [2, 4]]
]

def get_merged_result(sets):
    result_list = []
    target_list = []
    for v in sets:
        if len(target_list) == 0:
            target_list = [v, v]
        else:
            if target_list[-1]+1 == v:
                target_list[-1] = v
                if sets[-1] == v:
                    result_list.append(target_list)
            else:
                result_list.append(target_list)
                target_list = [v, v]
    return result_list

if __name__ == '__main__':
    for sample in DUMMY:
        sets = set()
        for list_v in sample:
            sets |= set(range(list_v[0], list_v[1]+1))
        print ('Q list = %s, A list = %s ') % (sample, get_merged_result(list(sets)))