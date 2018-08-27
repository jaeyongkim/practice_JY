#every day coding test 2018.08.27 [!]
'''
Q : Given a string, find the longest substring that does not have duplicate characters.
'''
DUMMY = [
    "aabcbcbc",
    "aaaaaaaa",
    "abbbcedd",
]

if __name__ == '__main__':
    for samples in DUMMY:
        longest_str = current_str = str()
        for c in samples:
            if c in current_str:
                current_str = current_str + c if not current_str[-1] is c else c
            else:
                current_str += c
                longest_str = current_str if current_str > longest_str else longest_str
        print("Q: %s , A:%s") % (samples, longest_str)

