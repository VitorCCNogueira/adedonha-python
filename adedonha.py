import random
alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
adedonha_tabela = ["nome", "objeto", "lugar","cor", "fruta"]

def mostrar_nomes():
    print(*adedonha_tabela)


def leitor_resp():
    resp = int(input("Informe 0 para parar, 1 para pedir ajuda e 2 para iniciar partida:"))
    return resp


pontos = 0
def identificacao(tipo, texto):  
    with open (f"Adedonha/{tipo}.txt", 'r', encoding="utf-8") as identificacao_tipo:   
        linhas = identificacao_tipo.readlines()
        linhas = [linha.strip().upper() for linha in linhas]
        if texto.upper().strip() not in linhas: 
            return False
        else:
            return True


def placar(nome, objeto, lugar, cor, fruta, letra):
    pontos = 0
    if nome and nome[0].upper() == letra and identificacao("pessoas", nome):
        pontos += 1
    if objeto and objeto[0].upper() == letra and identificacao("objetos", objeto):
        pontos += 1
    if lugar and lugar[0].upper() == letra and identificacao("lugares", lugar):
        pontos += 1
    if cor and cor[0].upper() == letra and identificacao("cores", cor):
        pontos += 1
    if fruta and fruta[0].upper() == letra and identificacao("frutos", fruta):
        pontos += 1
    print("Pontos da rodada:", pontos)
    return pontos


while True:
    resp = leitor_resp()

    if resp == 0:
        break
    elif resp == 1:
        mostrar_nomes()
    elif resp == 2:
        letra = random.choice(alfabeto)
        print(f"A letra sorteada foi {letra}")
        print("nome, objeto, lugar, cor, fruta")
        try:
            nome, objeto, lugar, cor, fruta = [
            item.strip() for item in input().split(",")
            ]
            pontos += placar(nome, objeto,  lugar, cor, fruta, letra)
        except ValueError:
            print("Você esqueceu de algum. Caso não saiba, deixe espaço vazio")
    else:
        print("Opção inválida.")
if pontos>0:
    print(f"O placar foi {pontos}")