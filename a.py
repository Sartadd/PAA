import random
import math

def calcular_satisfacao(formula, atribuicao):
    """ Calcula o número de cláusulas satisfeitas dada uma atribuição de variáveis. """
    satisfacao = 0
    for clausula in formula:
        if any(literal if literal > 0 else not atribuicao[abs(literal) - 1] for literal in clausula):
            satisfacao += 1
    return satisfacao

def gerar_vizinho(atribuicao):
    """ Gera um vizinho modificando aleatoriamente uma variável. """
    vizinho = atribuicao[:]
    i = random.randint(0, len(atribuicao) - 1)
    vizinho[i] = not vizinho[i]
    return vizinho

def tempera_simulada_maxsat(formula, num_variaveis, T_max=100.0, T_min=1.0, alpha=0.95, iteracoes=100):
    """ Implementa a têmpera simulada para o problema MAX-SAT. """
    T = T_max
    estado = [random.choice([True, False]) for _ in range(num_variaveis)]
    melhor_estado = estado[:]
    melhor_custo = calcular_satisfacao(formula, melhor_estado)

    while T > T_min:
        for _ in range(iteracoes):
            vizinho = gerar_vizinho(estado)
            delta_E = calcular_satisfacao(formula, vizinho) - calcular_satisfacao(formula, estado)

            if delta_E > 0 or random.random() < math.exp(delta_E / T):
                estado = vizinho[:]

            if calcular_satisfacao(formula, estado) > melhor_custo:
                melhor_estado = estado[:]
                melhor_custo = calcular_satisfacao(formula, melhor_estado)

        T *= alpha  # Resfriamento

    return melhor_estado, melhor_custo

# Exemplo de entrada: Fórmula em forma de lista de cláusulas (cada cláusula é uma lista de inteiros)
formula = [[1, 2, 3], [-2, 3, 1]]
num_variaveis = 3

# Executando a têmpera simulada
melhor_atribuicao, max_satisfacao = tempera_simulada_maxsat(formula, num_variaveis)
print("Melhor atribuição encontrada:", melhor_atribuicao)
print("Número de cláusulas satisfeitas:", max_satisfacao)
