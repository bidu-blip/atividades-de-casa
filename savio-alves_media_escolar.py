"""
Essa atividade visa testar seus conhecimentos acerca de estruturas condicionais.

Conceito: Um sistema que calcula se um aluno foi aprovado, está de recuperação ou foi reprovado com base na média das notas.

Passos:

    Defina quatro variáveis com notas de 0 a 10
    Calcule a média das notas(somar todas as notas e dividir por 4)
    Se a média for maior ou igual a 7, exibe: "Parabéns, você foi aprovado!"
    Senão, se a nota for maior ou igual a 5(mas menor do que 7), exibe: "Você está de recuperação."
    Caso contrário, deve exibir: "Que pena, você foi reprovado!"

"""

nota_1 = 7.5; nota_2 = 8.8; nota_3 = 8.7; nota_4 = 4.2
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4.0

print("\nSua média é %0.1f" % media)

if media >= 7.0:
    
    print("Parabéns, você foi aprovado.")
else:
    print("Você está de recuperação.")



