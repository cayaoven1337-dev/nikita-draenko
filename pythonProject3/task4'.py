while True:
    ip = input("Введите IP-адрес: ")
    parts = ip.split(".")

    if len(parts) == 4:
        correct = True
        for p in parts:
            if not p.isdigit() or not 0 <= int(p) <= 255:
                correct = False
                break
        if correct:
            break

    print("Неправильный IP-адрес")

# После выхода из цикла IP корректный:
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