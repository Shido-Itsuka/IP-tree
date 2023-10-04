import random
import ip_calculator as ipc


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

        self.degrees = [2 ** x for x in range(12, 1, -1)]

    def node_input(self):
        nodes = input().split(', ')
        try:
            nodes = list(map(int, nodes))
        except ValueError:
            raise ValueError(f'Invalid input: {nodes}')

        nodes.sort()

        for i in range(len(nodes)):
            if nodes[i] > self.degrees[i] - 2:
                raise ValueError(f"Node {nodes[i]} is out of range")

    def main(self):
        self.node_input()


# c1 = ipc.IP_Calculator()
if __name__ == "__main__":
    ip_tree_1 = IP_tree_Calculator()
    ip_tree_1.main()
