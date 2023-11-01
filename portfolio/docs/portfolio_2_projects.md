# Projetos e problemas

Algoritmos de busca possuem muitas aplicabilidades e são muito parecidos;
Inclusive, um motivo para isso é que muitos algoritmos de busca são
variações de um mesmo algoritmo. Porém, cada um possui suas vantagens e
desvantagens, e é importante saber quando utilizar cada um deles.

## [LootMaze](https://github.com/fmaachadoo/LootMaze)

O LootMaze é um jogo que criei para experimentar com diferentes tipos de
algoritmos de busca. O jogo é um labirinto onde o jogador deve encontrar o
caminho mais curto para chegar ao objetivo. O código está disponível no
[Github](https://github.com/fmaachadoo/LootMaze).

Este projeto inclui uma interface gráfica para visualizar o labirinto e
os algoritmos de busca em ação. Em cada execução do jogo, o personagem no jogo
executa os algoritmos A\* (A-star), Dijkstra e DFS (Depth-First Search) para
encontrar o caminho mais curto para o objetivo.

A cada execução do algoritmo, é registrado a visualização dos passos que o
algoritmo tomou para encontrar o caminho mais curto. Também é exibido a
quantidade de passos que o algoritmo tomou para encontrar o caminho mais curto
e também o tamanho do mesmo.

Assim que o algoritmo encontra o caminho mais curto, o personagem executa uma
animação seguindo o caminho encontrado.

![Printscreen do Jogo](https://user-images.githubusercontent.com/40258400/238491363-68616b91-638e-490a-add8-12799581e19b.png)

Um ponto interessante do jogo é que os labirintos são personalizáveis. O arquivo
que guarda as informações do labirinto é na verdade um arquivo PNG, então fica
fácil de editar e criar novos labirintos para experimentar com os algoritmos.

Esse jogo é um ótimo projeto para adicionar melhorias como obstaculos e inimigos
tanto como novos algoritmos e heurísticas para encontrar o objetivo.

No caso, para o algoritmo A\* no jogo, implementei usando a Manhattan Distance para
estimar o custo do caminho mais curto.