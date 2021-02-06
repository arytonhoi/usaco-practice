"""
ID: aryton.1
LANG: PYTHON3
TASK: beads
"""
# O(n) time - only iterate through string once
# O(n) space - for the double string
if __name__ == '__main__':
    with open('beads.in', 'r') as fin:
        num_beads = int(fin.readline().strip())
        beads = fin.readline().strip()

    beads += beads
    max_sum = 0
    i = j = k = 0

    while k < len(beads):
        streak1 = beads[i]
        if i == 0:
            # first pass, extend j
            while (j - i < num_beads) and (beads[j] == streak1 or beads[j] == 'w'):
                j += 1
                if beads[j] != streak1 and streak1 == 'w':
                    streak1 = beads[j]
            if j - i >= num_beads:
                # j has fully wrapped back to i
                max_sum = num_beads
                break
        elif beads[i-1] == 'w':
            # backtrack
            while i > 0 and beads[i-1] == 'w':
                i -= 1

        streak2 = beads[j]  # streak2 will never be 'w'
        k = j
        while k < len(beads) and (k - i < num_beads) and (beads[k] == 'w' or beads[k] == streak2):
            k += 1

        max_sum = max(max_sum, k - i)
        if k - i >= num_beads:
            break
        i = j
        j = k

    # print(sums)

    with open('beads.out', 'w') as fout:
        fout.write(f"{max_sum}\n")
