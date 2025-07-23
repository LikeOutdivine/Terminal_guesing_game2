import random
import os
import time

# Configuração
largura = 20
altura = 10
jogador = {'x': largura // 2, 'y': altura // 2, 'tamanho': 1}
bolinhas = []

def gerar_bolinhas():
    while len(bolinhas) < 5:
        tipo = random.choice([1, 5])
        bolinhas.append({
            'x': random.randint(0, largura - 1),
            'y': random.randint(0, altura - 1),
            'tipo': tipo
        })

def desenhar():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(altura):
        linha = ""
        for x in range(largura):
            if jogador['x'] == x and jogador['y'] == y:
                linha += "O"
            elif any(b['x'] == x and b['y'] == y for b in bolinhas):
                for b in bolinhas:
                    if b['x'] == x and b['y'] == y:
                        linha += "+" if b['tipo'] == 1 else "*"
                        break
            else:
                linha += "."
        print(linha)
    print(f"Tamanho da bola: {jogador['tamanho']}")

def mover(direcao):
    if direcao == "w" and jogador['y'] > 0:
        jogador['y'] -= 1
    elif direcao == "s" and jogador['y'] < altura - 1:
        jogador['y'] += 1
    elif direcao == "a" and jogador['x'] > 0:
        jogador['x'] -= 1
    elif direcao == "d" and jogador['x'] < largura - 1:
        jogador['x'] += 1

def verificar_colisao():
    global bolinhas
    novas = []
    for b in bolinhas:
        if b['x'] == jogador['x'] and b['y'] == jogador['y']:
            jogador['tamanho'] += b['tipo']
        else:
            novas.append(b)
    bolinhas[:] = novas

# Loop principal
gerar_bolinhas()
while True:
    desenhar()
    comando = input("Mover (w/a/s/d ou q para sair): ").lower()
    if comando == "q":
        break
    mover(comando)
    verificar_colisao()
    gerar_bolinhas()