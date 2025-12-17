config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = config.split()[-1]
result = vlans.split(",")
print(result)