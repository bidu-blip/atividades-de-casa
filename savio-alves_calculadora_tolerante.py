"""
Essa atividade visa testar seus conhecimentos acerca de tratamento de erros.   

Conceito: Crie uma calculadora que seja tolerante a falhas, trate os erros e mostre para o usuário mensagens mais elegantes.

Passos:

    Peça ao usuário dois valores
    Converta eles para inteiro ou float.
    Faça as quatro operações aritmeticas (soma, subtração, multiplicação e divisão).
    Utilizando o except, trate os tipos de erros:
    - ValueError
    - ZeroDivisionError
    Não esqueça dos comentários no código para documentação
"""


def entrada_de_valores() -> (float, float):
    # Entradas dos valores 'A' e 'B'.
    valor_a = input("valor(A): ")
    valor_b = input("valor(B): ")
    # Verifica se a string é um valor aceitável para processamento.
    correto = (lambda s: s.isdigit() or ('.' in s and s.count('.') == 1))
    
    if not(correto(valor_a) or correto(valor_b)):
        raise ValueError("Só é aceito números inteiros ou decimais.")
    
    return (float(valor_a), float(valor_b))
    
def efetua_as_operacoes(a: float, b: float) -> list[float]:
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    
    try:
        divisao = a / b
    except ZeroDivisionError:
        print("Não foi possível efetura a divisão pois você digitou o valor B como zero.")
        divisao = None
    else:
        print("Nem problema relatado.")
    finally:
        print("Processamento realizado.")
        
    return (soma, subtracao, multiplicacao, divisao)
       
def visualizacao_dos_resultados(
    adicao: float, subtracao: float, 
    multiplicacao: float, divisao: float
    ) -> None:
    # Simbolos unicodes.
    IGUAL = '\u003d'
    # Os símbolos Unicode de soma(+), subtração(-), multiplicação(x)
    # e divisão(/), respectivamente.
    SIMBOLOS = ('\u002b', '-', '\u00d7', '\u00f7')
    
    print("\n\nA efetuação das seguintes operações:")    
    print(f"\n\t{a} {SIMBOLOS[0]} {b} {IGUAL} {adicao:5.2f}")
    print(f"\t{a} {SIMBOLOS[1]} {b} {IGUAL} {subtracao:5.2f}")
    print(f"\t{a} {SIMBOLOS[2]} {b} {IGUAL} {multiplicacao:5.1f}")
    
    if divisao is not None:
        print(f"\t{a} {SIMBOLOS[3]} {b} {IGUAL} {divisao: 5.3f}", end='\n\n')
    
# Fica em loop até as entradas corretas sejam passadas.
print("\n\n\tUma Calculadora Tolerante a Erros", end='\n\n')

while True:
    try:
        (a, b) = entrada_de_valores()
        valores = efetua_as_operacoes(a, b)
        visualizacao_dos_resultados(*valores)
        break
    except ValueError as erro:
        print(f"\n[ERROR]{erro}", end='\n\n')
        continue