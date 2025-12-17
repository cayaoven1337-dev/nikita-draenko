mac = "AAAA:BBBB:CCCC"
mac = mac.replace(":", "")
binary = bin(int(mac, 16))[2:]
print(binary)