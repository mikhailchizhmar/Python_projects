import calculator

print(calculator.add(13, 21))
print(calculator.sub(14, 21))
print(calculator.mul(14, 21))
print(calculator.div(14, 7))

try:
    print(calculator.div(14, 0))
except ZeroDivisionError as e:
    print(e)

try:
    print(calculator.div(14.7, 2436.9))
except TypeError as e:
    print(e)