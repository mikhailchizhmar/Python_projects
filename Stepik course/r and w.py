lst = []
with open("dataset_24465_4.txt") as f, open("test.txt", 'w') as w:
    for line in f:
        lst.append(line.rstrip())
    w.write('\n'.join(lst[::-1]))
print(lst)
