import subprocess


def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []

    for ip in ip_list:
        result = subprocess.run(
            ["ping", "-c", "1", "-n", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    ips = ["8.8.8.8", "1.1.1.1", "10.255.255.1"]
    good, bad = ping_ip_addresses(ips)

    print("Доступные:", good)
    print("Недоступные:", bad)