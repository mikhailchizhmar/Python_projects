import sys


def main():
    rows = []
    output = False
    for line in sys.stdin:
        line = line.rstrip()
        if len(line) != 5:
            raise ValueError
        rows.append(line)
    if len(rows) != 3:
        raise ValueError
    if (rows[0][0] == '*' and rows[0][1:4].find('*') == -1 and rows[0][4] == '*'
        and rows[1][0:2] == '**' and rows[1][2] != '*' and rows[1][3:] == '**'
        and rows[2][0::2] == '***' and rows[2][1] != '*' and rows[2][3] != '*'):
        output = True
    return output


if __name__ == '__main__':
    try:
        print(main())
    except ValueError:
        print("Error")
