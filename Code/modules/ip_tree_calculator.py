import random
import ip_calculator as ipc
import json


class IP_tree_Calculator:
    subnets = {
        4096: [[0, None], [1, None]],

        2048: [[0, None], [1, None]],

        1024: [[0, None], [1, None]],

        512: [[0, None], [1, None]],

        256: [[0, None], [1, None]],

        128: [[0, None], [1, None]],

        64: [[0, None], [1, None]],

        32: [[0, None], [1, None]],

        16: [[0, None], [1, None]],

        8: [[0, None], [1, None]],

        4: [[0, None], [1, None]]
    }

    def __init__(self):
        self.nodes = None

        self.degrees = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4]  # [2 ** x for x in range(12, 1, -1)]
        self.max_of_nodes = [4094, 2046, 1022, 510, 254, 126, 62, 30, 14, 6, 2]  # [x - 2 for x in self.degrees]

    def node_input(self):
        self.nodes = input().split(', ')
        try:
            self.nodes = list(map(int, self.nodes))
        except ValueError:
            return 'Invalid input: non-int type detected;\nPlease try again'
        else:
            self.nodes = list(map(int, self.nodes))

        self.nodes.sort()
        unic_nodes = list(set(self.nodes))

        dict_nodes = {}

        for node in self.nodes:
            for i in range(len(self.degrees)):
                if (node <= self.max_of_nodes[i]) and (node >= self.max_of_nodes[i+1]):
                    if self.degrees[i] not in dict_nodes.keys():
                        dict_nodes[self.degrees[i]] = [node]
                    else:
                        dict_nodes[self.degrees[i]].append(node)
                    break

        nodes_sum = sum(self.nodes)
        for number in self.max_of_nodes:
            if number >= nodes_sum:
                max_node = number
                break

        if (nodes_sum := sum(self.nodes)) > (correct_sum := (4094 - 2 * len(unic_nodes))):
            return (f"Invalid input: nodes sum "
                    f"({nodes_sum if nodes_sum <= 99999 else str(nodes_sum)[:5]+'...'}) > "
                    f"{correct_sum};\nPlease try again")

        return dict_nodes, max_node

    def main(self):
        print(self.node_input())


# c1 = ipc.IP_Calculator()
if __name__ == "__main__":
    ip_tree_1 = IP_tree_Calculator()
    ip_tree_1.main()
