import networkx as nx
import matplotlib.pyplot as plt

# Создание пустого графа
G = nx.Graph()

# Добавление узлов в граф
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# Добавление ребер в граф
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

# Отрисовка графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold')

# Отображение графика
plt.show()
