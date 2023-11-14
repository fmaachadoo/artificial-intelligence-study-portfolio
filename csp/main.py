import random
import os
import json
import sys

from constraint import Problem
from pprint import pprint
import pygame


X_SCALE = 95


def encontrar_arquivo_json_mais_recente(diretorio):
    """
    Encontra o arquivo JSON mais recente em um diretório.
    
    Args:
        diretorio (str): Diretório onde os arquivos JSON estão.
        
    Returns:
        str: Nome do arquivo JSON mais recente.
    """
    # Lista todos os arquivos no diretório e filtra por arquivos .json
    arquivos_json = [
        arquivo
        for arquivo in os.listdir(diretorio)
        if arquivo.endswith(".json")
    ]

    # Ordena os arquivos pela data de modificação (do mais recente para o mais antigo)
    arquivos_json.sort(
        key=lambda x: os.path.getmtime(os.path.join(diretorio, x)),
        reverse=True,
    )

    # Retorna o arquivo mais recente
    return arquivos_json[0] if arquivos_json else None


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


def quebrar_texto(texto, fonte, max_largura):
    """
    Quebra o texto em várias linhas para que caiba na largura máxima 
    especificada.
    
    Args:
        texto (str): Texto a ser quebrado.
        fonte (pygame.font.Font): Fonte do texto.
        max_largura (int): Largura máxima da linha.
    
    Returns:
        list: Lista de strings com o texto quebrado em várias linhas.    
    """
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste_linha = linha_atual + palavra + " "
        if fonte.size(teste_linha)[0] <= max_largura:
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)

    return linhas


def desenhar_linha_tempo(tela, eventos, num_salas=4):
    """
    Desenha a linha do tempo na tela.
    
    Args:
        tela (pygame.Surface): Superfície da janela.
        eventos (dict): Dicionário com os eventos e seus horários.
        num_salas (int): Número de salas disponíveis.
    
    Returns:
        None
    """    
    altura_offset = altura * 0.1
    tela.fill(branco)
    altura_sala = (altura - altura_offset) // num_salas
    espacamento = 5

    for sala in range(1, num_salas + 1):
        # Adiciona nome da sala na lateral
        fonte_sala = pygame.font.Font(None, 20)
        texto_sala = fonte_sala.render(f"Sala {sala}", True, preto)
        tela.blit(
            texto_sala,
            (5, (sala - 1) * altura_sala + altura_offset + (altura_sala / 2)),
        )

    # Desenhando as linhas horárias
    for hora in range(7, 20):
        pygame.draw.line(
            tela,
            cinza,
            ((hora - 7) * X_SCALE, 0),
            ((hora - 7) * X_SCALE, altura),
            1,
        )
        fonte_hora = pygame.font.Font(None, 20)
        texto_hora = fonte_hora.render(f"{hora}:00", True, preto)
        tela.blit(texto_hora, ((hora - 7) * X_SCALE + 5, 5))

    # Desenhando os eventos
    for evento, (sala, (inicio, fim)) in eventos.items():
        cor = cores[sala % len(cores)]
        largura_evento = (fim - inicio) * X_SCALE - espacamento
        retangulo_evento = (
            (inicio - 7) * X_SCALE + espacamento / 2,
            (sala - 1) * altura_sala + altura_offset + espacamento / 2,
            largura_evento,
            altura_sala - espacamento,
        )
        pygame.draw.rect(tela, cor, retangulo_evento)

        fonte = pygame.font.Font(None, 20)
        titulos = quebrar_texto(
            evento, fonte, max_largura=altura_sala - (altura_sala * 0.2)
        )

        linha = 0
        for titulo in titulos:
            texto = fonte.render(titulo, True, preto)
            texto_rotacionado = pygame.transform.rotate(texto, 90)
            posicao_linha = 24 * linha
            tela.blit(
                texto_rotacionado,
                (
                    retangulo_evento[0] + posicao_linha + 10,
                    retangulo_evento[1] + 5,
                ),
            )
            linha += 1


if __name__ == "__main__":
    # Define numero de salas e diretorio dos arquivos JSON
    num_salas = 4
    diretorio_json = "."

    # Encontra o arquivo JSON mais recente
    arquivo_json_mais_recente = encontrar_arquivo_json_mais_recente(
        diretorio_json
    )
    caminho_arquivo_json = (
        os.path.join(diretorio_json, arquivo_json_mais_recente)
        if arquivo_json_mais_recente
        else None
    )

    # Lendo o arquivo JSON e carregando os eventos
    if caminho_arquivo_json:
        with open(caminho_arquivo_json, "r") as f:
            eventos_dict = json.load(f)
        pprint(eventos_dict)
    else:
        print("Nenhum arquivo JSON encontrado.")

    # Resolvendo o problema de agendamento
    solucao = resolver_agendamento(eventos_dict, num_salas=num_salas)

    # Dados dos eventos
    eventos = solucao

    # Inicializando Pygame
    pygame.init()

    # Configurações da janela
    largura, altura = 1250, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Linha do Tempo das Salas")

    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    cinza = (200, 200, 200)
    cores = [(118, 215, 196), (93, 173, 226), (174, 214, 241), (247, 220, 111)]

    # Loop principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        desenhar_linha_tempo(tela, eventos)
        pygame.display.flip()
