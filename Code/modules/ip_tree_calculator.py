import random
import ip_calculator as ipc
import json


class IP_tree_Calculator:
    """ IP tree calculator"""

    def __init__(self):
        self.nodes = None
        self.dict_nodes = {}

        self.degrees = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4]  # [2 ** x for x in range(12, 1, -1)]
        self.max_of_nodes = [4094, 2046, 1022, 510, 254, 126, 62, 30, 14, 6, 2]  # [x - 2 for x in self.degrees]

        # максимальное число возможных узлов в подсети
        self.max_amount_of_nodes = {4096: 1, 2048: 2, 1024: 4, 512: 8, 256: 16, 128: 32, 64: 64, 32: 128, 16: 256,
                                    8: 512, 4: 1024}

    def node_input(self):
        self.nodes = input().split(', ')  # ввод узлов через запятую

        # проверка есть ли в вводе пользователя числа
        # True -> self.nodes = [int, int, ...]
        # False -> return 'Error'
        try:
            self.nodes = list(map(int, self.nodes))
        except ValueError:
            return 'Invalid input: non-int type detected;\nPlease try again'
        else:
            self.nodes = list(map(int, self.nodes))

        self.nodes.sort()  # сортировка узлов по возрастанию

        # проверка есть ли узлы меньше 2
        # True -> return 'Error'
        # False -> OK
        invalid_nodes = []
        for node in self.nodes:
            if node < 2:
                invalid_nodes.append(node)
        if invalid_nodes:
            return f'Node(s) {invalid_nodes} < 2;\nPlease try again'
        else:
            del invalid_nodes

        dict_nodes = {}  # словарь для узлов

        # распределение узлов по подсетям
        # -> dict_nodes: ключ - подсеть, значение - список узлов
        # словарь на выходе может содержать избыточное число узлов, проверка на валидность расположена ниже
        for node in self.nodes:
            for i in range(len(self.degrees)):
                if (node <= self.max_of_nodes[i]) and (node > self.max_of_nodes[i+1]):
                    if self.degrees[i] not in dict_nodes.keys():
                        dict_nodes[self.degrees[i]] = [node]
                    else:
                        dict_nodes[self.degrees[i]].append(node)
                    break

        # проверка на отсутствие узлов в словаре
        # True -> return 'Error'
        # False -> OK
        if dict_nodes == {}:
            return f'Nodes ({self.nodes}) > 4094;\nPlease try again'

        # проверка на наличие узлов, которые не были добавлены в словарь
        # True -> return 'Error'
        # False -> OK
        dict_nodes_list = []
        [dict_nodes_list.extend(x) for x in list(dict_nodes.values())]
        if len(self.nodes) > len(dict_nodes_list):
            return f'Node(s) {set(self.nodes) - set(dict_nodes_list)} > 4094;\nPlease try again'

        # сумма введенных узлов
        nodes_sum = sum(self.nodes)

        # максимально возможная сумма узлов
        correct_sum = 4096 - (self.max_amount_of_nodes.get((min(list(dict_nodes.keys())))) * 2)

        # проверка суммы узлов
        # True -> return 'Error'
        # False -> OK
        if nodes_sum > correct_sum:
            return f'Nodes sum ({nodes_sum}) > {correct_sum};\nPlease try again'

        # поиск максимальной подсети для дерева
        max_subnet = 0
        for number in reversed(self.degrees):
            if number-2 >= nodes_sum:
                max_subnet = number
                break
        if max_subnet == 0:
            return f'Nodes sum ({nodes_sum:e}) > {self.max_of_nodes[0]};\nPlease try again'

        # Минимальная подсеть в дереве
        min_subnet = min(list(dict_nodes.keys()))

        self.dict_nodes = dict_nodes
        return dict_nodes, max_subnet, min_subnet, correct_sum, nodes_sum

    def tree_constructor(self, dict_nodes, max_subnet, min_subnet):

        tree = {}

        return tree

    def node_distribution(self):
        pass

    def main(self):
        out = self.node_input()
        flag = False
        # если вернется tuple, то его элементы выведутся через строку
        if type(out) is tuple:

            print((out[0]), '',  # json.dumps(out[0], indent=2)
                  f'Максимальная подсеть в дереве: {out[1]}',
                  f'Минимальная подсеть в дереве: {out[2]}',
                  f'Максимальная сумма всех узлов: {out[3]}',
                  f'Текущая сумма узлов: {out[4]}',
                  *out[5:], sep='\n', end=f'\n{79 * "-"}\n')
            flag = True
        else:
            print(out)

        if flag:
            tree_func_out = self.tree_constructor(out[0:1], out[1:2], out[2:3])
            print(tree_func_out, '', sep='\n')


# c1 = ipc.IP_Calculator()
if __name__ == "__main__":
    ip_tree_1 = IP_tree_Calculator()
    ip_tree_1.main()
