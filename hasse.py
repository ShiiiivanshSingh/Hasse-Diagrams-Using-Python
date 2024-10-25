import networkx as nx
import matplotlib.pyplot as plt


H_new = nx.DiGraph()

# Power set for S = {a, b, c}
power_set_new = ['∅', '{a}', '{b}', '{c}', '{a, b}', '{a, c}', '{b, c}', '{a, b, c}']


hasse_edges_new = [('∅', '{a}'), ('∅', '{b}'), ('∅', '{c}'), 
                   ('{a}', '{a, b}'), ('{a}', '{a, c}'), 
                   ('{b}', '{a, b}'), ('{b}', '{b, c}'), 
                   ('{c}', '{a, c}'), ('{c}', '{b, c}'), 
                   ('{a, b}', '{a, b, c}'), ('{a, c}', '{a, b, c}'), ('{b, c}', '{a, b, c}')]

H_new.add_edges_from(hasse_edges_new)


plt.figure(figsize=(8, 8))
pos_new = nx.spring_layout(H_new) 
nx.draw(H_new, pos_new, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', arrows=False)


nx.draw_networkx_edge_labels(H_new, pos_new)


plt.title("Hasse Diagram for P(S, ⊆) with S = {a, b, c}", fontsize=14)
plt.show()
