saldo = 0
limite_saque = 500
saque_diario = 3
saques_realizados = 0
extrato = []

print("--- MENU DO BANCO ---")
print()

while True:
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    print()
    opcao = input("Digite uma opção: ")

    if opcao == "d":
        # Depósito
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    elif opcao == "s":
        # Saque
        if saques_realizados < saque_diario:
            valor = float(input("Digite o valor do saque: "))
            if 0 < valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque: R${valor:.2f}")
                saques_realizados += 1  # Incrementa o contador de saques
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor de saque inválido ou saldo insuficiente.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        # Extrato
        print("\n=== Extrato ===")
        if extrato:
            for transacao in extrato:
                print(transacao)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema")
        break

    else:
        print("Opção inválida. Tente novamente.")





