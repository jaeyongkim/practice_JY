#every day coding test 2018.08.16 [!]
'''
Q : Given an integer array, find the second largest element.
'''
DUMMY = [
    [10, 5, 4, 3, -1],
    [3, 3, 3]
]

if __name__ == '__main__':
    import copy
    for samples in DUMMY:
            question = copy.copy(samples)
            top_thing = reduce(lambda a, b: a if a > b else b, samples)
            samples.pop(samples.index(top_thing))
            seconds_thing = reduce(lambda a, b: a if a > b else b, samples)
            answer = seconds_thing if not top_thing is seconds_thing else 'Does not exist.'
            print ('Q: %s , A: %s') % (question, answer)

