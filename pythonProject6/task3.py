from task2 import create_network_map
from draw_network_graph import draw_topology


def unique_network_map(topology_dict):
    unique = {}

    for local, remote in topology_dict.items():
        if (remote, local) not in unique:
            unique[local] = remote

    return unique


if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    topology = create_network_map(infiles)
    topology = unique_network_map(topology)

    draw_topology(topology)