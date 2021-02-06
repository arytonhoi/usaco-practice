"""
ID: aryton.1
LANG: PYTHON3
TASK: friday
"""
if __name__ == '__main__':
    with open('friday.in', 'r') as fin:
        num_years = int(fin.readline().strip())

    # 1 = Monday
    # Start on Jan 1, 1900
    start_year = 1900
    current_weekday = 1

    count = [0 for _ in range(7)]

    for i in range(num_years):
        current_year = start_year + i
        current_month = 1
        current_day = 1
        is_leap_year = False

        # check leap year
        if current_year % 4 == 0:
            if current_year % 100 != 0:
                is_leap_year = True
            elif current_year % 100 == 0 and current_year % 400 == 0:
                is_leap_year = True

        # 30 days: 9-sept, 4-apr, 6-june, 11-nov
        # 31 days rest except
        # 28 days feb except 29 on leap year
        while not (current_month == 12 and current_day == 31):
            if current_day == 13:
                count[current_weekday - 1] += 1

            next_month = False
            if ((
                current_month == 9
                or current_month == 4
                or current_month == 6
                or current_month == 11
            )
                and current_day == 30
            ):
                next_month = True
            elif is_leap_year and current_month == 2 and current_day == 29:
                next_month = True
            elif not is_leap_year and current_month == 2 and current_day == 28:
                next_month = True
            elif current_day == 31:
                next_month = True

            if next_month:
                current_month = ((current_month) % 12) + 1
                current_day = 1
            else:
                current_day += 1

            current_weekday = ((current_weekday) % 7) + 1
        current_weekday = ((current_weekday) % 7) + 1

    with open('friday.out', 'w') as fout:
        # rotate counts from starting on monday to start on saturday
        count = count[5:] + count[:5]
        fout.write(f"{' '.join(map(str, count))}\n")
