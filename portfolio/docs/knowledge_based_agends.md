# Agentes baseados em conhecimento

Agentes baseados em conhecimento são projetados para operar em domínios 
específicos. Eles utilizam um vasto conjunto de conhecimentos sobre esse 
domínio para interpretar dados, resolver problemas e tomar decisões.
Esses conhecimentos sobre o domínio se sintetizam em forma de uma base de 
conhecimento que armazena fatos, regras, heurísticas e relações que são 
estruturados de forma que o agente possa acessá-la e interpretá-la 
eficientemente utilizando regras de lógica, utilizando raciocínio dedutivo,
indutivo ou abdutivo.

Explicando novamente:

Podemos chamar essa base de conhecimento de *knowledge base* (KB) e essa
base irá guardar sentenças que representam alguma informação sobre o mundo.
Essas sentenças devem ser capazes de ser aferidas logicamente.

Quando uma sentença na base de conhecimento não depende de outras sentenças,
ou seja, é uma sentença independente, podemos chamar de **axioma**

## TELL & ASK

Essa base de conhecimento é mutável e deve ser capaz de adição de novas
setenças. Comumente, essas operações de adição de sentenças pode ser chamada de
**TELL**.

Assim como podemos adicionar novas sentenças na base de conhecimento, devemos
também ter a capacidade de consultar e aferir as sentenças. Essas operações de
consulta são comumente chamadas de **ASK**.

Ambos os processos mencionados acima podem envolver inferência, gerando novas
sentenças derivando de sentenças antigas.

## Abordagens

Temos duas abordagens para o desenvolvimento do agente baseado em conhecimento:

- Abordagem declarativa: Quando uma base de conhecimento inicia-se vazia, e
as setenças são criadas em tempo de execução, sendo inseridas por um 
projetista.

- Abordagem procedural: Quando as sentenças e comportamentos desejados são
inseridos diretamente no código do programa.

# Lógica

Na lógica, identificamos principalmente dois elementos: 
A sintaxe e a semântica.

A sintaxe, um componente essencial do sistema linguístico em uso, estabelece as 
relações entre os elementos de uma sentença. Ela define a estrutura correta e a 
forma de construção das frases.

Por outro lado, a semântica se ocupa da interpretação das sentenças. Dentro de 
um contexto lógico possível 
(onde as sentenças não violam regras estabelecidas), a semântica é responsável 
por determinar a veracidade das afirmações. 

Tomemos, por exemplo, a sentença *alfa \( α \)*. Se em um modelo específico 
*M*, *α* é considerada verdadeira, então dizemos que *M* satisfaz ou é um 
modelo para **α**.

A relação lógica entre sentenças é expressa pela notação α⊨β. Isso significa 
que α é consequência lógica de β (α implica β), ou que β é verdadeiro se, e 
somente se, α também for verdadeiro.

Então tendo uma base de conhecimentos *KB*, e um algoritmo de inferência tiver 
a capacidade de derivar *α* de *KB*, podemos escrever logicamente: *α* é derivado 
de *KB* por *i* ou *i* deriva *α* de *KB*.

**Quando a sintaxe da lógica proposicional que é utilizada para criar as relações**
**entre as sentenças do nosso agente, podemos definir os seguintes simbolos:**

Snippet *ipsis litteris* retirado do slide da aula 12 de Inteligência 
Artificial, ministrada na Universidade de Brasília pelo professor 
Fabiano Araújo Soares:

    ¬ (não, NOT). Uma sentença como ¬W1,3 é chamada de negação de W1,3. ​

    ∧ (e, AND). Uma sentença cujo conectivo principal é ∧, como W1,3 ∧ P3,1, é chamada de conjunção;​

    ∨ (ou, OR). Uma sentença cujo conectivo principal é ∨, como W1,3 ∨ P3,1, é uma disjunção; ​

    ⇒ (implica, IMPLIES). Uma sentença como (W1,3 ∧ P3,1) ⇒ ¬W2,2 é chamada de implicação (ou condicional). Sua premissa ou antecedente é (W1,3 ∧ P3,1), e sua conclusão ou consequente é ¬W2,2. As implicações também são conhecidas como regras ou declarações if-then. A implicação é escrita em outros livros como ⊃ ou →.​

    ⇔ (se e somente se). A sentença W1,3 ⇔ ¬W2,2 é uma bicondicional.​

    Temos também o ou exclusivo: Não há consenso sobre o símbolo para ou exclusivo, a princípio, vamos adorar ⊕.​

Na programação podemos utilizar a forma Backus-Naur (BNF) para expressar a
sintaxe da lógica dos programas.

## Estrutura Básica BNF

**Símbolos Terminais**: São os elementos básicos da linguagem 
(por exemplo, palavras-chave, operadores, números literais). 
Eles são escritos como estão, sem necessidade de definição adicional.

**Símbolos Não-Terminais**: Representam conjuntos de sequências de símbolos 
terminais e não-terminais. Eles são usualmente descritos em termos de outros 
símbolos não-terminais e terminais.

**Regras de Produção**: São declarações que descrevem como os símbolos 
não-terminais podem ser combinados para formar sequências válidas na linguagem. 
Cada regra de produção tem um símbolo não-terminal no lado esquerdo do sinal 
de igual (::=) e os símbolos que definem esse não-terminal no lado direito.

**Exemplo Simples**

Considere uma linguagem simples onde definimos que uma "expressão" pode ser um 
número, uma adição ou uma subtração:

```go
<expression> ::= <number>
               | <expression> "+" <expression>
               | <expression> "-" <expression>
<number> ::= "0" | "1" | "2" | ... | "9"
```

Esse conceito é utilizado não só em inteligência artificial, mas também em
interpretadores de linguagem por exemplo.

> Em 2019, eu fiz uma linguagem de programação interpretada que utiliza a forma
> Backus-Naur para definir as regras da linguagem. Essa linguagem utiliza uma
> sintaxe formada por palavras em latim. O projeto é chamado de 
> [Latym-language](https://github.com/fmaachadoo/Latym-language) pois foi
> desenvolvido em Python.
>
> Podemos ver no arquvio [grammar.lark](https://github.com/fmaachadoo/Latym-language/blob/master/latym/grammar.lark)
> como que as regras da sintaxe foram definidas.
>
> Observe que a sintática apenas define sintaxe, sendo necessário outro formato
> de definição para a [semântica](https://github.com/fmaachadoo/Latym-language/blob/master/latym/runtime.py).

Já quando falamos da semântica da lógica proposicional, a semântica define
as regras para determinar quando uma sentença é verdadeira em um determinado
modelo.

Darei mais detalhes sobre lógica ao explicar o projeto desenvolvido para
a entrega deste compilado sobre agentes baseados em conhecimento.

# Processo de inferência

No campo da inteligência artificial, especialmente relevante para nós como 
engenheiros de software, o processo de inferência é um aspecto central que 
permeia várias áreas e aplicações. Este processo se baseia em deduzir 
conclusões lógicas a partir de informações disponíveis, utilizando tanto 
raciocínio dedutivo quanto indutivo. A dedução se concentra em tirar conclusões 
necessárias de premissas consideradas verdadeiras, enquanto a indução visa 
extrair conclusões prováveis a partir de observações.

A lógica formal desempenha um papel crucial aqui, fornecendo uma estrutura 
rigorosa para representar e inferir conhecimento. Ela ajuda a distinguir entre 
inferência dedutiva, que lida com conclusões necessárias a partir de premissas 
conhecidas, e inferência indutiva, que busca padrões para gerar conclusões 
prováveis. Em inteligência artificial, isso se traduz em sistemas de inferência 
automática, como os sistemas baseados em regras, que aplicam regras lógicas 
para eficientemente inferir novas informações.

Além disso, a inferência probabilística, que lida com incertezas e atribui 
probabilidades às conclusões, é vital em contextos onde a certeza absoluta é 
inalcançável. Redes Bayesianas são um exemplo típico dessa aplicação. Nos 
sistemas baseados em conhecimento, observamos um ciclo de inferência que 
envolve a coleta de informações, consulta à base de conhecimento, dedução de 
ações apropriadas e, por fim, a execução dessas ações.

No aprendizado de máquina, a inferência é fundamental na capacidade do modelo 
de generalizar a partir dos dados de treinamento para fazer previsões sobre 
novos dados. Assim, seja em sistemas baseados em regras ou em aprendizado de 
máquina, a habilidade de realizar inferências lógicas e probabilísticas é 
essencial para desenvolver soluções eficazes em IA. Este entendimento é crucial 
para nós na engenharia de software, pois permite criar sistemas mais 
inteligentes e adaptáveis.


# Agente baseado em lógica proposicional

Definimos um agente baseado em lógica proposicional, aquele que consegue,
ao utilizar uma base de conhecimento, tomar ações baseado nas relações entre
as sentenças.

Podemos relembrar a Backus-Naur Form para expressar problemas para agentes
baseados em lógica proposicional, de formas que para expressar as sentenças
podemos usar proposições simples, que são unidades básicas de conhecimentos, ou
também podem ser chamadas de átomos, visto que são sentenças indivisíveis. E
para relacionar essas proposições podemos utilizar Conjunções e Disjunções,
como os operadores lógicos `AND` (conjunção "e") ou `OR` (disjunção "ou"),
permitindo assim a criação de sentenças complexas.

> A lógica proposicional é uma forma simples e formal de representar 
> conhecimentos, vantajosa pela sua clareza, simplicidade e facilidade de 
> implementação. Contudo, ela é limitada em expressividade, não sendo adequada 
> para representar relações complexas ou conhecimento hierárquico. Além disso, 
> enfrenta desafios de escalabilidade em sistemas mais complexos, onde a adição 
> de novos fatos pode levar a um aumento exponencial nas combinações a serem 
> consideradas.

# Bibliografia

- Aula 12 de Inteligência Artificial, ministrada na Universidade de Brasília pelo
professor Fabiano Araújo Soares.

- https://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/slides/aula1021.pdf

- https://www.ime.usp.br/~leliane/IAcurso2006/slides/Aula7-LProposicional-I-2006.pdf

- https://www.cin.ufpe.br/~in1116/aulas/agentes-bc.pptx
