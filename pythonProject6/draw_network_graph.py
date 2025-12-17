from graphviz import Graph


def draw_topology(topology_dict, filename="topology"):
    """
    Функция принимает словарь топологии и рисует схему в формате svg.
    topology_dict:
    {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ...
    }
    """

    graph = Graph(format="svg")
    graph.attr(rankdir="LR")

    for local, remote in topology_dict.items():
        local_device, local_intf = local
        remote_device, remote_intf = remote

        graph.edge(
            f"{local_device}\n{local_intf}",
            f"{remote_device}\n{remote_intf}"
        )

    graph.render(filename, view=False)