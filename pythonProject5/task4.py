# task4.py

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = {}
    for intf, vlans in intf_vlan_mapping.items():
        commands = []
        for cmd in trunk_template:
            if cmd.endswith("allowed vlan"):
                commands.append(f"{cmd} {','.join(str(v) for v in vlans)}")
            else:
                commands.append(cmd)
        result[intf] = commands
    return result


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

print(generate_trunk_config(trunk_config, trunk_mode_template))