#every day coding test 2018.09.07 [!]
'''
Q : Given two strings of equal length, check if two strings can be encrypted 1 to 1.
'''
DUMMY = [
    ("EGG", "FOO"),
    ("ABBCD", "APPLE"),
    ("AAB", "FOO")
]

if __name__ == '__main__':
    for sample in DUMMY:
        maps = dict()
        first_str = sample[0]
        second_str = sample[1]
        checker = True
        for _ in range(len(first_str)):
            holder = maps.get(first_str[_])
            if holder:
                if holder != second_str[_]:
                    checker = False
                    break
            else:
                maps.update({first_str[_]: second_str[_]})
        print("Q: %s , A:%s") % (sample, checker)

