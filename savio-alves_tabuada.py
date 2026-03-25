"""
Essa atividade visa testar seus conhecimentos acerca de estruturas de repetição.

Conceito:  O programa deve pedir um número ao usuário e mostrar a tabuada desse número 
           de 1 a 10.

Passos:

    Pedir ao usuário que digite um número.
    Usar uma estrutura de repetição (for) para contar de 1 até 10.
    A cada repetição, multiplicar o número digitado pelo contador.
    Mostrar o resultado na tela.

Sinta-se livre para adicionar funcionalidades, como por exemplo: validar a entrada do 
usuário.
"""

# Converte o número de entrada num inteiro.
numero = int(input("\nDigite um número para visualizar sua tabuada: "))

# Caso o usuário insista num número maior que 100, entrará em loop, até 
# que ele digite um número aceitável. Aqui não é permitido isso, já que, 
# estragará a formatação do resultado.
while numero >= 100:
    print("Não é permitido um número maior que 100! Tente novamente.")
    numero = int(input("Digite um número para visualizar sua tabuada: "))

# Caso ele digite números decimais(ponto flutuante). Só será válidos números
# inteiros positivos:

print(f"\n\nA tabuada do número {numero}:", end='\n\n')
for i in range(1, 10 + 1):
    # A formatação espeara resultados de apenas três dígitos.
    print(f"{numero:>10d} x {i:2d}  =  {numero * i:3d}")