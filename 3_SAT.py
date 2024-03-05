import random
import re


def inicializar_3_SAT(nombre_archivo):
    """Inicializa el 3-SAT con el archivo de texto que contiene la expresión"""
    sat_entrada = open(nombre_archivo, "r")
    tres_sat = sat_entrada.readline()
    return tres_sat


def sacar_literales(expresion):
    """Saca los literales de la expresión 3-SAT"""
    pattern = "([a-zA-Z])"
    matches = re.findall(pattern, expresion)
    return matches


def remover_duplicados(literales):
    """Remueve los literales duplicados de la lista de literales de la expresión 3-SAT"""
    # convertir la lista a un conjunto para remover duplicados
    unique_set = set(literales)

    # Crear una lista del conjunto único
    numeros_unicos = list(unique_set)
    return numeros_unicos


def asignacion_aleatoria(literales):
    """Asigna valores aleatorios a los literales"""
    asignacion = {}
    for literal in literales:
        asignacion[literal] = random.randint(0, 1)
    return asignacion


def convertir_complementos(expresion, literales, valores):
    """Convierte los complementos de los literales en la expresión 3-SAT"""
    for literal in literales:
        pattern = "(-" + literal + ")"
        if valores[literal] == 0:
            expresion = re.sub(pattern, "1", expresion)
        else:
            expresion = re.sub(pattern, "0", expresion)
    return expresion


def convertir_normales(expresion, literales, valores):
    """Convierte los literales en la expresión 3-SAT"""
    for literal in literales:
        pattern = literal
        if valores[literal] == 0:
            expresion = re.sub(pattern, "0", expresion)
        else:
            expresion = re.sub(pattern, "1", expresion)
    return expresion


def convertir_expresion(expresion, literales, valores):
    """Convierte la expresión 3-SAT con los valores de los literales"""
    expresion = convertir_complementos(expresion, literales, valores)
    expresion = convertir_normales(expresion, literales, valores)
    return expresion


def contador(expresion):
    """Cuenta el número de paréntesis en la expresión 3-SAT"""
    k = 0
    for parentesis in expresion:
        if parentesis == "(":
            k += 1
    return k


def separar_expresion(expresion):
    """Separa la expresión 3-SAT en cláusulas"""
    pattern = r"\([^()]+\)"
    matches = re.findall(pattern, expresion)
    return matches


def evaluar_sat(expresion):
    """Evalúa la expresión 3-SAT"""
    k = contador(expresion)
    clausulas = separar_expresion(expresion)
    for i in range(k):
        clausula = clausulas[i]
        if "1" not in clausula:
            return False
    return True


def respuesta(booleano):
    """Devuelve la respuesta de la satisfacibilidad de la expresión 3-SAT"""
    if booleano:
        return "Satisfacible"
    else:
        return "No satisfacible"


if __name__ == "__main__":

    tres_sat_crudo = inicializar_3_SAT("3_SAT.txt")
    literales = remover_duplicados(sacar_literales(tres_sat_crudo))
    print("original:   " + tres_sat_crudo)
    print("\n")

    print("literales:  " + str(literales))
    print("\n")

    # ////////////////////////////////////////////////////////////////Fase adivinatoria
    valores = asignacion_aleatoria(literales)
    # ////////////////////////////////////////////////////////////////

    print("valores:    " + str(valores))
    print("\n")

    # ////////////////////////////////////////////////////////////////Fase de verificación
    tres_sat = convertir_expresion(tres_sat_crudo, literales, valores)
    print("expresion:" + str(tres_sat))
    print("\n")

    satisfacible = evaluar_sat(tres_sat)
    print("Resultado:  " + respuesta(satisfacible))
    # ////////////////////////////////////////////////////////////////
