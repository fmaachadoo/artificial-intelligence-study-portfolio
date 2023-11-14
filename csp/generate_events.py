import json
import random
import time

PREFIXOS = [
    "Gerenciamento de",
    "Introdução a",
    "Fundamentos de",
    "Técnicas de",
    "Aplicações de",
    "Desenvolvimento de",
]

SUFIXOS = [
    "Dados Alienigenas",
    "Inteligência Artificial",
    "Tiktok",
    "Influenciamento Digital",
    "Post-Ironic Memes",
    "Cancelamento no Twitter",
    "Reprodução Humana",
]

# Gerando 25 eventos fictícios
num_salas = 4
num_eventos = 25
eventos = {}

for i in range(num_eventos):
    nome_evento = (
        f"{PREFIXOS[random.randint(0, len(PREFIXOS) - 1)]} "
        f"{SUFIXOS[random.randint(0, len(SUFIXOS) - 1)]}"
    )
    inicio = random.randint(8, 16)  # Escolhe uma hora de início entre 8h e 16h
    duracao = random.randint(1, 3)  # Duração de 1 a 3 horas
    fim = inicio + duracao
    fim = min(fim, 18)  # Garante que não passe das 18h
    eventos[nome_evento] = (inicio, fim)


actual_timestamp = int(time.time())

# Salvando os eventos em um arquivo JSON
with open(f"eventos_{actual_timestamp}.json", "w") as f:
    json.dump(eventos, f, indent=4)
