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

## Lógica

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

## Processo de inferência

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


## Agente baseado em lógica proposicional

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

## Projeto e discussões

### [Prolog](https://www.swi-prolog.org/pldoc/doc_for?object=manual)

Agentes baseados em conhecimento podem ser utilizado em inúmeras aplicações,
tanto em jogos quanto em contexto medicinal por exemplo, ajudando em análises
e identificação de possíveis problemas.

Podemos citar que esse tipo de agente não é novidade no ramo da inteligência
artificial. Uma linguagem que consegue ter a vantagem de facilidade do
desenvolvimento desses agentes é Prolog, que é uma linguagem que utiliza
um paradigma lógico matemático.

Prolog é amplamente utilizado em sistemas de inferência e resolução de 
problemas em IA, graças à sua habilidade natural de representar regras de 
conhecimento e realizar inferências lógicas. Também é eficiente em problemas de 
busca, processamento de linguagem natural e na representação de conhecimento e 
ontologias, sendo útil para prototipagem rápida devido à sua natureza de alto 
nível.
Apesar de suas vantagens, Prolog tem limitações em termos de desempenho, principalmente em aplicações que exigem alto processamento. Sua curva de 
aprendizado pode ser íngrime para quem está acostumado com linguagens 
imperativas, e a escalabilidade pode ser um desafio em sistemas muito grandes e 
complexos.

> Eu já [desenvolvi um sistema em Prolog](https://github.com/fmaachadoo/2021.2-G2_Solaire_Disciples_Logical_Hospital_Triage) 
> para gerar a Classificação de Manchester em um hospital fictício. O sistema
> utiliza conhecimento sobre a situação dos pacientes para fazer um rankeamento
> e gerar uma fila de prioridade para o atendimento.


### Coup Simplificado

Para exemplificar e explicar um pouco melhor como um agente baseado em 
conhecimento funciona, fiz um programa que simula uma versão simplificada do
jogo 
[Coup](https://tabulaquadrada.com.br/review-coup-que-mane-golpinho-o-que/).

As regras do jogo são:
    - Inicialmente cada jogador recebe duas cartas e duas moedas.
    - Quando é a vez do jogador, ele pode escolher realizar uma ação comum ou uma ação da carta.
    - Algumas cartas podem bloquear certas ações.
    - Quando um jogador possui 10 ou mais moedas, ele é obrigado a realizar a ação de golpe de estado.
    - Ganha o jogador que ainda tiver carta quando nenhum outro jogador tem uma carta.

As ações comuns são:
    - Coup, ou Golpe de Estado: O jogador gasta 7 moedas e elimina uma carta inimiga, e essa ação não pode ser bloqueada.
    - Income, ou Renda: O jogador pega apenas uma moeda do jogo para si, esta ação não pode ser bloqueada.
    - Foreign Aid, ou Ajuda Externa: O jogador pode pegar duas moedas do jogo, porém um Duque pode bloquear essa ação.

As cartas são chamadas de influências:
    - Duque (Duke)
        - Tax: O duque pode pegar 3 moedas do jogo para si, esta ação não pode ser bloqueada.
        - O duque pode bloquear a ação de Ajuda Externa de outro jogador.
    - Capitão (Captain)
        - O capitão pode roubar duas moedas de outro jogador, essa ação pode ser bloqueada se e somente se o outro jogador também tiver um capitão.
    - Assassino (Assassin)
        - O assassino gasta 3 moedas para tentar assassinar outro jogador. Essa ação pode ser bloqueada se e somente se o outro jogador tiver uma Condessa.
    - Condessa (Contessa)
        - Apenas bloqueia o assassinado de si mesmo.

> Observação: Para fins de simplicidade o Embaixador foi retirado do jogo.

> Observação 2: Para fins de simplicidade retiramos a possibilidade de Blefe.

O código do jogo se encontra na pasta [ai_coup dentro do repositório do presente
documento](https://github.com/fmaachadoo/artificial-intelligence-study-portfolio/tree/main/ai_coup).

#### Execução

Para executar o projeto, basta executar o comando:

```sh
python main.py
```

A partir daí, o programa irá imprimir na tela que operações os jogadores estão
realizando e como os agentes baseados em conhecimento estão tomando deciões e
guardando conhecimentos em sua base. Exemplo:

```sh

------------------
Bob has 5 coins and [Assassin, Duke] cards
Shirley has 2 coins and [Contessa, Contessa] cards
[32mAI Guilherme[37m has 2 coins and [Contessa, Captain] cards
[32mAI Kung Lao[37m has 2 coins and [Duke, Captain] cards
------------------

[32mAI Guilherme[37m's turn
[32mAI Guilherme[37m is targeting Bob because it has 5 coins
[32mAI Guilherme[37m decides to Steal against Bob
Steal was Successful by Bob
[02m
[32mAI Guilherme[37m acknowledged: [32mAI Guilherme[37m Steal Bob was Successful
[32mAI Guilherme[37m acknowledged: Bob was stolen
[32mAI Guilherme[37m is predicting the game
Since Bob played Tax,[32mAI Guilherme[37m inferred Bob has a Duke
Since Bob was stolen,[32mAI Guilherme[37m inferred Bob doesnt have a Captain
[32mAI Guilherme[37m inferred, as a final guess, that Bob has ['Duke']
Since Shirley played Foreign Aid,[32mAI Guilherme[37m inferred Shirley doesnt have a Duke
[32mAI Guilherme[37m inferred, as a final guess, that Shirley has []
[32mAI Guilherme[37m inferred, as a final guess, that [32mAI Kung Lao[37m has []
[0m
[02m
[32mAI Kung Lao[37m acknowledged: [32mAI Guilherme[37m Steal Bob was Successful
[32mAI Kung Lao[37m acknowledged: Bob was stolen
[32mAI Kung Lao[37m is predicting the game
Since Bob played Tax,[32mAI Kung Lao[37m inferred Bob has a Duke
Since Bob was stolen,[32mAI Kung Lao[37m inferred Bob doesnt have a Captain
[32mAI Kung Lao[37m inferred, as a final guess, that Bob has ['Duke']
Since Shirley played Foreign Aid,[32mAI Kung Lao[37m inferred Shirley doesnt have a Duke
[32mAI Kung Lao[37m inferred, as a final guess, that Shirley has []
Since [32mAI Guilherme[37m played Steal,[32mAI Kung Lao[37m inferred [32mAI Guilherme[37m has a Captain
[32mAI Kung Lao[37m inferred, as a final guess, that [32mAI Guilherme[37m has ['Captain']
[0m

------------------
Bob has 3 coins and [Assassin, Duke] cards
Shirley has 2 coins and [Contessa, Contessa] cards
[32mAI Guilherme[37m has 2 coins and [Contessa, Captain] cards
[32mAI Kung Lao[37m has 2 coins and [Duke, Captain] cards
------------------
```

Nesta simulação temos dois tipos de agente:

- Bob e Shirley são agentes que possuem uma lógica básica de como jogar o jogo e não possuem base de conhecimento, fazendo assim que possam cometer erros ao tomar decisões.
- AI Guilherme e AI Kung Lao são agentes que possuem base de conhecimento e possuem uma lógica programada com a abordagem procedural.

Então a cada jogada os agentes vão percebendo o que aconteceu e adicionando em
sua base de conhecimento, para posteriormente inferir quais cartas os jogadores
têm e poder tomar decisões mais corretas.

Podemos ver nos logs que quando AI Guilherme tentou roubar duas moedas do Bob,
que o roubo foi feito com sucesso, então a partir disso, AI Kung Lao pode
inferir que AI Guilherme possui pelomenos um Capitão e que Bob não possui um 
capitão.

```
AI Kung Lao acknowledged: AI Guilherme Steal Bob was Successful
AI Kung Lao acknowledged: Bob was stolen
AI Kung Lao is predicting the game
Since Bob played Tax, AI Kung Lao inferred Bob has a Duke
Since Bob was stolen, AI Kung Lao inferred Bob doesnt have a Captain
AI Kung Lao inferred, as a final guess, that Bob has ['Duke']
Since Shirley played Foreign Aid, AI Kung Lao inferred Shirley doesnt have a Duke
AI Kung Lao inferred, as a final guess, that Shirley has []
Since AI Guilherme played Steal,AI Kung Lao inferred AI Guilherme has a Captain
AI Kung Lao inferred, as a final guess, that AI Guilherme has ['Captain']
```

> AI Kung Lao também continuou inferindo ações em rodadas passadas do jogo.

A lógica de inferência dos agentes é a seguinte:

```python
def predict_player_cards(self, player):
        # Initialize a dictionary to hold the inferred cards for the player
        inferred_cards = {
            "Duke": 0,
            "Assassin": 0,
            "Captain": 0,
            "Contessa": 0,
        }

        # Logical propositions based on actions
        for action in self.knowledge[player]["actions"]:
            if action == "Tax":
                print(
                    f"Since {player.name} played Tax,"
                    f"{self.name} inferred {player.name} has a Duke"
                )
                inferred_cards["Duke"] = 1
            elif action == "Assassinate":
                print(
                    f"Since {player.name} played Assassinate,"
                    f"{self.name} inferred {player.name} has an Assassin"
                )
                inferred_cards["Assassin"] = 1
            elif action == "Steal":
                print(
                    f"Since {player.name} played Steal,"
                    f"{self.name} inferred {player.name} has a Captain"
                )
                inferred_cards["Captain"] = 1
            elif action == "Block Foreign Aid":
                print(
                    f"Since {player.name} blocked Foreign Aid,"
                    f"{self.name} inferred {player.name} has a Duke"
                )
                inferred_cards["Duke"] = 1
            elif action == "Block Assassination":
                print(
                    f"Since {player.name} blocked Assassination,"
                    f"{self.name} inferred {player.name} has a Contessa"
                )
                inferred_cards["Contessa"] = 1
            elif action in ["Foreign Aid", "Income"]:
                print(
                    f"Since {player.name} played {action},"
                    f"{self.name} inferred {player.name} doesnt have a Duke"
                )
                inferred_cards["Duke"] = 0
            elif action == "Assassinated":
                print(
                    f"Since {player.name} was assassinated,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Contessa"
                )
                inferred_cards["Contessa"] = 0
            elif action == "Stolen":
                print(
                    f"Since {player.name} was stolen,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Captain"
                )
                inferred_cards["Captain"] = 0
            elif action == 'No block Foreign Aid':
                print(
                    f"Since no one blocked Foreign Aid,"
                    f"{self.name} inferred {player.name} doesnt have a "
                    f"Duke"
                )
                inferred_cards["Duke"] = 0
            elif action == 'Block Stealing':
                print(
                    f"Since {player.name} blocked Stealing,"
                    f"{self.name} inferred {player.name} has a Captain"
                )
                inferred_cards["Captain"] = 1

        cards = filter(lambda x: x[1] > 0, inferred_cards.items())

        # Find the two most likely cards
        sorted_cards = sorted(cards, key=lambda x: x[1], reverse=True)
        
        most_likely_cards = [card[0] for card in sorted_cards[:2]]

        print(
            f"{self.name} inferred, as a final guess, "
            f"that {player.name} has {most_likely_cards}"
        )
        
        return most_likely_cards
```

É uma lógica simples, porém possui uma falha ao lidar com incertezas. 
Por exemplo, quando a partida começa e ainda não temos nenhum conhecimento
sobre os outros jogadores. Porém isso é fácil de resolver, incrementando o
agente com lógica baseada em probabilidade.

Enquanto isso temos a lógica para a tomada de decisões na jogada.
Primeiro o agente irá escolher o jogador mais ameaçador 
(com mais cartas e mais moedas) e em seguida irá definir o que é possível fazer
contra esse jogador tendo como base o conhecimendo de quais cartas esse jogador
possui. Caso não seja possível realizar nenhuma ação contra esse jogador,
o agente irá ver qual outra ação ele pode fazer sem ser bloqueado por outro
jogador.

```python
    def get_target_priority(self):
        def sort_key(target):
            return (
                self.knowledge[target]["card_amount"], 
                self.knowledge[target]["coins"]
            )

        return sorted(
            self.players,
            key=sort_key,
            reverse=True,
        )

    def decide_action(self):
        target_list = self.get_target_priority()
        for target in target_list:
            if target.name == self.name:
                continue

            print(
                f"{self.name} is targeting {target.name} because it has "
                f"{target.coins} coins"
            )

            if not target.is_alive():
                print("The target is dead... choosing other target")
                continue

            if self.coins >= 10:
                print(
                    f"{self.name} has 10+ coins and is obligated to coup"
                )
                return Coup, target

            random.shuffle(self.cards)

            for card in self.cards:
                if card.has_action:
                    if (
                        card.action.name == 'Assassinate' and 
                        (
                            self.coins < 3 or 
                            self.target_has(target, "Contessa")
                        )
                    ):
                        print(
                            f"{self.name} knows that can't assassinate "
                            f"{target.name}"
                        )
                        continue
                    
                    if self.coins >= 7:
                        return Coup, target

                    if (
                        card.action.name == 'Steal' and 
                        self.target_has(target, "Captain")
                    ):
                        print(
                            f"{self.name} knows that can't steal "
                            f"from {target.name}"
                        )
                        continue

                    target = (target if card.action.require_target else None)

                    return card.action, target
            
            if self.game_hasnt("Duke"):
                return ForeignAid, None
            
            return Income, None

```

## Bibliografia

- Aula 12 de Inteligência Artificial, ministrada na Universidade de Brasília pelo
professor Fabiano Araújo Soares.

- https://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/slides/aula1021.pdf

- https://www.ime.usp.br/~leliane/IAcurso2006/slides/Aula7-LProposicional-I-2006.pdf

- https://www.cin.ufpe.br/~in1116/aulas/agentes-bc.pptx

- https://www.swi-prolog.org/pldoc/doc_for?object=manual
