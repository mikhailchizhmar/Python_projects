x = [1, 2, 3]
y = x
y.append(666)
print(x, y)

s = "wipducpe"
t = s
t += "1234567890"
print(s, t)

z = True

def h():
    global z
    z = False

h()
print(z)


class M:
    pass


x = M()
x.count = 0
x.count += 5
print(x.count)