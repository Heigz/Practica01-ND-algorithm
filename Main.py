import random
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


def eliminar_duplicados(arr):
    # convertir la lista a un conjunto para remover duplicados
    unique_set = set(arr)

    # Crear una lista del conjunto único
    numeros_unicos = list(unique_set)

    return numeros_unicos


def agarrar_nodos_al_azar(numero_nodos):
    nodos_random = []
    for x in range(random.randint(2, numero_nodos)):
        nodos_random.append(random.randint(1, numero_nodos))
    return nodos_random


def existe_trajectoria(G, u, v, k, nodos_rand_unicos, contador):
    if u == v and contador < k:
        return True

    for neighbor in G.neighbors(u):
        if neighbor in nodos_rand_unicos:
            contador += 1
            u = neighbor
            return existe_trajectoria(G, neighbor, v, k, nodos_rand_unicos, contador)


if __name__ == "__main__":

    # Inicializamos grafica con el archivo grafica.txt
    G = inicializar_grafica("grafica.txt")

    # ///////////////////////////////////////////////////////// Fase adivinatoria
    nodos_rand = agarrar_nodos_al_azar(G.number_of_nodes())
    nodos_rand_unicos = eliminar_duplicados(nodos_rand)
    # /////////////////////////////////////////////////////////
    # print(
    #     "Seleccione 2 nodos uv, ademas un entero positivo k el cual indique el peso de la trayectoria"
    # )
    # u = int(input("Ingrese en nodo u:"))
    # v = int(input("Ingrese en nodo v:"))
    # k = input("Ingrese el entero positivo k:")

    if 7 in nodos_rand_unicos:
        nodos_rand_unicos.remove(7)
    if 3 in nodos_rand_unicos:
        nodos_rand_unicos.remove(3)

    # print("antes: " + str(nodos_rand_unicos))
    # ///////////////////////////////////////////////////////// Fase de verificación
    if existe_trajectoria(G, "7", "3", 8, [6, 4, 5, 2], 0):
        print("Existe una trayectoria de u a v con peso menor a " + str(8))
    else:
        print("No existe una trayectoria de u a v con peso menor a" + str(8))
    # /////////////////////////////////////////////////////////

    # Dibujamos la grafica
    # nx.draw(
    #     G,
    #     with_labels=True,
    #     font_family="serif",
    #     edge_color="b",
    # )
    # plt.margins(0.1)
    # plt.show()
