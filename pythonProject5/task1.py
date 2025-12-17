# task1.py

def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for intf, vlan in intf_vlan_mapping.items():
        result.append(f"interface {intf}")
        for cmd in access_template:
            if cmd.endswith("access vlan"):
                result.append(f"{cmd} {vlan}")
            else:
                result.append(cmd)
    return result


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

print(generate_access_config(access_config, access_mode_template))