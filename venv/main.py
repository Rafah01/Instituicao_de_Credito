# Estrutura de tratamento de erro
try:
    """"def juros_composto():
        
    def  juros_simples():
    """
    #Faz o cadastro do cliente
    def cadastro():

        nome=str(input("Para começarmos, digite seu nome aqui.\n"))
        cpf=int(input("{}, agora seu CPF,apenas os números.\n".format(nome)))
        dia=int(input("{}, digite o dia em que nasceu.\n".format(nome)))
        mes = int(input("{}, digite o mês em que nasceu.\n".format(nome)))
        ano = int(input("{}, digite o ano em que nasceu.\n".format(nome)))


        return nome

    print("--------------------------------------------------------------------\n\nOlá, seja bem-vindo(a)  à nossa instituição, espero poder ajudá-lo(a)\n\n--------------------------------------------------------------------\n\n")
    dados=cadastro()
    tam=len(dados)

    for a in range(tam):
        print(dados[a])
        print("\n")
except:
    print("Algo deu errado!")
