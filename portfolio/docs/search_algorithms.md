# Algoritmos de Busca
Algoritmos de busca são essenciais para explorar um espaço de estados a fim de 
encontrar uma solução para um determinado problema. Eles são classificados 
principalmente em dois tipos: Busca Cega (ou Busca Não-Informada) e Busca 
Informada.

## Busca Cega (Busca Não-Informada)
Esses algoritmos não têm informações adicionais sobre estados além daqueles 
que estão explícitos no problema. Eles são chamados de "cegos" porque exploram 
o espaço de estados sem qualquer direção guiada para encontrar a solução.

### Algoritmos Comuns:

- Busca em Largura (Breadth-First Search, BFS)
- Busca em Profundidade (Depth-First Search, DFS)
- Busca de Custo Uniforme

## Como Funciona:

Começam a partir de um estado inicial e expandem a fronteira de estados 
possíveis até atingir o estado objetivo.

# Comparação entre Breadth-First Search, Depth-First Search e Busca de Custo Uniforme

Esses três algoritmos são comumente usados para a resolução de problemas e têm 
suas próprias vantagens e desvantagens. Abaixo, segue uma comparação detalhada 
entre Breadth-First Search (BFS), Depth-First Search (DFS) e Busca de Custo 
Uniforme (UCS).

## Breadth-First Search (BFS)

### Exemplo de algoritmo em Python

```python
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        (current_node, path) = queue.popleft()
        
        if current_node not in visited:
            visited.add(current_node)
            
            if current_node == goal:
                return path
            
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))

# Exemplo de uso
graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C', 'F'], 'F': ['E']}
print(bfs(graph, 'A', 'F'))  # Output: ['A', 'C', 'E', 'F']
```

**Mecanismo**: Explora todos os vizinhos de um nó antes de passar para os 
vizinhos do próximo nível.

**Filosofia**: "Expandir primeiro na largura".

**Completo**: Sim, garante encontrar a solução se uma existir.

**Ótimo**: Sim, se o custo para cada passo for o mesmo.

**Uso de Memória**: Elevado, pois mantém todos os nós em memória.

**Aplicações**: Útil para encontrar o menor caminho em um espaço de estados, 
em problemas onde a solução mais curta é desejada.

## Depth-First Search (DFS)

### Exemplo de algoritmo em Python

```python
def dfs(graph, current_node, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(current_node)
    path.append(current_node)
    
    if current_node == goal:
        return path
    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path.copy())
            
            if new_path:
                return new_path

# Exemplo de uso
graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C', 'F'], 'F': ['E']}
print(dfs(graph, 'A', 'F'))  # Output: ['A', 'B', 'D', 'C', 'E', 'F']

```

**Mecanismo**: Explora tão profundamente quanto possível ao longo de cada ramo 
antes de retroceder.

**Filosofia**: "Expandir primeiro em profundidade".

**Completo**: Não necessariamente, especialmente em árvores infinitas.

**Ótimo**: Não, pode encontrar uma solução subótima.

**Uso de Memória**: Menor comparado ao BFS, pois armazena apenas o caminho da raiz até o nó atual.

**Aplicações**: Útil em cenários como labirintos e jogos de estratégia, onde 
encontrar qualquer solução válida é mais importante do que encontrar a solução 
mais curta.

## Busca de Custo Uniforme (UCS)

### Exemplo de algoritmo em Python

```python
import heapq

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]
    
    while queue:
        (cost, current_node, path) = heapq.heappop(queue)
        
        if current_node not in visited:
            visited.add(current_node)
            path = path + [current_node]
            
            if current_node == goal:
                return cost, path
            
            for neighbor, edge_cost in graph[current_node].items():
                heapq.heappush(queue, (cost + edge_cost, neighbor, path))

# Exemplo de uso
graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2}, 'C': {'A': 4, 'E': 3}, 'D': {'B': 2}, 'E': {'C': 3, 'F': 5}, 'F': {'E': 5}}
print(ucs(graph, 'A', 'F'))  # Output: (9, ['A', 'B', 'D', 'C', 'E', 'F'])
```

**Mecanismo**: Expandir o nó com o menor custo acumulado até agora.

**Filosofia**: "Expandir com base no custo mais baixo".

**Completo**: Sim, desde que o custo de cada aresta seja maior que algum valor ε>0.

**Ótimo**: Sim, sempre encontra a solução de menor custo.

**Uso de Memória**: Pode ser alto, pois mantém todos os nós visitados em memória.

**Aplicações**: Útil em problemas de roteamento, como encontrar o caminho mais curto em um mapa com diferentes custos de deslocamento.

## Resumo das Diferenças

### Objetivo:

- BFS é geralmente usado para encontrar o caminho mais curto em termos de número de passos.
- DFS é usado para encontrar qualquer solução válida de forma eficiente em memória.
- UCS é usado para encontrar o caminho de menor custo.

### Eficiência:

- BFS e UCS são geralmente mais lentos mas produzem melhores soluções.
- DFS é mais rápido e usa menos memória, mas pode encontrar soluções subótimas.

### Complexidade de Espaço:

- BFS e UCS podem exigir mais memória.
- DFS é mais eficiente em termos de memória.

### Garantia de Solução Ótima:

- BFS só é ótimo quando todos os passos têm o mesmo custo.
- DFS não garante uma solução ótima.
- UCS sempre encontra uma solução ótima, dado que todos os custos de aresta sejam positivos.

</br>

## Busca Informada
Esses algoritmos usam informações adicionais 
(geralmente na forma de uma função heurística) para fazer escolhas mais 
informadas durante a busca, possibilitando encontrar soluções de forma mais 
eficiente.

### Algoritmos Comuns:

- A* (A-Star)
- Best-First Search
- Hill Climbing

## Como Funciona:

Utilizam uma função heurística para estimar o custo do estado atual até o 
estado objetivo, priorizando estados que parecem levar a uma solução mais 
eficiente.

# Comparação entre A*, Best-First Search e Hill Climbing

Esses três algoritmos são tipos de buscas informadas que usam heurísticas para 
direcionar a exploração. Aqui estão suas principais características, vantagens 
e desvantagens:

## A* (A-Star)

```python
"""
Este exemplo contempla o uso da distância de Manhattan como heurística.
"""
import heapq

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    open_set = [(0, start, [])]  # (f_score, current_node, path)
    visited = set()

    while open_set:
        f, current, path = heapq.heappop(open_set)

        if current in visited:
            continue

        path = path + [current]
        visited.add(current)

        if current == goal:
            return f, path

        for neighbor, cost in graph[current].items():
            g = f - manhattan_distance(current, goal)  # Recalculate g_score
            h = manhattan_distance(neighbor, goal)
            f_new = g + cost + h

            heapq.heappush(open_set, (f_new, neighbor, path))

# Exemplo de uso
graph = { (0, 0): {(0, 1): 1, (1, 0): 1.5},
          (0, 1): {(0, 0): 1, (0, 2): 1},
          (0, 2): {(0, 1): 1, (1, 2): 1},
          (1, 0): {(0, 0): 1.5, (1, 1): 1},
          (1, 1): {(1, 0): 1, (1, 2): 1},
          (1, 2): {(1, 1): 1, (0, 2): 1} }
start = (0, 0)
goal = (1, 2)
print(a_star(graph, start, goal))  # Output: (3.5, [(0, 0), (1, 0), (1, 1), (1, 2)])
```

**Mecanismo**: Utiliza tanto o custo acumulado do nó inicial até o nó atual (g(n)) como uma função heurística estimada do nó atual ao nó objetivo (h(n)) para priorizar a exploração.

> No exemplo acima foi usada a Distância de Manhattan como heurística, porém
> essa heurística é apenas um exemplo. O algoritmo pode usar outra função de
> heurística ou combinação de funções de heurísticas.

**Filosofia**: "Expandir o nó que tem a menor soma de custos g(n) + h(n)."

**Completo**: Sim, desde que a heurística seja admissível e consistente.

**Ótimo**: Sim, sob as mesmas condições.

**Aplicações**: Pathfinding, planejamento de movimento, etc.

> A* é um algoritmo que também possui variações, como o A* Epsilon, que é uma
> variação do A* que permite que o algoritmo explore mais nós, porém com um
> custo maior. Isso é útil para encontrar soluções mais rapidamente, porém
> subótimas. [Referência sobre variações do A*](https://en.wikipedia.org/wiki/A*_search_algorithm#Bounded_relaxation)

## Best-First Search

```python
import heapq

def best_first_search(graph, start, goal, heuristic):
    open_set = [(heuristic(start, goal), start, [])]
    visited = set()

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current in visited:
            continue

        path = path + [current]
        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            h = heuristic(neighbor, goal)
            heapq.heappush(open_set, (h, neighbor, path))

# Exemplo de uso
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E', 'F'], 'D': [], 'E': [], 'F': []}
heuristic = lambda x, y: ord(y) - ord(x)
start = 'A'
goal = 'F'
print(best_first_search(graph, start, goal, heuristic))  # Output: ['A', 'C', 'F']
```

**Mecanismo**: Utiliza apenas a função heurística (h(n)) para direcionar a busca.

**Filosofia**: "Expandir o nó que parece mais próximo do objetivo com base na heurística."

**Completo**: Não necessariamente.

**Ótimo**: Não.

**Aplicações**: Problemas em que encontrar uma solução rapidamente é mais importante do que encontrar a melhor solução.

## Hill Climbing

```python
def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]

    while current != goal:
        neighbors = [(neighbor, heuristic(neighbor, goal)) for neighbor in graph[current]]
        if not neighbors:
            return None  # Falhou em encontrar um caminho

        # Escolhe o vizinho com a melhor heurística
        best_neighbor, _ = min(neighbors, key=lambda x: x[1])
        
        if heuristic(best_neighbor, goal) >= heuristic(current, goal):
            return None  # Alcançado um máximo local

        current = best_neighbor
        path.append(current)

    return path

# Exemplo de uso
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E', 'F'], 'D': [], 'E': [], 'F': []}
heuristic = lambda x, y: ord(y) - ord(x)
start = 'A'
goal = 'F'
print(hill_climbing(graph, start, goal, heuristic))  # Output: ['A', 'C', 'F']
```

**Mecanismo**: Escolhe o melhor nó vizinho com base na heurística e move-se para ele, sem manter um histórico.

**Filosofia**: "Sempre suba a colina. Se chegar ao topo, pare."

**Completo**: Não.

**Ótimo**: Não.

**Aplicações**: Otimização local, onde encontrar um máximo ou mínimo local é suficiente.

## Resumo das Diferenças

**Heurísticas**:

- A* usa tanto o custo real até o ponto atual (g(n)) quanto uma estimativa para o objetivo (h(n)).
- Best-First e Hill Climbing usam apenas a estimativa para o objetivo (h(n)).

**Ótimalidade**:

- A* é ótimo se a heurística for admissível e consistente.
- Best-First e Hill Climbing não garantem a ótimalidade.

**Completude**:

- A* é completo, enquanto Best-First e Hill Climbing podem falhar em encontrar uma solução.

**Uso de Memória**:

- A* e Best-First podem usar uma quantidade significativa de memória para armazenar nós.
- Hill Climbing usa pouca memória, pois não mantém um histórico de estados.

**Aplicações**:

- A* é geralmente preferido quando uma solução ótima é necessária.
- Best-First é útil quando a velocidade é mais importante do que a precisão.
- Hill Climbing é usado para otimizações locais, onde o espaço de estados é muito grande para explorar completamente.

 Escolher o algoritmo certo depende fortemente do problema específico que você está tentando resolver, das garantias que você precisa (completude, ótimalidade), e dos recursos disponíveis (tempo, memória).

## Considerações Gerais

### Aplicabilidade: 

A escolha do tipo de algoritmo de busca a ser utilizado depende muito do tipo 
de problema. Buscas cegas são mais genéricas e fáceis de implementar, mas podem
ser impraticáveis para espaços de estados muito grandes. Buscas informadas são 
geralmente preferíveis quando se tem um bom conhecimento do domínio do 
problema.

### Recursos Computacionais: 
Algoritmos de busca podem ser intensivos em termos de tempo e memória, o que é 
uma consideração importante em aplicações em tempo real ou em dispositivos com 
recursos limitados.

### Heurísticas: 
Em buscas informadas, a seleção de uma boa heurística é crucial. 
Uma heurística inadequada pode fazer com que o algoritmo funcione mal, 
enquanto uma boa heurística pode resolver o problema de forma muito eficiente.

> Em resumo, algoritmos de busca são uma ferramenta fundamental em IA para a 
> resolução de problemas, e a compreensão dos diferentes tipos e suas 
> aplicações pode fornecer insights valiosos na escolha da estratégia de 
> resolução de problemas mais adequada.

<br>

# **Um algoritmo de busca não discutido em sala de aula**

Ambos os algoritmos comentados abaixo são de busca cega.

## **Dijkstra**

Um algoritmo relacionado aos mencionados acima é o Dijkstra, que é um algoritmo
de busca de caminho mais curto. Ele é um algoritmo de busca em grafos que serve 
para encontrar o caminho mais curto entre um nó inicial e todos os outros nós 
em um grafo ponderado e dirigido. **Importante notar que os pesos das arestas devem ser não-negativos para que o algoritmo funcione corretamente.**

> Vale lembrar que o algoritmo A\* é uma variação do algoritmo de Dijkstra que
> usa heurísticas para encontrar o caminho mais curto. Ou seja, Dijkstra é um
> A* sem heurísticas, ou seja, não informado sobre o ambiente.

```python
import heapq

def dijkstra(graph, start, goal):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == goal:
            return current_distance

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

# Exemplo de uso
graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2}, 'C': {'A': 4, 'E': 3}, 'D': {'B': 2}, 'E': {'C': 3, 'F': 5}, 'F': {'E': 5}}
print(dijkstra(graph, 'A', 'F'))  # Output: 9
```

## **Bellman-Ford**

Outro algoritmo parecido com Dijkstra que também vale mencionar é o Bellman-Ford
que também é um algoritmo de busca de caminho mais curto, porém ele funciona
mesmo quando as arestas possuem pesos negativos. Porém, ele é mais lento que o
Dijkstra.

```python
def bellman_ford(graph, start, end):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour, cost in graph[node].items():
                if distance[node] + cost < distance[neighbour]:
                    distance[neighbour] = distance[node] + cost

    for node in graph:
        for neighbour, cost in graph[node].items():
            if distance[node] + cost < distance[neighbour]:
                print("Graph contains a negative weight cycle")
                return None

    return distance[end]

# Exemplo de uso
graph = {'A': {'B': -1, 'C':  4},
         'B': {'C':  3, 'D':  2, 'E':  2},
         'C': {},
         'D': {'B':  1, 'C':  5},
         'E': {'D': -3}}
print(bellman_ford(graph, 'A', 'E'))  # Output: 1 (seguindo o caminho A -> B -> E)
```

# Comparação entre Dijkstra e Bellman-Ford:

- Dijkstra: Mais rápido para grafos sem arestas negativas, mas falha na presença de pesos negativos.

- Bellman-Ford: Mais lento, mas mais versátil, já que pode lidar com arestas negativas e detectar ciclos negativos.

# Bibliografia

https://edisciplinas.usp.br/pluginfile.php/4848799/mod_resource/content/3/2019-ProblemasComoBusca-BuscaCega.pdf

https://www.ime.usp.br/~cris/mac5711/slides/aula14.pdf

https://www.youtube.com/watch?v=788_MGOgNA4

https://www.youtube.com/watch?v=3cuOA-mxaHg

https://www.youtube.com/watch?v=DlE2C0TTxqk

https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

https://www.geeksforgeeks.org/what-are-the-differences-between-bellman-fords-and-dijkstras-algorithms/