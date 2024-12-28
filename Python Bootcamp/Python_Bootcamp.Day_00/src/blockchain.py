import sys

exit_flag = True
n_lines = 0
try:
    n_lines = int(sys.argv[1])
    if n_lines < 0:
        raise ValueError
    exit_flag = False
except IndexError:
    print("One argument is required!")
except ValueError:
    print("The argument must be a positive integer!")

if not exit_flag:
    count = 0
    for line in sys.stdin:
        if count >= n_lines:
            break
        line = line.rstrip()
        cond = line.startswith('00000') and line[5] != '0' and len(line) == 32
        if cond:
            print(line)
            count += 1
