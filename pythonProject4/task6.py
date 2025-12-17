entries = []

with open("CAM_table.txt") as f:
    for line in f:
        if "." in line:
            parts = line.split()
            vlan = int(parts[0])
            mac = parts[1]
            intf = parts[3]
            entries.append([vlan, mac, intf])

for vlan, mac, intf in sorted(entries):
    print(vlan, mac, intf)