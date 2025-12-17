trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
}

for intf, params in trunk.items():
    action = params[0]      # add / del / only
    vlans = params[1:]      # список VLAN

    print("interface FastEthernet " + intf)

    for cmd in trunk_template:
        if cmd.endswith("allowed vlan"):
            if action == "add":
                print(f" {cmd} add {','.join(vlans)}")
            elif action == "del":
                print(f" {cmd} remove {','.join(vlans)}")
            elif action == "only":
                print(f" {cmd} {','.join(vlans)}")
        else:
            print(" " + cmd)