from task1 import parse_cdp_neighbors


def create_network_map(filenames):
    topology = {}

    for filename in filenames:
        with open(filename) as f:
            output = f.read()
            topology.update(parse_cdp_neighbors(output))

    return topology


if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    print(create_network_map(infiles))