import collections

my_graph = [
    (7, "A", "B"),
    (5, "A", "D"),
    (7, "B", "A"),
    (8, "B", "C"),
    (9, "B", "D"),
    (7, "B", "E"),
    (8, "C", "B"),
    (5, "C", "E"),
    (5, "D", "A"),
    (9, "D", "B"),
    (7, "D", "E"),
    (6, "D", "F"),
    (7, "E", "B"),
    (5, "E", "C"),
    (7, "E", "D"),
    (8, "E", "F"),
    (9, "E", "G"),
    (6, "F", "D"),
    (8, "F", "E"),
    (11, "F", "G"),
    (9, "G", "E"),
    (11, "G", "F"),
]
node_list = sorted(list(set([item[1] for item in my_graph])))


def remove_duplicated_node(graph: list) -> list:
    num_list = []
    cleand_graph = []
    for node in graph:
        num = ord(node[1]) + ord(node[2])
        if not num in num_list:
            num_list.append(num)
            cleand_graph.append(node)
    return sorted(cleand_graph, key=lambda x: x[0])


cleaned_graph = remove_duplicated_node(graph)