# **Problemas de Satisfação de Condições (CSPs)**

## Impressões iniciais

Como engenheiro de software, você provavelmente já se deparou com problemas 
complexos que envolvem várias condições e restrições. Nesse contexto, os 
Problemas de Satisfação de Restrições (CSPs) são extremamente relevantes.

Imagine que você está desenvolvendo um sistema de agendamento. 
Há várias variáveis em jogo: as disponibilidades de tempo, os recursos 
necessários, as preferências dos usuários, entre outros. 
Aqui, cada variável (X) representa um elemento desse sistema - por exemplo, 
um intervalo de tempo específico ou um recurso. Cada uma dessas variáveis tem 
um domínio (D), que é o conjunto de valores possíveis que ela pode assumir. 
Por exemplo, o domínio de um intervalo de tempo pode ser as horas do dia 
durante as quais uma sala está disponível.

Agora, as restrições (C) são as condições que determinam como essas variáveis 
podem ser combinadas. Por exemplo, uma sala não pode ser reservada para dois 
eventos diferentes ao mesmo tempo. O desafio em CSPs é encontrar uma 
atribuição para todas as variáveis que satisfaça todas essas restrições.

Resolver CSPs pode ser complexo, especialmente quando temos muitas variáveis e 
restrições. Uma abordagem é usar backtracking, que é um tipo de pesquisa em 
profundidade. Basicamente, você tenta uma solução, e se encontrar um conflito, 
volta atrás (backtrack) e tenta uma abordagem diferente. 
É um método poderoso, mas pode ser ineficiente para problemas muito grandes.

Outras técnicas incluem algoritmos de consistência local, que tentam reduzir o 
tamanho do problema eliminando valores que não podem fazer parte de uma solução 
válida. Também temos heurísticas de pesquisa, como a busca com propagação de 
restrições, que tentam antecipar e resolver conflitos antes que eles ocorram.

Em resumo, os CSPs são uma ferramenta poderosa em IA e ciência da computação, 
ajudando-nos a lidar com problemas complexos onde várias condições e restrições 
precisam ser satisfeitas simultaneamente. Eles são aplicáveis em uma variedade 
de campos, desde planejamento e agendamento até design de circuitos e jogos. 
Como engenheiros de software, entender e aplicar CSPs pode nos ajudar a criar 
soluções mais eficientes e eficazes para problemas complexos.

# Representação Atômica vs Fatorada

A representação atômica de um estado é similar a uma representação de caixa 
preta, ou seja, não temos informações sobre suas propriedades e componentes
internos. Quando temos uma representação mais complexa e expressiva, temos
uma representação fatorada, onde temos acesso aos atributos de um estado.

```mermaid
graph TD
    subgraph "Representação Atômica"
        A[Estado atômico A] --> B[Estado Atômico B] --> C[Estado Atômico C]
    end

    
    subgraph "Representação Fatorada"
        subgraph Estado_A
            F[Estado fatorado A]
            F -->|Detalhe 1| J[Propriedade 1]
            F -->|Detalhe 2| K[Propriedade 2]
            F -->|Detalhe 3| I[Propriedade 3]
        end
    
        subgraph Estado_B
            X[Estado fatorado A]
            X -->|Detalhe 1| Y[Propriedade 1]
            X -->|Detalhe 2| Z[Propriedade 2]
            X -->|Detalhe 3| L[Propriedade 3]
        end

        Estado_A ---> Estado_B

    end
```

Ao trabalhar com CSPs, iremos dar ênfase a representação fatorada do estados 
pois precisamos ter uma visão mais granular sobre o problema, e tendo a 
possibilidade de quebrar o problema em subproblemas facilita a encontrar a
solução.

# Definindo Problemas de Satisfação de Condições

A idéia principal de usar uma CSP se baseia em achar uma solução eliminando
grandes porções do espaço de busca ao identificar condições neste espaço de
busca que impossibilitam o resultado.

Em termos mais técnicos, um CSPs são tipicamente definidas por três 
componentes:

- **Variáveis** (X): Um conjunto finito de variáveis que precisam ser resolvidas.
- **Domínios** (D): Um conjunto finito de valores que as variáveis podem assumir.
- **Restrições** (C): Um conjunto de condições que as soluções devem satisfazer.

Tendo definido isso, podemos dizer que CSPs lidam com atribuições de valores
às variáveis.
- Quando uma atribuição não viola nenhuma restrição, ela é chamada de
**consistente**;
- Quando todas as variáveis recebem um valor, a atribuição é **completa**;
- Quando nem todas as variáveis recebem um valor, a atribuição é **parcial**;

Então para definir uma **solução**, precisamos que ela seja 
**consistente e completa**. Logo, uma solução parcial é aquela que é completa
porém nem todas as variáveis são atribuias a algum valor.
Soluções de CSP são problemas NP-Completo em geral.

# Tipos de Condições


## Condições necessárias

Iremos dar ênfase aos seguintes tipos de condições:

- Unárias
- Binária
- Alta Ordem (Ternária+)
- Global

### Restrições Unárias
- **Conceito**: As restrições unárias são as mais simples em CSPs. 
Elas afetam uma única variável.
- **Exemplo**: Uma restrição que especifica que uma variável \( X \) deve 
ser maior que 5.

### Restrições Binárias
- **Conceito**: As restrições binárias envolvem duas variáveis e estabelecem 
uma relação entre elas.
- **Exemplo**: Uma restrição que exige que duas variáveis \( X \) e 
\( Y \) sejam diferentes entre si.

### Restrições de Alta Ordem (Ternária+)
- **Conceito**: As restrições de alta ordem envolvem três ou mais variáveis.
Elas são mais complexas que as unárias e binárias e permitem expressar relações
entre grupos de muitas variáveis.
- **Exemplo**: Uma restrição que determina que a soma das variáveis \( X, Y, \)
e \( Z \) deve ser igual a um valor específico.

### Restrições Globais
- **Conceito**: As restrições globais afetam um grande número de variáveis, às 
vezes todas em um CSP. 
Elas são úteis para expressar condições abrangentes que envolvem múltiplas 
variáveis.
- **Exemplo**: Uma restrição de que todas as variáveis em um conjunto devem 
ter valores diferentes, como na regra do Sudoku, onde cada número deve 
aparecer apenas uma vez em cada linha, coluna e bloco.

**Qualquer uma dessas condições de CSP podem ser reduzidas a condições biárias.**

## Condições de preferência

Ao contrário das condições necessárias, que são obrigatórias para resolução do
CSP, as condições de preferência servem para encontrarmos uma solução preferida.

**Por exemplo:**
> Em um jogo onde um mago precisa atravessar o campo de batalha,
> ele tem diversos caminhos para escolher que satisfazem as condições que o mago
> irá chegar ao outro lado do campo vivo e sem atacar nenhum aliado. Mas o mago
> pode preferir ir por um caminho onde ele enfrente o máximo de inimigos, 
> ou então pode preferir ir por um caminho onde há mais espólios, ou então pode
> preferir ir por um caminho onde ele perca o mínimo de vida possível. Isso tudo
> são preferências, e não uma condição obrigatória.

## Propagação de condição

Para ocorrer a propagação de condições, um algoritmo CSP reduz o domínio de
valores que uma variável pode assumir, que pode reduzir o domínio de outra
variável e assim sucessivamente. O objetivo de propagação de condições é
garantir a consistência local.

Para explicar o parágrafo acima, iremos explicar como ocorre o funcionamento
da propagação de condições em CSPs:

### Funcionamento

**Redução de Domínio**: Inicialmente, cada variável em um CSP tem um 
conjunto de possíveis valores que pode assumir (seu domínio). Quando 
uma restrição é aplicada, o domínio de uma variável pode ser reduzido. 
Por exemplo, se temos uma variável \( X \) com um domínio de {1, 2, 3, 4, 5} e
uma restrição unária \( X > 2 \), o domínio de \( X \) é reduzido para 
{3, 4, 5}.

**Efeito Cascata**: Esta redução pode ter um efeito cascata. Considerando 
uma restrição binária entre \( X \) e \( Y \), a alteração no domínio de 
\( X \) pode levar a uma redução no domínio de \( Y \). Por exemplo, se 
\( Y \) deve ser diferente de \( X \) e o novo domínio de \( X \) é {3, 4, 5}, 
então os valores correspondentes são removidos do domínio de \( Y \).

**Consistência Local**: O objetivo da propagação é alcançar a 
consistência local. Isso significa que para cada variável e suas restrições 
diretas (com outras variáveis), existe pelo menos uma atribuição válida que 
satisfaz as restrições.

### Impacto no Desenvolvimento de Software

Para um engenheiro de software, a questão de propagação de condições pode ter
as seguintes importâncias:

- **Otimização de Algoritmos**: Utilizar a propagação de condições em CSPs pode
significar a diferença entre um algoritmo que resolve problemas em tempo hábil e
um que não é viável para uso prático.

- **Complexidade Computacional**: A propagação eficaz de condições pode reduzir
drasticamente o espaço de busca, diminuindo a complexidade computacional do
problema.

- **Aplicações Práticas**: Em sistemas de agendamento, planejamento de recursos,
ou em soluções de problemas lógicos como Sudoku, a propagação de condições é uma
técnica essencial para garantir soluções eficientes.

Em resumo, a propagação de condições em CSPs é uma técnica fundamental para 
qualquer engenheiro de software envolvido na solução de problemas complexos que 
requerem otimização e eficiência. Ela não só reduz o espaço de busca, como 
também assegura a consistência local das soluções, dois aspectos cruciais para a 
eficiência dos sistemas que desenvolvemos e mantemos.


# Consistência

## Nó

## Arco

## Trajeto

## K

## Globais

# Algoritmos

# Estrutura de Problemas

# Discussões

# Projetos e problemas

# Bibliografia

https://folivetti.github.io/courses/IA/PDF/Aula04.pdf

https://en.wikipedia.org/wiki/AC-3_algorithm

https://www.cs.cmu.edu/~arielpro/15381f16/c_slides/781f16-3.pdf