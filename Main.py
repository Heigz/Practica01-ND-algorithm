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

    if u in G.neighbors(v) and contador < k:
        print(u + "->" + v)
        if nodos_rand_unicos[0] in G.neighbors(u):
            u = v
            if (
                existe_trajectoria(G, u, v, k, nodos_rand_unicos, contador)
                and contador < k
            ):
                return True
        else:
            return False

    if u == v and contador < k:
        print("contador " + str(contador))
        print("hola")
        return True

    for neighbor in G.neighbors(u):

        neighbor = str(neighbor)
        if neighbor in nodos_rand_unicos:
            contador += 1
            u = neighbor
            if len(nodos_rand_unicos) > 1:
                nodos_rand_unicos.remove(neighbor)
                print(u)
            else:
                existe_trajectoria(G, u, neighbor, k, nodos_rand_unicos, contador)
                return True

            if (
                existe_trajectoria(G, neighbor, v, k, nodos_rand_unicos, contador)
                and contador < k
            ):

                return True


if __name__ == "__main__":

    # Inicializamos grafica con el archivo grafica.txt
    G = inicializar_grafica("grafica.txt")

    # ///////////////////////////////////////////////////////// Fase adivinatoria
    nodos_rand = agarrar_nodos_al_azar(G.number_of_nodes())
    nodos_rand_unicos = eliminar_duplicados(nodos_rand)
    # /////////////////////////////////////////////////////////
    print(
        "Seleccione 2 nodos uv, ademas un entero positivo k el cual indique el peso de la trayectoria"
    )
    u = str(input("Ingrese en nodo u:"))
    v = str(input("Ingrese en nodo v:"))
    k = input("Ingrese el entero positivo k:")

    if u in nodos_rand_unicos:
        nodos_rand_unicos.remove(u)
    if v in nodos_rand_unicos:
        nodos_rand_unicos.remove(v)

    print(str(nodos_rand_unicos))
    # ///////////////////////////////////////////////////////// Fase de verificación
    if existe_trajectoria(G, u, v, 8, nodos_rand_unicos, 0):
        print("Existe una trayectoria de u a v con peso menor a " + str(k))
    else:
        print("No existe una trayectoria de u a v con peso menor a " + str(k))
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
