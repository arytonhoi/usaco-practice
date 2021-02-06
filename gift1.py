"""
ID: aryton.1
LANG: PYTHON3
TASK: gift1
"""
if __name__ == '__main__':
    with open('gift1.in', 'r') as fin:
        num_people = int(fin.readline().strip())
        people = {}
        for i in range(num_people):
            people[fin.readline().strip()] = {}

        for i in range(num_people):
            name = fin.readline().strip()
            money, num_friends = map(int, fin.readline().split())

            person = people[name]
            person["money"] = money
            person["num_friends"] = num_friends
            person["friends"] = []
            for j in range(num_friends):
                person["friends"].append(fin.readline().strip())

        money = {name: 0 for name, _ in people.items()}
        for name in people.keys():
            person = people[name]

            if person["num_friends"] == 0:
                money[name] += person["money"]
                continue

            amount_give = person["money"] // person["num_friends"]
            amount_keep = person["money"] % person["num_friends"]
            money[name] -= person["money"] - amount_keep
            for friend in person["friends"]:
                money[friend] += amount_give

    with open('gift1.out', 'w') as fout:
        for name, amount in money.items():
            fout.write(f"{name} {amount}\n")
