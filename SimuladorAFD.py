
K =[] # Conjunto de estados

V =[] # Alfabeto

T= [] # Transições

i = ""  # Estado Inicial

F = [] # Estado Final

delta = {} # Dicionario de Transição

escolha = 0

def processar_afd(cadeia, estado_inicial, estados_finais, delta):
    estado_atual = estado_inicial
    
    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False
    
    return estado_atual in estados_finais

escolha = input("Digite 0 para testar manualmente ou qualquer outro valor para teste automatico com valores pré definidos: ")

if escolha == "0":
    K = list((input("Digite o Conjunto de Estados(K) da linguagem separados por espaço (Exemplo: q0 q1 q2): ").split()))

    V = list((input("Digite o Alfabeto(V) separados por espaço: (Exemplo: a b): ").split()))

    while True:
        i = input("Digite o Inicio(i) do AFD:")
        F = list((input("Digite os Finais(F) do AFD separados por espaço (Exemplo: q2 q3): ").split()))
        if i in K and all(f in K for f in F):
            break
        else:
            print("Digite valores corretos para inicio e fim")

    entrada = input("Digite todas as Transições(T) (origem símbolo destino) separadas por espaço (Exemplo: q0 a q1 q0 b q2): ")
    valores = entrada.split()

    T = [tuple(valores[i:i+3]) for i in range(0, len(valores), 3)]

else:
    K = ["q0", "q1", "q2", "q3"]

    V =["a","b"]

    i = "q0"

    F = ["q3"]

    T = [
        ("q0", "a", "q1"),
        ("q0", "b", "q2"),
        ("q1", "a", "q0"),
        ("q1", "b", "q3"),
        ("q2", "a", "q3"),
        ("q2", "b", "q0"),
        ("q3", "a", "q2"),
        ("q3", "b", "q1")
    ]

for origem, simbolo, destino in T:
    delta[(origem, simbolo)] = destino

print(f"Conjunto de Estados: {K}\nAlfabeto: {V}\nEstado Inicial: {i}\nEstados Finais: {F}\nTransições: {T}")
while True:
    cadeia = input("Digite a cadeia para testar (ou 'sair' para encerrar): ")
    if cadeia.lower() == 'sair':
        break
    if processar_afd(cadeia, i, F, delta):
        print("Cadeia aceita!")
    else:
        print("Cadeia rejeitada!")





