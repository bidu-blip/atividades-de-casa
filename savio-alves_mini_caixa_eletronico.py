'''
Essa atividade visa testar seus conhecimentos acerca de estruturas de repetição.

Conceito: O programa deve receber um valor de saque e mostrar quantas notas de cada tipo (50, 20, 10, 5 e 2) serão entregues.

Passos:
    Pedir ao usuário um valor de saque (inteiro)
    Crie uma lista com as notas disponiveis (maiores primeiro)
    Para cada nota:
    Comece o contador dessa nota em 0
    Enquanto o valor restante for maior ou igual à nota, subtraia a nota do valor e aumente o contador.
    Ao terminar, imprima quantas notas daquela face serão usadas.

Sinta-se livre para adicionar funcionalidades, como por exemplo: validar a entrada 
do usuário.
'''

saque = int(input("\nQual é o valor do saque: "))
# Notas possíveis de se dividir do dinheiro.
notas = (50, 20, 10, 5, 2)
# Contadores de cada nota retidadas.
quantias = {2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 1: 0}
cursor = 0

# Algoritmo: Enquanto o saque não for zero, subtrair uma ordem de notas. Em cada
#            subtração, registrar a nota subtraida nos seus respectivos contadores.
#            Quando esgotar a quantia de notas que subtrair, parte para outra na 
#            lista/tupla.
#           
#            Obs.: Ele não funciona com todos os números. Acho que por causa da falta
#            de um real.
while saque > 0:
    if __debug__:
        print(f"cursor: {cursor}")
        
    nota = notas[cursor]
    
    if __debug__:
        print(f"saque: {saque}")
        print(quantias)
        print(f"nota: {nota}")
        print(f"cursor: {cursor}")
    
    
    if saque >= nota:
        quantias[nota] += 1
        saque -= nota
    else:
        cursor += 1

print("\nO saque ficou em:")
for (nota, unidades) in quantias.items():
    if unidades == 0:
        continue
    print(f"\tNota de R${nota:>3},00: {unidades:>4d} unidades")
    