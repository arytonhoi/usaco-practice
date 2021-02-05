"""
ID: aryton.1
LANG: PYTHON3
TASK: ride
"""
if __name__ == '__main__':
    with open('ride.in', 'r') as fin:
        comet = fin.readline().strip()
        group = fin.readline().strip()

    prod1, prod2 = 1, 1
    for c in comet:
        prod1 *= ord(c) - ord('A') + 1
    for c in group:
        prod2 *= ord(c) - ord('A') + 1

    with open('ride.out', 'w') as fout:
        if prod1 % 47 == prod2 % 47:
            fout.write("GO\n")
        else:
            fout.write("STAY\n")
