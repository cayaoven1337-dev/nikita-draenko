ignore = ["duplex", "alias", "configuration"]

src = 'config_sw1.txt'
dst = 'result.txt'

with open(src) as f, open(dst, 'w') as out:
    for line in f:
        line = line.rstrip()

        if line.startswith('!'):
            continue

        skip = False
        for word in ignore:
            if word in line:
                skip = True
                break

        if not skip and line:
            out.write(line + '\n')