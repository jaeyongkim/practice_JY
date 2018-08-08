#every day coding test 2018.07.16 [!]
'''
Q : Given an integer, check if it is a palindrome.
'''


DUMMY = [1233441, 1234321, -1111, 1234, 9223372036854775800, 1112223333333222111]

# def checker_max_int():
#     import sys
#     print (sys.maxint)

def digit_check(n):
    import math
    return int(math.log10(n)) + 1

def is_palindrome(input, digit):
    '''
     If I can use str, it will be so simple :)
     -------> input[::-1]
        
     1. negative check
     2. digit check using max int size. -> 9223372036854775807
        -> too much.
            -> so I was searched int digit check in google.
                -> I found this
                    -> digits = int(math.log10(n))+1
     3. compare during downsizing check_index and multiply, division, subtract
     4. determination increasing check index based on even and odd.
    '''
    count = 1
    while True:
        front_value = (input/10**(digit-count))-(input/10**(digit-count+1))*10
        back_value = (input/10**(count-1))-(input/10**count)*10
        if front_value != back_value:
            return False
        if digit % 2 == 0 and count*2 == digit:
            return True
        elif digit % 2 == 1 and count*2+1 == digit:
            return True
        count += 1

if __name__ == '__main__':
    for sample in DUMMY:
        # validation check about negative num.
        checker = False if sample < 0 else is_palindrome(sample, digit_check(sample))
        print ('%d is palindrome -> %s') % (sample, checker)
