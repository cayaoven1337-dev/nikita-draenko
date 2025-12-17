with open("CAM_table.txt") as f:
    for line in f:
        if "." in line:  # строка с MAC адресом
            parts = line.split()
            vlan = parts[0]
            mac = parts[1]
            intf = parts[3]
            print(vlan, mac, intf)