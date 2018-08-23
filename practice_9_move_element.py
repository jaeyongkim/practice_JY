#every day coding test 2018.08.23 [!]
'''
Q : Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.
'''
DUMMY = [
    [0, 5, 0, 3, -1],
    [3, 0, 3]
]

if __name__ == '__main__':
    import copy
    for samples in DUMMY:
            question = copy.copy(samples)
            for i, v in enumerate(samples):
                if v == 0:
                    del samples[i]
                    samples.append(0)
            print("Q: %s , A:%s") % (question, samples)

