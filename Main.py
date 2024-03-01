import networkx as nx
import matplotlib.pyplot as plt


def inicializar_grafica(nombre_archivo):
    G = nx.Graph()
    grafica_entrada = open(nombre_archivo, "r")
    nodos = grafica_entrada.readline()

    # Incluir los nodos en la grafica
    for x in range(len(nodos)):
        if x % 2 == 0:
            G.add_node(nodos[x])

    # Incluir aristas en las grafica
    aristas = grafica_entrada.readlines()
    for x in range(len(aristas)):
        G.add_edge(str(aristas[x][0]), str(aristas[x][0 + 2]))
    grafica_entrada.close()
    return G


if __name__ == "__main__":
    G = inicializar_grafica("grafica.txt")
    print(G.edges.__len__.__sizeof__)
    # G = nx.Graph()
    # G.add_node("A")
    # G.add_node("B")
    # G.add_node("C")
    # G.add_node("D")
    # nx.draw(
    #     G,
    #     with_labels=True,
    #     # node_color="red",
    #     # font_weight="bold",
    #     font_family="serif",
    #     # font_size=20,
    #     # node_size=2000,
    # )

    nx.draw(G, node_color="r", edge_color="b")
    plt.margins(0.1)
    plt.show()
