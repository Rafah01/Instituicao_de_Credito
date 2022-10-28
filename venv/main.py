# Estrutura de tratamento de erro

try:

    #Pega a faixa salarial do cliente
    def faixa_renda():
        print("\nSua faixa de renda será especificada com base em seu salário,\ninforme-o digitando o número abaixo na faixa salarial em que se enquadra.\n")
        faixa= int(input("\n1. menos de 1 salário.\n2. Entre 1 a 2 salários.\n3. Entre 2 a 5 salários.\n4. Mais que 5 salários.\n"))
        return faixa

    #valor total  pra casa
    def casa():
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

    #valor total pra veículos
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

    def juros_composto(valor,meses,taxa):
        montante= valor*((1+taxa)**meses)
        total=valor+ montante
        return total

    def  juros_simples(valor, meses,taxa):

        montante=(valor*meses*taxa)
        total=valor+montante
        return total

    #Faz o cadastro do cliente

    def cadastro():

        nome=str(input("Para começarmos, digite seu nome aqui.\n"))
        cpf=int(input("{}, agora seu CPF,apenas os números.\n".format(nome)))
        dia=int(input("{}, digite o dia em que nasceu.\n".format(nome)))
        mes = int(input("{}, digite o mês em que nasceu.\n".format(nome)))
        ano = int(input("{}, digite o ano em que nasceu.\n".format(nome)))


        return nome


    #main





    print("--------------------------------------------------------------------\n\nOlá, seja bem-vindo(a)  à nossa instituição, espero poder ajudá-lo(a)\n\n--------------------------------------------------------------------\n\n")

    nome=cadastro()
    print("\n{}, vamos começar? Escolha uma opção\n".format(nome))
    while(1):
        print("\n1. Financiamento de Veículos\n2. Financiamento de Casa\n")
        decisao=int(input("Digite a opção desejada.\n"))

        if decisao==1:
            total=veiculo();
            print("O valor total a ser pago é:R$ {:.2f}".format(total))

        elif decisao==2:
            total = casa()
            print("O valor total a ser pago é:R$ {:.2f}".format(total))
        else:
            print("Digite o número corretamente!")
            break


        continua=str(input("\nDeseja continuar? Digite sim, se não quiser, digite nao.\n"))

        if(continua=="sim"):
            continue
        elif continua=="nao":
            print("Até mais!")
            break
        else:
            print("animal, digita corretamente!!!!")

except:
    print("Algo deu errado! Tente novamente")
