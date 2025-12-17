# task6.py

def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}

    with open(config_filename) as f:
        for line in f:
            line = line.strip()

            if line.startswith("interface"):
                intf = line.split()[1]
                vlan_access_mode = False

            if "switchport mode access" in line:
                vlan_access_mode = True
                access[intf] = 1

            if "switchport access vlan" in line:
                access[intf] = int(line.split()[-1])

            if "switchport trunk allowed vlan" in line:
                vlans = [int(v) for v in line.split()[-1].split(",")]
                trunk[intf] = vlans

    return access, trunk


print(get_int_vlan_map("config_sw2.txt"))