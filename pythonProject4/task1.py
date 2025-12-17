with open("ospf.txt") as f:
    for line in f:
        line = line.strip().replace(",", "")
        parts = line.split()

        prefix = parts[0]
        metric = parts[1]
        nexthop = parts[3]
        update = parts[4]
        interface = parts[5]

        print(f"Prefix               {prefix}")
        print(f"AD/Metric           {metric}")
        print(f"Next-Hop            {nexthop}")
        print(f"Last update         {update}")
        print(f"Outbound Interface  {interface}\n")