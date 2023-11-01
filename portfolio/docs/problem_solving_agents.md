# Agentes solucionadores de problemas

## Definição de problema

Podemos definir um problema usando quatro características:

- Estado inicial do problema
- Ações possíveis
- Teste de término
- Função de custo da solução

### Estado inicial do problema

Onde o agente é iniciado. 
Ex: posição inicial de um robô.

### Ações possíveis

Conjunto de ações que o agente pode executar, pela função sucessor ou pelo conjunto de operadores. 
Sendo que a função sucessor é uma função que recebe um estado e retorna um conjunto de ações possíveis.
E o conjunto de operadores é um conjunto de ações possíveis para gerar os sucessores.
Ex: movimentar-se para frente, para trás, para esquerda ou para direita.

### Um teste de término

Define um conjunto de estados que são considerados como solução, sendo que
estes estados podem ser chamados de objetivo. Porém esse conjunto de estados
pode ser algo mais simples e abstrato, assim como uma situação de check-mate
no xadrez.

### Função de custo da solução

É uma função que recebe uma solução e retorna um valor numérico que representa
o custo da solução, também conhecida por medida de desempenho. 
O objetivo é encontrar a solução com o menor custo possível.

# Problemas de Malha Fechada e Malha Aberta em Agentes de Soluções de Problemas

Os termos "malha fechada" e "malha aberta" são frequentemente usados para 
descrever o grau de interação e feedback entre um agente e seu ambiente. 
Ambos têm implicações importantes no design e na operação de agentes de 
soluções de problemas.

## Malha Fechada
Em um sistema de malha fechada, o agente recebe feedback contínuo do ambiente 
e ajusta suas ações com base nesse feedback. Isso é comum em cenários onde o 
estado do ambiente pode mudar dinamicamente, e o agente precisa se adaptar a 
essas mudanças em tempo real.

### Como Funciona: 
O agente toma uma ação, observa o resultado e o usa para informar a próxima 
ação.

### Aplicações:

Robótica, onde o robô precisa se ajustar a obstáculos em movimento.
Mercados financeiros, onde o agente de negociação precisa se adaptar às 
flutuações de preço.

### Desafios:

Requer capacidade de processamento em tempo real.
Pode exigir algoritmos de aprendizado por reforço ou outros métodos de 
aprendizado de máquina para adaptar-se eficazmente.

## Malha Aberta

Em um sistema de malha aberta, o agente não recebe feedback em tempo real ou 
não o utiliza para ajustar suas ações futuras. Ele se baseia mais em um modelo 
predefinido do ambiente e em um plano estabelecido.

### Como Funciona: 

O agente toma uma série de ações com base em um plano predefinido, sem 
necessariamente revisar ou ajustar o plano em resposta às mudanças no ambiente.

### Aplicações:

Resolução de problemas de quebra-cabeça como o Cubo de Rubik.
Planejamento de rota em um mapa estático.

### Desafios:

Menos adaptável a mudanças no ambiente.
O plano inicial precisa ser bem elaborado para garantir o sucesso.


## Intersecção entre Malha Fechada e Malha Aberta

Em muitas aplicações práticas, os agentes operam em um espectro entre malha 
fechada e malha aberta. Por exemplo, um carro autônomo pode ter um plano de 
rota geral (abordagem de malha aberta), mas ainda precisa se adaptar a outros 
veículos e condições da estrada em tempo real (abordagem de malha fechada).

Problemas de malha fechada são não deterministicos por sofrer interferências
externas do ambiente. Já problemas de malha aberta são determinísticos pois
não sofrem interferências externas do ambiente.

# Em Resumo
A escolha entre malha fechada e malha aberta dependerá do problema específico 
que o agente de soluções de problemas está tentando resolver, do ambiente em 
que está operando e dos recursos computacionais disponíveis. Ambos têm seus 
próprios conjuntos de desafios e vantagens, e compreendê-los é crucial para 
o design eficaz de agentes inteligentes.

# Bibliografia

https://edisciplinas.usp.br/pluginfile.php/4848799/mod_resource/content/3/2019-ProblemasComoBusca-BuscaCega.pdf

https://edisciplinas.usp.br/pluginfile.php/4183182/mod_resource/content/1/Aula1V2017.pdf