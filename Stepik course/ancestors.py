ancestors_descendants = {}


def add_descendants():
    for k in ancestors_descendants:
        for elem in ancestors_descendants[k]:
            if elem in ancestors_descendants.keys():
                ancestors_descendants[k].extend(ancestors_descendants[elem])


def input_letters(k):
    for i in range(k):
        s = input().split()
        for j in range(2, len(s)):
            if s[j] not in ancestors_descendants.keys():
                ancestors_descendants[s[j]] = []

        for j in range(2, len(s)):
            ancestors_descendants[s[j]].append(s[0])
    add_descendants()


def output_letters(k):
    for i in range(k):
        flag = "No"
        s = input().split()
        if s[0] == s[1] and s[0] not in ancestors_descendants.items():
            print("Yes")
            continue
        if s[0] not in ancestors_descendants.keys():
            flag = "No"
        elif s[0] == s[1] or s[1] in ancestors_descendants[s[0]]:
            flag = "Yes"
        print(flag)


n = int(input())
input_letters(n)

q = int(input())
output_letters(q)
for k in ancestors_descendants:
    print(k, "->", ancestors_descendants[k])

print(ancestors_descendants)
