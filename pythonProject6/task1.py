def parse_cdp_neighbors(command_output):
    result = {}
    lines = command_output.splitlines()

    local_device = lines[0].split(">")[0]

    for line in lines:
        parts = line.split()
        if len(parts) >= 5 and parts[1][0].isalpha():
            remote_device = parts[0]
            local_intf = parts[1] + parts[2]
            remote_intf = parts[-2] + parts[-1]

            result[(local_device, local_intf)] = (remote_device, remote_intf)

    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))