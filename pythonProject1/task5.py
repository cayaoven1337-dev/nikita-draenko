command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vl1 = command1.split()[-1].split(",")
vl2 = command2.split()[-1].split(",")
result = sorted(list(set(vl1) & set(vl2)))
print(result)