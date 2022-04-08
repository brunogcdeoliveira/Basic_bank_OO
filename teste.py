def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    print("Conta criada com sucesso")
    return conta

conta1 = cria_conta(123, "Bruno", 100.50, 200.99)
conta2 = cria_conta(123, "Bruno", 100.50, 200.99)

conta_selecionada = int(input("Selecione um numero de conta: "))

if(conta_selecionada == conta1["numero"]):
    print("Titular: {}".format(conta1["titular"]))