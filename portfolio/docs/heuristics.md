### O que são Funções Heurísticas?

Em termos simples, uma função heurística é como um atalho que ajuda o 
computador a decidir qual opção é "provavelmente" a melhor, sem ter que 
calcular todas as opções em detalhes. Ela dá uma espécie de "nota" para cada 
opção, e a opção com a melhor "nota" é geralmente escolhida.

> Imagine que você está jogando um jogo de tabuleiro e tem várias jogadas 
> possíveis. Você não tem tempo para pensar em todas as consequências de cada 
> movimento até o final do jogo, certo? Em vez disso, você faz um "palpite 
> educado" sobre qual movimento parece ser o melhor. Esse "palpite educado" 
> é essencialmente o que uma função heurística faz em 
> inteligência artificial (IA).

### Importância

Funções heurísticas são importantes porque tornam os algoritmos mais rápidos. 
Em muitos problemas, especialmente em IA, há muitas opções e possibilidades a 
considerar. Calcular todas elas levaria muito tempo e recursos. Uma boa função 
heurística pode reduzir drasticamente esse esforço.

### Exemplos Simples

1. **Jogo da Velha**: Uma heurística simples seria contar o número de linhas, 
colunas ou diagonais que estão a um passo de serem completadas. Quanto mais 
você tiver, melhor é a posição.

2. **Problema do Caminho Mais Curto**: Se você quiser ir de uma cidade A para 
uma cidade B, uma função heurística pode ser a distância em linha reta entre A 
e B. Essa é uma boa estimativa do caminho mais curto possível.

### Como são Utilizadas?

Em algoritmos como A* (A-star), as funções heurísticas são usadas para 
estimar o custo do caminho mais curto de um ponto a outro. O algoritmo usa 
essa estimativa para priorizar quais caminhos explorar primeiro.

### Limitações

1. **Precisão**: Uma função heurística é um palpite, então pode estar errada. 
Uma má heurística pode até piorar o desempenho do algoritmo.

2. **Complexidade**: Algumas funções heurísticas podem ser complicadas de 
calcular, anulando os benefícios de velocidade que oferecem.

### Resumo

Então, uma função heurística é como um "truque" que ajuda os computadores a 
tomar decisões mais rapidamente. Elas são super úteis em IA para tornar os 
algoritmos mais eficientes, mas é importante escolher a heurística certa para 
o problema que você está tentando resolver.

# Contribuindo para o assunto de heurísticas

## Distância de Manhattan

Um exemplo de heurística é a distância de Manhattan, que é a distância entre
dois pontos em um grid, se deslocando apenas na horizontal e vertical. Essa
heurística foi comentada brevemente em sala de aula porém é interessante
aprofundar um pouco mais sobre ela.

A distância de Manhattan é uma função heurística comumente usada em problemas 
que envolvem grade ou espaço bidimensional, como encontrar o caminho mais curto
em um labirinto.

> Implementei uma espécie de jogo para experimentar com diferentes tipos de
> algoritmos de busca. O jogo é um labirinto onde o jogador deve encontrar o
> caminho mais curto para chegar ao objetivo. O código está disponível no
> [Github](https://github.com/fmaachadoo/LootMaze).
>
> **Para o algoritmo A\* no jogo, implementei usando a Manhattan Distance para
> estimar o custo do caminho mais curto.**

![Printscreen do Jogo](https://user-images.githubusercontent.com/40258400/238491363-68616b91-638e-490a-add8-12799581e19b.png)

### O que é Distância de Manhattan?

A distância de Manhattan entre dois pontos \( A \) e \( B \) em um plano é a 
soma das diferenças absolutas de suas coordenadas. Por exemplo, se 
\( A=(x_1, y_1) \) e \( B=(x_2, y_2) \), a distância de Manhattan seria 
\( |x_1 - x_2| + |y_1 - y_2| \).

### Como é Utilizada como Heurística?

Suponha que você está resolvendo um problema de labirinto em uma grade 2D e 
quer encontrar o caminho mais curto de um ponto inicial a um ponto final. 
Você pode usar a distância de Manhattan como uma função heurística para estimar
 o "custo" para chegar do ponto atual ao destino. O algoritmo de busca, como 
 A*, usaria essa estimativa para priorizar quais caminhos explorar.

### Vantagens

1. **Simplicidade**: É fácil de calcular.
2. **Eficiência**: Ajuda o algoritmo de busca a focar nos caminhos mais 
promissores, acelerando a solução do problema.

### Limitações

1. **Admissibilidade**: Em alguns casos, pode não ser a melhor estimativa para 
o custo real. Por exemplo, se o movimento diagonal é permitido, a distância de 
Manhattan pode superestimar o custo.
2. **Aplicabilidade**: É mais útil em espaços bidimensionais ou em problemas 
que podem ser mapeados em uma grade 2D.

### Exemplo em um Problema de Caminho Mais Curto

Suponha que o ponto inicial esteja na coordenada (2, 3) e o ponto final esteja 
na coordenada (5, 6). A distância de Manhattan entre esses pontos seria 
\( |5-2| + |6-3| = 3 + 3 = 6 \).

O algoritmo usaria essa distância para estimar que o custo para ir do ponto 
inicial ao ponto final é de aproximadamente 6 unidades. Isso ajuda o algoritmo 
a priorizar rotas que parecem mais curtas, economizando tempo e recursos 
computacionais.

Então, em resumo, a distância de Manhattan é uma heurística popular e útil, 
especialmente para problemas que envolvem grades ou espaços bidimensionais.

# Bibliografia

https://edisciplinas.usp.br/pluginfile.php/7340740/mod_resource/content/1/IAPos_NA06.pdf

https://www.geeksforgeeks.org/a-search-algorithm/

https://xlinux.nist.gov/dads/HTML/manhattanDistance.html#:~:text=Definition%3A%20The%20distance%20between%20two,y1%20%2D%20y2%7C.

