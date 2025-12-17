ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
parts = ospf_route.split()
prefix = parts[0]
ad_metric = parts[1].strip("[]")
next_hop = parts[3].strip(",")
last_update = parts[4].strip(",")
interface = parts[5]
print("Prefix")
print(prefix)
print("AD/Metric")
print(ad_metric)
print("Next-Hop")
print(next_hop)
print("Last Update")
print(last_update)
print("Outbound Interface")
print(interface)