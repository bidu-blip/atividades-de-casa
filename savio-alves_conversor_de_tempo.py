'''
Essa atividade visa testar seus conhecimentos acerca de funções.

Conceito: Criar uma função que converta segundos em horas, minutos e segundos.

Passos:

    Crie uma função que receba um número de segundos.
    Use divisão inteira e resto para encontrar quantas horas, minutos e segundos há no total.
    O resultado deve ser exibido no formato:
    "2h 15m 30s"
    Teste com diferentes valores, como 3661 (resultado esperado: "1h 1m 1s").
'''



def mostrar_cabecalho_do_programa(nome="<Insira o Nome Aqui>"):
    SEPARADOR = '-'
    COMPRIMENTO = 55

    print(SEPARADOR * COMPRIMENTO)
    print(f"\t\t{nome}")
    print(SEPARADOR * COMPRIMENTO)

def formate_o_horario_em_digital(segundos):
    hora    = segundos // 3600
    minuto  = (segundos // 60) % 60
    segundo = segundos % 60

    print(f"{hora:0>2d}:{minuto:0>2d}:{segundo:0>2d}")

def formate_o_horario_classico(segundos):
    hora      = segundos // 3600
    minuto    = (segundos // 60) % 60
    segundo   = segundos % 60

    print(f"{hora}h {minuto}min {segundo}seg")

def pular_uma_linha():
    print("")

mostrar_cabecalho_do_programa("Formatador de Tempo(seg)")
segundos = int(input("\nDigite qualquer quantia de segundos: "))

pular_uma_linha()
formate_o_horario_classico(segundos)
formate_o_horario_em_digital(segundos)