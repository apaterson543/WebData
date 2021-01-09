import matplotlib.pyplot as plt
import networkx as nx


def find_max_betweenness(G):
    max = 0
    max_e = None

    f = nx.edge_betweenness_centrality(G, k=None, normalized=True, weight=None, seed=None)
    for edge in f:
            if max < f[edge]:
                max = f[edge]
                max_e = edge

    max_edge = list(max_e)
    return max_edge

def girmin_newman(iteration_num, G):
    for i in range(iteration_num):
        max_between = find_max_betweenness(G)
        G.remove_edge(max_between[0], max_between[1])
    return None

def color_nodes():
    color = ["#1f78b4"] * 34
    color[0] = "red"
    color[33] = "green"
    for i in range(len(G.nodes)):
        if i != 0 and i != 33:
            if G.nodes[i]["club"] == 'Mr. Hi':
                color[i] = "#ffcccb"
            else:
                color[i] = "#90ee90"

    return color


if __name__=="__main__":
    value = ''
    iterate = 0
    while value != 'e':
        G = nx.karate_club_graph()
        girmin_newman(iterate, G)
        color = color_nodes()
        iterations = str(iterate) + " iterations"
        ax = plt.gca()
        ax.set_title(iterations)
        nx.draw_kamada_kawai(G, with_labels=True, node_color=color, ax=ax)
        plt.savefig('Graphs/after_' + iterations)
        plt.show()

        value = input("Enter + to increase iterations or - to decease: ")
        if value == '+':
            iterate += 1
        if value == '-':
            iterate -= 1
