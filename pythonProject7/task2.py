def convert_ranges_to_ip_list(ip_ranges):
    result = []

    for item in ip_ranges:
        if "-" not in item:
            result.append(item)
        else:
            start, end = item.split("-")

            if "." in end:
                start_parts = start.split(".")
                end_parts = end.split(".")
                start_last = int(start_parts[-1])
                end_last = int(end_parts[-1])
                base = ".".join(start_parts[:-1])
            else:
                start_parts = start.split(".")
                start_last = int(start_parts[-1])
                end_last = int(end)
                base = ".".join(start_parts[:-1])

            for i in range(start_last, end_last + 1):
                result.append(f"{base}.{i}")

    return result


if __name__ == "__main__":
    ips = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
    print(convert_ranges_to_ip_list(ips))