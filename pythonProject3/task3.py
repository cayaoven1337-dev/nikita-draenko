ip = input("Введите IP-адрес: ")

parts = ip.split(".")

if len(parts) != 4:
    print("Неправильный IP-адрес")
else:
    correct = True
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            correct = False
            break

    if not correct:
        print("Неправильный IP-адрес")
    else:
        first = int(parts[0])

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