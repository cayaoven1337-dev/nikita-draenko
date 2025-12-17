import sys

filename = "config_sw1.txt"

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if not line.startswith("!") and line != "":
            print(line)