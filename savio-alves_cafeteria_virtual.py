"""
Essa atividade visa testar seus conhecimentos acerca de estruturas condicionais.

Conceito: 

Um programa que pergunta ao cliente o que ele deseja beber e informa o preço e uma mensagem correspondente.
  
Passos:

    Exiba um mini-menu: "Bem-vindo! O que deseja hoje? Temos 'cafe', 'cha' ou 'chocolate'."
    Peça ao usuário para digitar sua escolha.
    Se a escolha for "cafe", exiba: "Um café expresso saindo! Fica R$ 5,00."  
    Senão, se a escolha for "cha", exiba: "Ótima escolha! Seu chá de camomila fica R$ 6,00."  
    Senão, se a escolha for "chocolate", exiba: "Preparando seu chocolate quente cremoso! Fica R$ 8,00."
    Caso contrário, exiba: "Desculpe, não temos essa opção no menu hoje."  
"""

MENU = {
    "café": 5.00,
    "chá": 6.00,
    "chocolate": 8.00
}

while True:
    escolha = input("\nBem-vido! O que deseja hoje? Temos 'cafe', 'cha' ou 'chocolate'.\n -->\t")

    if escolha.lower() in ("café", "cafe"):
        print("\nUm café expresso saindo! Fica R${:0.2f}.".format(MENU["café"]))
    elif escolha.lower() in ("cha", "chá"):
        print("\nÓtima escolha! Seu chá de camomila fica em R${:0.2f}.".format(MENU["chá"]))
    elif escolha.lower() == "chocolate":
        print("\nPreparando seu chocolate quente cremoso,... fica R${:0.2f}.".format(MENU["chocolate"]))
    else:
        print("Desculpe, não temos essa opção no menu!")