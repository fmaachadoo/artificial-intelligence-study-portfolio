# Portfolio-3 - CSP

## Projetos e problemas

### Problema de agendamento de eventos

Imagine um problema onde temos vários eventos e temos que agendar esses eventos
em um número definido de salas disponíveis em uma universidade. 
Cada evento tem um horário de início e fim. Então precisamos definir quais
eventos ocorrerão em quais salas.

Para resolver esse problema, podemos usar algoritmos de CSP; Em modos práticos
podemos utilizar uma biblioteca Python chamada `python-constraint` a fim de
definir variáveis, domínios e restrições.

Essa biblioteca simplifica a confecção de um script que resolva uma CSP; 
Utilizando os algoritmos de Backtracking, Recursive backtracking e Min-Conflits
essa biblioteca resolve problemas de domínios finitos.

Para demonstrar a resolução do problema, escrevi um script Python em português
com comentários em linha e Docstrings para deixar o mais explícito possível o
funcionamento do código.

O trecho de código abaixo é a parte principal da resolução da CSP no projeto:

```python
def resolver_agendamento(eventos, num_salas=4):
    """
    Resolve o problema de agendamento de eventos em salas.
    
    Args:
        eventos (dict): Dicionário com os eventos e seus horários.
        num_salas (int): Número de salas disponíveis.
    
    Returns:
        dict: Dicionário com os eventos e seus horários nas respectivas salas.
    """
    problem = Problem()

    # Adicionando eventos como variáveis com seus domínios (salas e horários)
    for evento, horario in eventos.items():
        inicio, fim = horario
        horarios_possiveis = [
            (sala, (inicio, fim)) for sala in range(1, num_salas + 1)
        ]
        problem.addVariable(evento, horarios_possiveis)

    # Adicionando restrição de não sobreposição
    for evento1 in eventos:
        for evento2 in eventos:
            if evento1 < evento2:
                problem.addConstraint(sem_sobreposicao, (evento1, evento2))

    # Encontrando uma solução
    return problem.getSolution()
```

É fácil ver como a biblioteca simplifica a resolução de CSPs.
Para um engenheiro de software, em cenários de mundo real, o uso de bibliotecas
que agilizam o desenvolvimento e permitem que o engenheiro se concentre mais
na lógica do problema do que na implementação de algoritmos é extremamente
vantajoso.

A restrição principal do problema é que os eventos não podem ser sobrepostos.

```python
def sem_sobreposicao(evento1, evento2):
    """
    Verifica se dois eventos não estão sobrepostos.
    
    Args:
        evento1 (tuple): Tupla com o nome do evento e seu horário.
        evento2 (tuple): Tupla com o nome do evento e seu horário.
    
    Returns:
        bool: True se não há sobreposição, False caso contrário.
    """
    sala1, (inicio1, fim1) = evento1
    sala2, (inicio2, fim2) = evento2
    return sala1 != sala2 or fim1 <= inicio2 or inicio1 >= fim2
```

No [repositório do respositório do presente documento](https://github.com/fmaachadoo/artificial-intelligence-study-portfolio),
é possível encontrar o código na pasta `csp`. [[Link para a pasta do projeto]](https://github.com/fmaachadoo/artificial-intelligence-study-portfolio/tree/main/csp)

Basta executar `python main.py` para ver o resultado do script.
Utilizei `pygame` para renderizar o resultado do script em uma janela.

![Prinscreen CSP Problem](image-1.png)
![Another Prinscreen](image-2.png)

O problema lê o arquivo json mais novo na pasta do algoritmo e calcula o resultado.
Então é possível gerar novos problemas e resolver com o script.
Basta executar `python generate_events.py` para gerar um novo json com as novas
condições de eventos.
