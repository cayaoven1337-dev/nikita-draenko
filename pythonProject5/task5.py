# task5.py

def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}

    with open(config_filename) as f:
        for line in f:
            line = line.strip()

            if line.startswith("interface"):
                intf = line.split()[1]

            if "switchport access vlan" in line:
                vlan = int(line.split()[-1])
                access[intf] = vlan

            if "switchport trunk allowed vlan" in line:
                vlans = [int(v) for v in line.split()[-1].split(",")]
                trunk[intf] = vlans

    return access, trunk


print(get_int_vlan_map("config_sw1.txt"))