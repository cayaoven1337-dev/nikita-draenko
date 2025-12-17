from tabulate import tabulate


def print_ip_table(reachable, unreachable):
    table = []

    max_len = max(len(reachable), len(unreachable))

    for i in range(max_len):
        r = reachable[i] if i < len(reachable) else ""
        u = unreachable[i] if i < len(unreachable) else ""
        table.append([r, u])

    print(tabulate(table, headers=["Reachable", "Unreachable"]))


if __name__ == "__main__":
    good = ["8.8.8.8", "1.1.1.1"]
    bad = ["10.255.255.1", "192.0.2.1"]
    print_ip_table(good, bad)