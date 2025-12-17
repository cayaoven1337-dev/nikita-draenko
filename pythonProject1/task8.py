ip = "192.168.3.1"
octets = ip.split()
ip_octets = ip.split(".")
bin_octets = [format(int(o), '08b') for o in ip_octets]
print("{:<10}{:<10}{:<10}{:<10}".format(*ip_octets))
print("{:<10}{:<10}{:<10}{:<10}".format(*bin_octets))