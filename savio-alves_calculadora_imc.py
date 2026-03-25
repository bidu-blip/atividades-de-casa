"""
Essa atividade visa testar seus conhecimentos acerca de funções.

Conceito: Criar uma função que calcule o IMC e informe a categoria correspondente.

Passos:

    Crie uma função que receba peso e altura como parâmetros.
    Calcule o IMC coma fórmula IMC = peso / (altura ** 2).
    Use condicionais para determinar a classificação e exibir as respectivas mensagens:
    Abaixo de 18.5: "Abaixo do peso"
    Entre 18.5 e 24.9: "Peso ideal"
    Entre 25 e 29.9: "Sobrepeso"
    30 ou mais: "Obesidade"
    Retorne ou exiba uma mensagem no formato:
    "Seu IMC é 22.8 - Peso Ideal"

Sinta-se livre para adicionar funcionalidades, como por exemplo: validar a entrada do usuário.
"""

SEPARADOR = '-'
COMPRIMENTO = 55
contagem = 30

def calculo_do_imc(peso, altura):
    return peso / (altura * altura)

def realizar_classificacao(valor_imc):
    print("\nA classificação deste IMC está", end=' ')

    if valor_imc <= 18.5:
        print("Abaixo do peso.")
    elif valor_imc >= 18.5 and valor_imc <=24.9:
        print("Peso ideal.")
    elif 25 <= valor_imc <= 29.9:
        print("Sobrepeso.")
    else:
        print("Obesidade.")

def mostrar_cabecalho_do_programa():
    print(SEPARADOR * COMPRIMENTO)
    print("\t\tCálculo do seu IMC")
    print(SEPARADOR * COMPRIMENTO)

def aplicar_espacamento():
    print(f"\n{SEPARADOR * COMPRIMENTO}", end='\n\n\n')

# O contador é um mecanismo para na ficar executando o programa
# eternamente.
while contagem < 30:
    mostrar_cabecalho_do_programa()

    peso = float(input("Digite seu peso(kg): "))
    altura = float(input("Digite sua altura(m): "))

    indice = calculo_do_imc(altura=altura, peso=peso)
    realizar_classificacao(indice)
    aplicar_espacamento()

    contagem += 1
