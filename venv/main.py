# Estrutura de tratamento de erro

try:
    """Funções """

    #A parti de critérios considerados, calcula a faixa salarial do cliente
    def faixa_renda():
        print("\nSua faixa de renda será especificada com base em seu salário,\ninforme-o digitando o número abaixo na faixa salarial em que se enquadra.\n")
        faixa= int(input("\n1. menos de 1 salário.\n2. Entre 1 a 2 salários.\n3. Entre 2 a 5 salários.\n4. Mais que 5 salários.\n"))
        return faixa

    #Calcula o valor total  para o imóvel

    def imovel():
        faixa=faixa_renda()
        valor=float(input("Diga-nos o valor da residência que deseja.\n"))
        meses = int(input("Em quantos meses poderá pagar tudo?"))

        if faixa>=3:
            total=juros_composto(valor,meses, 0.05)

        elif faixa==1:

            total = juros_simples(valor, meses,0.001)
        else:

            total = juros_composto(valor, meses, 0.01)

        return total

    #Calcula o valor total pra veículos

    def veiculo():
        faixa = faixa_renda()
        valor=float(input("Diga-nos o valor do veículo que deseja.\n"))
        meses = int(input("Em quantos meses poderá pagar tudo?"))

        if faixa >= 3:
            total = juros_composto(valor, meses, 0.05)

        elif faixa == 1:

            total = juros_simples(valor, meses, 0.001)
        else:

            total = juros_composto(valor, meses, 0.01)


        return total

    #Função que calcula o total do valor com juros compostos

    def juros_composto(valor,meses,taxa):
        montante= valor*((1+taxa)**meses)
        total=valor+ montante
        return total


    # Função que calcula o total do valor com juros simples

    def  juros_simples(valor, meses,taxa):

        montante=(valor*meses*taxa)
        total=valor+montante
        return total

    #Faz o cadastro do cliente, recebendo seus dados

    def cadastro():

        nome=str(input("Para começarmos, digite seu nome aqui.\n"))
        cpf=int(input("{}, agora seu CPF,apenas os números.\n".format(nome)))
        dia=int(input("{}, digite o dia em que nasceu.\n".format(nome)))
        mes = int(input("{}, digite o mês em que nasceu.\n".format(nome)))
        ano = int(input("{}, digite o ano em que nasceu.\n".format(nome)))


        return nome


    #Programa ´principal





    print("--------------------------------------------------------------------\n\nOlá, seja bem-vindo(a)  à nossa instituição, espero poder ajudá-lo(a)\n\n--------------------------------------------------------------------\n\n")

    nome=cadastro()
    print("\n{}, vamos começar? Escolha uma opção\n".format(nome))

    #Estrutura de repetição a parti da qual o programa funcionará
    while(1):
        print("\n1. Financiamento de Veículos\n2. Financiamento de Casa\n")
        decisao=int(input("Digite a opção desejada.\n"))

        if decisao==1:
            total=veiculo();
            print("O valor total a ser pago é:R$ {:.2f}".format(total))

        elif decisao==2:
            total = imovel()
            print("O valor total a ser pago é:R$ {:.2f}".format(total))
        else:
            print("Digite o número corretamente!")
            break

        while(True):
            continua=str(input("\nDeseja continuar? Digite sim, se não quiser, digite nao.\n"))

            if(continua=="sim"):
                continue
            elif continua=="nao":
                print("\nAté mais!\n")
                break
            else:
                print("\nDigite corretamente o dado acima.\n")

except:
    print("Algo deu errado! Tente novamente")
