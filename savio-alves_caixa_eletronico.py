"""
Essa atividade visa testar seus conhecimentos acerca de estruturas condicionais.

Conceito: Um programa que sabe quanto "saldo" você tem em uma conta. Você diz quanto quer gastar, e o programa decide se a compra é aprovada ou negada.

Passos:

    Defina uma variável com o saldo disponível
    Pergunte ao usuário qual o valor da compra que ele deseja fazer
    Caso não saiba como "Perguntar ao usuário", defina uma variável com o valor da compra.
    Se o valor da compra for menor ou igual ao saldo, o programa deve exibir: "Compra aprovada! Obrigado."
    Caso contrário, deve exibir: "Saldo insuficiente, compra negada!"
"""

saldo = 300

while True:
    try:
        valor = float(input("Qual o valor da compra: "))
    except ValueError:
        print("\nSão aceitos apenas dígitos!")
        continue
    else: pass
    finally: pass

    if valor <= saldo:
        print("Compra aprovada!")
        saldo -= valor
    else:
        print("Saldo ineficiente, compra negada!")