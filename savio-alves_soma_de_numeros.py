"""
Essa atividade visa testar seus conhecimentos acerca de estruturas de repetição.

Conceito: O programa deve somar vários números informados pelo usuário até que 
          ele digite 0, que serve para encerrar o programa.

Passos:

    Criar uma variável para guardar a soma (começando com 0).
    Repetir o processo de pedir um número ao usuário.
    Se o número for diferente de 0, somá-lo à variável.
    Se o número for 0, parar a repetição.
    Mostrar o valor total somado no final.

Sinta-se livre para adicionar funcionalidades, como por exemplo: validar a entrada 
do usuário.
"""

acumulador = 0
valor = -1

while valor != 0:
    valor = int(input("Digite um número: "))
    
    if valor < 0:
        print(f"\nVocê digitou um número negativo: {valor}. Tente novamente!\n")
        continue
    
    acumulador += valor
    
    # Apenas imprime o acumulado se o número colocada não foi zero. Assim, é evitado
    # que sai mais uma impressão a sair do programa, deixando apenas a mensagem
    # final formatada.
    if valor != 0:
        print(f"Sua soma está em {acumulador}.")

# Mensagem final de impressão.
print(f"\nSua soma total final ficou em {acumulador}.\n")