from typing import Any

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model":"4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
device = input("Vvedite name ustroistva: ")
params = ",".join(london_co[device].keys())
parameter = input(f"Vvedite name parametra ({params}) :").lower()
print(london_co[device].get(parameter, "takogo parametra net"))

ip_input = input("Введите IP-сеть (например 10.1.1.0/24): ")

if "/" not in ip_input:
    print("Ошибка: введите сеть в формате IP/MASK, например 10.1.1.0/24")
    exit()

ip, mask = ip_input.split("/")
mask = int(mask)

octets = ip.split(".")
if len(octets) != 4 or not all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
    print("Ошибка: некорректный IP-адрес")
    exit()

bin_ip = " ".join("{:08b}".format(int(o)) for o in octets)

mask_bin = "1" * mask + "0" * (32 - mask)

mask_octets = [
    int(mask_bin[0:8], 2),
    int(mask_bin[8:16], 2),
    int(mask_bin[16:24], 2),
    int(mask_bin[24:32], 2)
]

print("\nNetwork:")
print("\t".join(octets))
print(bin_ip)

print("\nMask:")
print(f"/{mask}")
print("\t".join(map(str, mask_octets)))
print(" ".join("{:08b}".format(o) for o in mask_octets))

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

mode = input("Введите режим (access/trunk): ")
iface = input("Введите интерфейс: ")

questions = {
    "access": "Введите номер VLAN: ",
    "trunk": "Введите разрешенные VLANы: "
}

vlans = input(questions[mode])

templates = {
    "access": access_template,
    "trunk": trunk_template
}

print(f"interface {iface}")
for line in templates[mode]:
    print(line.format(vlans))