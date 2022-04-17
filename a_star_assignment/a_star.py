# Curso de Especialização de Inteligência Artificial Aplicada
# Setor de Educação Profissional e Tecnológica - SEPT
# Universidade Federal do Paraná - UFPR

# IAA003 - Linguagem de Programação Aplicada
# Exercício de implementação do Algoritmo A*

# Aluno: Augusto Cesar Souza Martins
# Data: 30/03/2022
# Uso:
#   ./python3 a_star.py 'Lugoj'
#   ou
#   ./python3 a_star.py

import math
from queue import PriorityQueue
from dists import dists, straight_line_dists_from_bucharest

def a_star(source, dest = 'Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    dest (somente Bucharest neste caso) segundo o algoritmo A*
    """

    if source not in dists:
        return "Cidade não encontrada"

    visited = {}
    border = PriorityQueue()
    heuristic_dict = straight_line_dists_from_bucharest
    cities = dists

    border.put((heuristic_dict[source], 0, source, [source]))
    visited[source] = heuristic_dict[source]

    while not border.empty():
        (heuristic, cost, node, path) = border.get()

        if node == dest:
            return path

        for (city_name, weight) in cities[node]:
            current_cost = cost + weight
            heuristic = current_cost + heuristic_dict[city_name]

            if not city_name in visited or visited[city_name] >= heuristic:
                visited[city_name] = heuristic
                border.put((heuristic, current_cost, city_name, path + [city_name]))
                    
def main(start = 'Timisoara'):
    print(a_star(start))

import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        NAME = sys.argv[1]
    else:
        NAME = 'Timisoara'
        print("Você pode usar 'Nome da Cidade' para iniciar. Começando em 'Timisoara'")
        
    main(NAME)