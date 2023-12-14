import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_children(parent, level, max_level):
    if level == max_level:
        return

    for i in range(2):
        child_value = parent.value * 2 + i + 1
        child = Node(child_value)
        parent.children.append(child)
        add_children(child, level+1, max_level)

def draw_tree(root):
    fig, ax = plt.subplots()
    ax.set_xlim([0, max_level + 1])
    ax.set_ylim([0, 2 ** (max_level + 1)])
    ax.axis('off')

    plot_tree(ax, root, 0, 2 ** max_level, 2 ** (max_level - 1))

    plt.show()

def plot_tree(ax, node, x, y, dy):
    ax.text(x, y, str(node.value), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    if len(node.children) == 0:
        return

    child_dy = dy / len(node.children)
    y_start = y - dy / 2
    y_pos = y_start + child_dy / 2

    for child in node.children:
        ax.plot([x, x+1], [y, y_pos], 'k-')
        plot_tree(ax, child, x+1, y_pos, child_dy)
        y_pos += child_dy

# Создаем корневой узел
root = Node(1)

# Задаем максимальную глубину дерева
max_level = 5

# Добавляем потомков
add_children(root, 0, max_level)

# Отрисовываем дерево
draw_tree(root)