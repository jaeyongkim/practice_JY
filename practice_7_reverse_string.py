# every day coding test 2018.08.08 [!]
'''
Q : Reverse all the words in the given string.
'''

DUMMY = [
   "abc 123 apple",
   "my name is jaeyong kim hello"
]


if __name__ == '__main__':
    for string_set in DUMMY:
        str_list = string_set.split(' ')
        result_list = list(map(lambda i: i[::-1] , str_list))
        print ("Q: %s\n A: %s") % (str_list, result_list)