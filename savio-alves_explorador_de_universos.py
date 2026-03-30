"""
Essa atividade visa testar seus conhecimentos acerca de requisições encadeadas e navegação 
em listas de dados.   

Conceito: Baseado no roteiro visto em aula, crie um programa que busca informações sobre um
Planeta específico da saga Star Wars.

Passos:

    Peça ao usuário para digitar o ID de um planeta (um número de 1 a 60).
    Acesse a URL: https://swapi.dev/api/planets/{ID}/.
    Extraia e exiba as seguintes chaves do JSON:
    Nome do planeta (name).
    Clima (climate).
    População (population).

Desafio: Verifique a chave residents. Se a lista de residentes estiver vazia, exiba 
"Este planeta não possui habitantes conhecidos". 

Caso contrário, exiba "Este planeta possui [X] residentes registrados".

Trate possíveis erros caso o usuário digite um ID que não existe (ex: Planeta 999).
"""

import requests
from pprint import (pprint as PPrint)

def criar_cabecalho(titulo) -> None:
    import shutil
    
    comprimento = len(titulo)
    LARGURA_TELA = shutil.get_terminal_size().columns - 5
    qtd_tracos = (LARGURA_TELA - comprimento) // 2
    barra = '-' * qtd_tracos
    
    print(f"\n{barra} {titulo} {barra}\n")
    del shutil

def compoe_uma_url(id: int) -> str:
    DOMINIO     = "swapi.dev"
    PROTOCOLO   = "https"
    ENDPOINT    = "/api/planets/"
    
    return f"{PROTOCOLO}://{DOMINIO}{ENDPOINT}{id}/"

def obtem_o_json(ID: int) -> dict:
    url        = compoe_uma_url(ID)
    resposta   = requests.get(url)
    data_json  = resposta.json()
    
    if resposta.status_code != 200:
        print("Erro ao pedir dados sobre o ID dado.")
    return data_json

def informacao_do_planeta(data: dict, ID: int) -> None:
    nome = data['name']
    populacao = data['population']
    clima = data['climate']
    
    print(f"""
        \rPlaneta {nome}({ID}):
        \r\t- População: {populacao}
        \r\t- Clima: {clima}
    """)

def execucao_do_programa() -> None:    
    # Visualização do cabeçalho do programa.
    criar_cabecalho("Buscador de Planetas do StarWars")

    # Entrada de texto, apenas aceito números, especialmente no range de um à sessenta. Então
    # realiza a conversão.
    entrada = input("Digite o 'id' do planeta(1 à 60): ")
    identidade = int(entrada)

    # Verifica se a instrução foi seguida. Um número limitado de 1 à 60. Se sim, ele vai na cadeia
    # de impressão da informação. Caso não, ele apenas termina o programa e informa o erro.
    if 1 <= int(entrada) <= 60:
        info_data  = obtem_o_json(identidade)
        
        # Verificando se o JSON retornado está bem, ou seja, tem os campos necessários para 
        # impressão. Se não houver, ele termina o programa com mensagens diferente dependendo
        # do tipo de erro, que foi verificado.
        if "name" in info_data and "climate" in info_data and "population" in info_data:
            informacao_do_planeta(info_data, identidade)
        else:
            print("O número deste planeta ainda não está bem formado!")
    else:
        
        print(f"\nVocê digitou {entrada}. É um valor incompátivel! Apenas de 1 á 60.\n")
    

execucao_do_programa()