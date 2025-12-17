ip_input = input("Введите IP-сеть (например 10.1.1.0/24): ")

ip, mask = ip_input.split("/")
mask = int(mask)

octets = ip.split(".")
bin_ip = "{:08b}{:08b}{:08b}{:08b}".format(*map(int, octets))

mask_bin = "1" * mask + "0" * (32 - mask)
mask_octets = [
    int(mask_bin[0:8], 2),
    int(mask_bin[8:16], 2),
    int(mask_bin[16:24], 2),
    int(mask_bin[24:32], 2)
]

print("Network:")
print("\t".join(octets))
print(" ".join([bin(int(o)) for o in octets]).replace("0b", "").zfill(8))

print("\nMask:")
print("/" + str(mask))
print("\t".join(map(str, mask_octets)))
print(" ".join("{:08b}".format(o) for o in mask_octets))