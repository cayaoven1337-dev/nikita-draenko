ip = input("Введите IP-адрес: ")

first = int(ip.split(".")[0])

if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= first <= 223:
    print("unicast")
elif 224 <= first <= 239:
    print("multicast")
else:
    print("unused")