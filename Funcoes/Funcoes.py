#inventario de equipamentos - listas, funcoes
def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento=[input("Equipamento: "),
                     float(input("Valor: ")),
                     int(input("Número Serial: ")),
                     input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite 'S' para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome........: ", elemento[0])
        print("Valor.......: ", elemento[1])
        print("Serial......: ", elemento[2])
        print("Departamento: ", elemento[3])

def localizarPorNome(lista):
    nomeEquipamento = input("Nome do equipamento: ")
    for elemento in lista:
        if nomeEquipamento == elemento[0]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])

def depreciarPorNome(lista, porc):
    depreciacao = input("Nome do equipamento: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] *= (1-porc/100)
            print("Novo valor: ", elemento[1])

def excluirPorSerial(lista):
    numSerial = int(input("Número serial do equipamento a ser excluido: "))
    for elemento in lista:
        if numSerial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos"

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
