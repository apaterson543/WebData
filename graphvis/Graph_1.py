import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

color = ["#1f78b4"] * 34
color[0] = "red"
color[33] = "green"

for i in range(len(G.nodes)):
    if i != 0 and i != 33:
        if G.nodes[i]["club"] == 'Mr. Hi':
            color[i] = "#ffcccb"
        else:
            color[i] = "#90ee90"

nx.draw_kamada_kawai(G, with_labels=True, node_color=color)
plt.savefig('Graphs/before_split.png')
plt.show()
