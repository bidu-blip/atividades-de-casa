'''
Essa atividade visa testar seus conhecimentos acerca de funções.

Conceito: Criar uma função que repete uma mensagem várias vezes.

Passos:

    Defina uma função que receba uma mensagem e um número de repetições.
    Dentro da função, use uma estrutura de repetição para mostrar a mensagem várias vezes.
    O programa deve exibir a mesma frase repetida conforme o número informado.
    Teste com diferentes mensagens e valores (ex: 3 -> a mensagem aparece 3 vezes).
'''


SEPARADOR = '-'
COMPRIMENTO = 55

def mostrar_cabecalho_do_programa(nome="<Insira o Nome Aqui>"):
    print(SEPARADOR * COMPRIMENTO)
    print(f"\t\t{nome}")
    print(SEPARADOR * COMPRIMENTO)

def camara_de_eco(quantidade, mensagem="Margens Plácidas"):
    print("") # Quebra-de-linha padrão.

    for contagem in range(quantidade):
        print(f"\t{contagem + 1:>3}ª. {mensagem}")



mostrar_cabecalho_do_programa("Câmara de Eco")

mensagem = input("\nDigite uma mensagem: ")
quantidade = int(input("Repetir quantas vezes: "))

camara_de_eco(quantidade, mensagem)
