from multiply import mul

x1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y1 = [[1,2],[1,2],[3,4]]

print(mul(x1, y1))

x2 = [[1,2,3],[4,5,6],[7,8,9],[10,11.5,12]]
y2 = [[1,2],[1,2],[3,4]]
try:
    print(mul(x2, y2))
except TypeError as e:
    print(e)

x3 = [[1,2],[4,5],[7,8],[10,11]]
y3 = [[1,2],[1,2],[3,4]]
try:
    print(mul(x3, y3))
except ValueError as e:
    print(e)