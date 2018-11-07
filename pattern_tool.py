#!/usr/bin/python3

# Credit to www.phillips321.co.uk for the inspiration for this script who in turn credits the Metasploit tool pattern_create.rb

import argparse

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

def pattern_create(length):
    pattern = ''
    a = 0
    b = 0
    c = 0
    while len(pattern) < length:
        pattern += upper[a] + lower[b] + numbers[c]
        c += 1
        if c == len(numbers):
            c = 0
            b += 1
        if b == len(lower):
            b = 0
            a += 1
        if a == len(upper):
            a = 0
    print(pattern[:length])
    print('Length: %i' % length)
    return pattern

def pattern_find(pattern):
    eip = input('Enter EIP address: ')
    ascii_eip = bytes.fromhex(eip).decode('ascii')
    print('EIP in ASCII: ' + ascii_eip)
    user_input = input('Is this Windows/ little endian? y/n: ')
    if user_input == 'n':
        to_locate = ascii_eip
        print('Big endian pattern to locate: ' + to_locate)
    else:
        to_locate = ascii_eip[::-1]
        print('Little endian pattern to locate: ' + to_locate)
    offset = pattern.find(to_locate)
    print('Offset is located at: ' + str(offset))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', help='Specify the desired number of characters for the pattern')
    args = parser.parse_args()
    length = int(args.length)
    pattern = pattern_create(length)
    pattern_find(pattern)

if __name__ == '__main__':
    main()
