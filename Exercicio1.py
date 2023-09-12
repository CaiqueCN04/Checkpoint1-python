estoque= {}

while True:
    programa = int(input(' 0 - Para encerrar programa \n 1 - Para adicionar item ao estoque \n 2 - Para vizualizar estoque \n 3 - Para remover item \n 4 - Para atualizar estoque\n Digite aqui sua escolha: '))
    if programa == 1 :
        nome = input('Digite o nome do produto: ')
        if not nome.replace(" ","").isalpha():
            print("O nome deve conter apenas letras, tente novamente.")
        valor = float(input('Digite o valor do produto: '))
        quantidade= int(input('Digite a quantidade do estoque: '))
        estoque[nome]= {'valor R$':valor , 'quantidade':quantidade}
        print(estoque) 
    elif programa== 2:
        print(estoque)
    elif programa == 3:
        cancela_item = input('Digite o produto a ser cancelado: ')
        if cancela_item in estoque:
            del estoque[cancela_item]
        else:
            print('Este produto não está no estoque') 
    elif programa == 4:
        nome=input('Digite o nome do produto que deseja atualizar: ')
        if nome in estoque:
            valor = float(input("Digite o novo preço do produto: "))
            quantidade = int(input("Digite a nova quantidade em estoque: "))
            estoque[nome]= {'valor R$':valor , 'quantidade':quantidade}           
            print(f'As informações do produto {nome} foram atualizadas.')
        else:
            print(f'O item {nome} não esta na lista')
    else:
       print(f'Estoque: {estoque}')
       print('Programa encerrado')
       break 
