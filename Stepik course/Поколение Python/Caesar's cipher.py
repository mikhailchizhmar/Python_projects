# only for lower case
n = int(input())
s = input()

for c in s:
    if ord(c) - n < 97:
        newc = chr(122 - n + ord(c) - 96)
    else:
        newc = chr(ord(c) - n)
    print(newc, end='')
