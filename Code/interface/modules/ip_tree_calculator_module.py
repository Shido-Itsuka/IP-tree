import random
import json
from collections import OrderedDict


class IP_Tree_Calculator:
    """ IP tree calculator"""

    def __init__(self, ip, nodes):
        self.nodes = None
        self.dict_nodes = {}

        self.degrees = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4]  # [2 ** x for x in range(12, 1, -1)]
        self.max_of_nodes = [4094, 2046, 1022, 510, 254, 126, 62, 30, 14, 6, 2]  # [x - 2 for x in self.degrees]

        # максимальное число возможных подсетей с распределенными узлами на них в подсети
        self.max_amount_of_nodes = {4096: 1, 2048: 2, 1024: 4, 512: 8, 256: 16, 128: 32, 64: 64, 32: 128, 16: 256,
                                    8: 512, 4: 1024}

        # максимально возможное число узлов на подсети
        self.max_of_nodes_dict = {4096: 4094, 2048: 2046, 1024: 1022, 512: 510, 256: 254, 128: 126, 64: 62, 32: 30,
                                  16: 14, 8: 6, 4: 2}

        # вводимый IP
        self.ip = ip

        # вводимые узлы
        self.nodes = nodes.split('\n')

    def node_input(self):
        # проверка есть ли в вводе пользователя числа
        # True -> self.nodes = [int, int, ...]
        # False -> return 'Error'
        try:
            self.nodes = list(map(int, self.nodes))
        except ValueError:
            raise TypeError('Invalid input: non-int type detected;\nPlease try again|N')
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
            raise ValueError(f'Node(s) {invalid_nodes} < 2;\nPlease try again|N')
        else:
            del invalid_nodes

        dict_nodes = {}  # словарь для узлов

        # распределение узлов по подсетям
        # -> dict_nodes: ключ - подсеть, значение - список узлов
        # словарь на выходе может содержать избыточное число узлов, проверка на валидность расположена ниже
        for node in self.nodes:
            for i in range(len(self.degrees)):
                if node > self.max_of_nodes[-1]:  # Нужно, чтобы избежать ошибки <IndexError: list index out of range>
                    if (node <= self.max_of_nodes[i]) and (node > self.max_of_nodes[i + 1]):
                        if self.degrees[i] not in dict_nodes.keys():
                            dict_nodes[self.degrees[i]] = [node]
                        else:
                            dict_nodes[self.degrees[i]].append(node)
                        break
                else:  # Распределение узлов из диапазона [2:6] по подсети
                    if (node < self.max_of_nodes[-2]) and (node >= self.max_of_nodes[-1]):
                        if self.degrees[-1] not in dict_nodes.keys():
                            dict_nodes[self.degrees[-1]] = [node]
                        else:
                            dict_nodes[self.degrees[-1]].append(node)
                        break

        # проверка на отсутствие узлов в словаре
        # True -> return 'Error'
        # False -> OK
        if dict_nodes == {}:
            raise ValueError(f'Nodes ({self.nodes}) > 4094;\nPlease try again|N')

        dict_nodes = OrderedDict(dict_nodes)

        # проверка на наличие узлов, которые не были добавлены в словарь
        # True -> return 'Error'
        # False -> OK
        dict_nodes_list = []
        [dict_nodes_list.extend(x) for x in list(dict_nodes.values())]
        if len(self.nodes) > len(dict_nodes_list):
            raise ValueError(f'Node(s) {set(self.nodes) - set(dict_nodes_list)} > 4094;\nPlease try again|N')

        # сумма введенных узлов
        nodes_sum = sum(self.nodes)

        # максимально возможная сумма узлов
        # correct_sum = 4096 - (self.max_amount_of_nodes.get((min(list(dict_nodes.keys())))) * 2)

        # проверка на превышение числа возможных подсетей с узлами в родительской подсети
        # True -> return 'Error'
        # False -> OK
        # Example: 1024: [1000, 1000, 1000, 1000, 1000] => True -> return 'Error'
        for k, v in dict_nodes.items():
            if self.max_amount_of_nodes.get(k) < len(v):
                raise ValueError((f'Amount of nodes ({len(v)}) for subnet ({k}) > '
                                  f'Max amount of nodes ({self.max_amount_of_nodes.get(k)}) for subnet ({k});'
                                  f'\nPlease try again'))

        # проверка на превышение максимально возможного числа узлов на подсети
        # True -> return 'Error'
        # False -> OK
        # Example: 1024: [1023] => True -> return 'Error'
        for k, v in dict_nodes.items():
            for i in v:
                if i > self.max_of_nodes_dict.get(k):
                    raise ValueError(f'Node(s) {v} on subnet {k} > {self.max_of_nodes_dict.get(k)};\nPlease try again')

        # !!! ДОЛЖНО БЫТЬ УДАЛЕНО ВСЛЕДСТВИЕ НЕНАДОБНОСТИ !!!
        # проверка суммы узлов
        # True -> return 'Error'
        # False -> OK
        # if nodes_sum > correct_sum:
        #     return f'Nodes sum ({nodes_sum}) > {correct_sum};\nPlease try again'
        # ^______________________________________________________________________^

        # поиск максимальной подсети для дерева
        max_subnet = 0
        for number in reversed(self.degrees):
            if number - 2 >= nodes_sum:
                max_subnet = number
                break
        if max_subnet == 0:
            raise ValueError(f'Nodes sum ({nodes_sum:e}) > {self.max_of_nodes[0]};\nPlease try again')

        # Проверка на количество подсетей в родительской подсети
        # True -> return 'Error'
        # False -> OK
        # Example: 1024: [1022], 2048: [1023, 1023] => True -> return 'Error'
        # Пояснение: Максимальная подсеть - 4096; на обе 2048 подсети распределяются узлы 1023 и 1023
        # остается подсеть 1024 и 1022 узла, которые распределяются на нее. Так как уже заняты обе 2048 подсети,
        # то 1024 существовать в данном случае просто не может => должна выводиться ошибка.
        if len(dict_nodes) > 1:
            reversed_dict = OrderedDict(sorted(dict_nodes.items(), reverse=True))
            keys = list(reversed_dict.keys())
            i = 0
            for i, (k, v) in enumerate(reversed_dict.items()):
                if i + 1 < len(keys):
                    possible_sub_amount = int((1 - (len(v) / self.max_amount_of_nodes.get(k)))
                                              * (self.max_amount_of_nodes.get(keys[i + 1])))
                    print(possible_sub_amount)
                    
                    if possible_sub_amount > 0:
                        if possible_sub_amount < len(reversed_dict.get(keys[i + 1])):
                            raise ValueError(f'Введенное число узлов на подсети "{reversed_dict.get(keys[i + 1])}"'
                                             f' равно "{len(reversed_dict.get(keys[i + 1]))}"'
                                             f', что больше допустимых "{possible_sub_amount}"')
                    else:
                        raise ValueError(f'Введенное число узлов на подсети "{reversed_dict.get(keys[i + 1])}"'
                                         f' равно "{len(reversed_dict.get(keys[i + 1]))}"'
                                         f', что больше допустимых "{possible_sub_amount}"')

        # Минимальная подсеть в дереве
        min_subnet = min(list(dict_nodes.keys()))

        self.dict_nodes = dict_nodes
        return dict_nodes, max_subnet, min_subnet, nodes_sum

    # Рекурсивная функция для создания словаря
    def create_nested_dict(self, subnets, count):
        if count == 0:
            return {}
        next_subnet = subnets[1:]
        nested_dict = {
            subnets[0]: (
                self.create_nested_dict(next_subnet, count - 1),
                self.create_nested_dict(next_subnet, count - 1))
        }

        return nested_dict

    # Создание дерева
    def tree_constructor(self, dict_nodes, max_subnet, min_subnet):
        # [max:min] => [int, int...]; P.S. Example: [4096, 2048, 1024]
        subnets = list(self.degrees[self.degrees.index(max_subnet):self.degrees.index(min_subnet) + 1])

        tree = {
            subnets[0]: (
                self.create_nested_dict(subnets[1:], len(subnets) - 1),
                self.create_nested_dict(subnets[1:], len(subnets) - 1))
        }

        return tree

    # Распределение подсетей по узлам
    def node_distribution(self):
        pass

    def main(self):
        out = self.node_input()

        print(dict(out[0]), '',  # json.dumps(out[0], indent=2)
              f'Максимальная подсеть в дереве:           {out[1]}',
              f'Минимальная подсеть в дереве:            {out[2]}',
              f'Текущая сумма узлов:                     {out[3]}',
              *out[4:], sep='\n', end=f'\n{79 * "-"}\n')

        tree_func_out = self.tree_constructor(*out[0:3])
        print(json.dumps(tree_func_out, indent=4), '', sep='\n')
        return out


# c1 = ipc.IP_Calculator()
if __name__ == "__main__":
    try:
        print(f'\n1) {'-' * 55}')
        ip_tree_1 = IP_Tree_Calculator('192.168.0.1', '1022\n1023\n1023')
        ip_tree_1.main()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    # для тестов:
    try:
        print(f'\n2) {'-' * 55}')
        ip_tree_2 = IP_Tree_Calculator('192.168.0.1', '1022\n510\n510\n510\n510\n510\n510\n510\n510')
        ip_tree_2.main()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        print(f'\n3) {'-' * 55}')
        ip_tree_3 = IP_Tree_Calculator('192.168.0.1', '1022\n1022\n1022\n1022')
        ip_tree_3.main()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        print(f'\n4) {'-' * 55}')
        ip_tree_4 = IP_Tree_Calculator('192.168.0.1', '100\n50\n50\n50\n15\n15\n15\n15\n15')
        ip_tree_4.main()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
