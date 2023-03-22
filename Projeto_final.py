#projeto Lanchete 
#autor anderson brito de lima 
import sys
from tinydb import TinyDB, Query

db = TinyDB('BancodeDados.json')
tableClient = db.table('Clientes')
tableProduct = db.table('Produtos')
tableOrder = db.table('Pedidos')
User = Query()

#informações clientes

def updateClientesPhone(name, newPhone):
    tableClient.update({'Telefone': newPhone}, User.Nome == name)

def deleteClientes(name):
    tableClient.remove(User.Nome == name)

def insertClientes(name, phone):
    tableClient.insert({'Nome': name, 'Telefone': phone})

def searchClientes(name):
    result = tableClient.search(User.Nome == name)
    print(result)

def updateClientes(name, newName):
    tableClient.update({'Nome': newName}, User.Nome == name)


# Produtos 
def deleteProdutos(name):
    tableProduct.remove(User.Nome == name)

def updateProdutos(name, newName):
    tableProduct.update({'Nome': newName}, User.Nome == name)

def updateProdutosPrice(name, newPrice):
    tableProduct.update({'PreçoUnitario': newPrice}, User.Nome == name)

def insertProdutos(name, price):
    tableProduct.insert({'Nome': name, 'PreçoUnitario': price})

def searchProdutos(name):
    result = tableProduct.search(User.Nome == name)
    print(result)

# Banco Pedidos



def updatePedido(name, orderprod, orderprodNumber):
    tableOrder.update({'Produto': orderprod, 'Quantidade': orderprodNumber}, User.Cliente == name, )


def deletePedido(name):
    tableOrder.remove(User.Nome == name)

def insertPedido(name, orderprod, orderprodNumber):
    tableOrder.insert({'Cliente': name, 'Produto': orderprod, 'Quantidade': orderprodNumber})

def searchPedido(name):
    result = tableOrder.search(User.Cliente == name)
    print(result)

def valorTotalPorCliente(name):
    tableOrder = db.table('tableOrder')
    orders = tableOrder.search(Query().Cliente == name)
    total = 0
    for order in orders:
        product = order['Produto']
        quantity = order['Quantidade']
        price = tableProduct.search(Query().Produto == product)[0]['Preco']
        total += price * quantity
    return total

def quantidadeTotalPorProduto():
    tableOrder = db.table('tableOrder')
    orders = tableOrder.all()
    quantities = {}
    for order in orders:
        product = order['Produto']
        quantity = order['Quantidade']
        if product in quantities:
            quantities[product] += quantity
        else:
            quantities[product] = quantity
    return quantities

def valorTotalFaturado():
    tableOrder = db.table('tableOrder')
    orders = tableOrder.all()
    total = 0
    for order in orders:
        product = order['Produto']
        quantity = order['Quantidade']
        price = tableProduct.search(Query().Produto == product)[0]['Preco']
        total += price * quantity
    return total

# final 
isEnd = 0

while isEnd == 0:
    print("Lanches Da Quarentena ")
    optionStart = int(input(" 1 Novo Pedido\n 2 Banco de dados\n 3 Listas\n 4 Finalizar\n"))
    # cria um pedido usando nome do cliente e vai adicinando valores de nome do produto e preço em uma lista
    if optionStart == 1:
        nome = input("Nome do Cliente: ")
        prodlist = []
        quantlist = []
        listend = 0
        i = 0
        while listend < 1:
            prodlist.insert(i, input("Nome do produto: "))
            quantlist.insert(i, input("Quantidade de produtos: "))
            listend = int(input("0 Adicionar mais produtos\n1 Sair\n"))
            i += 1
        insertPedido(nome, prodlist, quantlist)
    # Banco de Dados
    elif optionStart == 2:
        option = 0
        while option != 4:
            option = int(
                input("Selecione uma opção:\n1 Clintes\n2 Produtos\n3 Pedidos\n4 Voltar\n "))
            # Start Cliente
            if option == 1:
                optionCliente = 0
                while optionCliente != 5:
                    optionCliente = int(input(" 1 Adicionar Cliente\n2 Procurar Informação de clientes\n"
                                              "3 Atualizar ""Informação de clientes\n 4 Deletar Cliente\n"
                                              "5 Voltar\n"))
                    if optionCliente == 1:
                        nome = input("Nome do Cliente: ")
                        phone = input("Telefone do Cliente: ")
                        insertClientes(nome, phone)
                    elif optionCliente == 2:
                        nome = input("Nome do Cliente: ")
                        searchClientes(nome)
                    elif optionCliente == 3:
                        optionUpdate = int(input("1 Atualizar Nome\n 2 Atualizar Telefone\n 3 Voltar\n"))
                        if optionUpdate == 1:
                            nomeAtual = input("Nome atual a ser Atualizado: ")
                            newName = input("Novo Nome: ")
                            updateClientes(nomeAtual, newName)
                        elif optionUpdate == 2:
                            nomeAtual = input("Nome do cliente a ser Atualizado: ")
                            newPhone = input("Novo telefone: ")
                            updateClientesPhone(nomeAtual, newPhone)
                        else:
                            continue
                    elif optionCliente == 4:
                        name = input("Nome do Cliente a ser Deletado")
                        deleteClientes(name)
                    else:
                        optionCliente = 5
            #  Fim cliente

            # Start Produto 
            elif option == 2:
                optionProduto = 0
                while optionProduto != 4:
                    optionProduto = int(input("1 Adicionar Produto\n 2 Atualizar Informação de Produto\n "
                                              "3 Deletar Produto\n4 Voltar\n"))
                    if optionProduto == 1:
                        nome = input("Nome do Produto: ")
                        price = input("Preço do Produto: ")
                        insertProdutos(nome, price)

                    elif optionProduto == 2:
                        optionUpdate = int(
                            input("1 Atualizar Nome do Produto\n2 Atualizar Preço do Produto\n"
                                  "3 Voltar\n"))
                        if optionUpdate == 1:
                            prodAtual = input("Produto atual a ser Atualizado: ")
                            newprod = input("Novo Produto: ")
                            updateClientes(prodAtual, newprod)

                        elif optionUpdate == 2:
                            prodAtual = input("Nome do produto a ser Atualizado: ")
                            newPrice = input("Novo preço: ")
                            updateClientesPhone(prodAtual, newPrice)
                        else:
                            continue
                    elif optionProduto == 3:
                        prod = input("Nome do Produto a ser Deletado")
                        deleteClientes(prod)
                    else:
                        optionProduto = 4
            # ---- End Produto ----

            # ---- Start Pedido ----
            elif option == 3:
                optionPedido = 0
                while optionPedido != 3:
                    optionPedido = int(input("1 Atualizar Informação de Pedido\n"
                                             "2Deletar Produto\n3 Voltar\n"))
                    if optionPedido == 1:
                        optionUpdate = int(input("1 Atualizar Pedido\n 2 Sair\n"))
                        if optionUpdate == 1:
                            orderAtual = input("Pedido atual a ser Atualizado(Usar nome do Cliente): ")
                            prodlist = []
                            quantlist = []
                            listend = 0
                            i = 0
                            while listend < 1:
                                prodlist.insert(i, input("Nome do produto: "))
                                quantlist.insert(i, input("Quantidade do produto: "))
                                listend = int(input("0 Adicionar mais produtos\n 1 Sair\n"))
                                i += 1
                            updatePedido(orderAtual, prodlist, quantlist)
                        else:
                            continue
                    elif optionPedido == 2:
                        orderclient = input("Nome do Cliente a ter o pedido Deletado")
                        deletePedido(orderclient)
                    else:
                        optionPedido = 3
            #Fim Pedido 
    # Listas e logicas de negocio
    elif optionStart == 3:
        option = 0
        while option != 6:
            option = int(input("1 Listar Clientes\n 2 Listar Produtos\n 3 Valor total de produtos por "
                               "cliente\n 4 quantidade total de pedidos para cada produto\n 5 Valor total "
                               "Faturado\n 6 Sair\n"))
            if option == 1:
                print(tableClient.all())
            elif option == 2:
                print(tableProduct.all())
            elif option == 3:
                name = input("Digite o nome do cliente: ")
                total = valorTotalPorCliente(name)
                print(f"O valor total dos produtos comprados por {name} é R${total:.2f}")
            elif option == 4:
                print("Digite o nome do produto")
                total = quantidadeTotalPorProduto()
            elif option == 5:
                total = valorTotalFaturado()
                print(f"O valor total faturado é R${total:.2f}")
            else:
                continue
    elif optionStart == 4:
        sys.exit()
