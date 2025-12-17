import sys

ignore = ["duplex", "alias", "configuration"]
filename = "config_sw1.txt"

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("!") or line == "":
            continue

        skip = False
        for word in ignore:
            if word in line:
                skip = True
                break

        if not skip:
            print(line)