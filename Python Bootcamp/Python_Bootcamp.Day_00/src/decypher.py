import sys

sentence = ''
try:
    sentence = sys.argv[1].split()
    output = ''
    for word in sentence:
        output += word[0]
    print(output)
except IndexError:
    print("One argument is required!")
