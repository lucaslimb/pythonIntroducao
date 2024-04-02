from Funcoes.Funcoes import *

lista = []

print("Preenchendo")
preencherInventario(lista)
print("")

print("Exibindo")
exibirInventario(lista)
print("")

print("Pesquisando")
localizarPorNome(lista)
print("")

print("Alterando")
depreciarPorNome(lista, 20)
print("")

print("Excluindo")
excluirPorSerial(lista)
print("")
exibirInventario(lista)

print("Resumindo")
resumirValores(lista)