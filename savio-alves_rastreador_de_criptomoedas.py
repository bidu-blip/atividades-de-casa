"""
Essa atividade visa testar seus conhecimentos acerca de requisições HTTP e manipulação 
de dicionários.  

Conceito: 

Um programa que consulta o valor atual do Bitcoin (ou outra criptomoeda) em Reais e informa 
ao usuário quanto ele teria se comprasse uma fração da moeda.

Passos:

    Utilize a API da AwesomeAPI: https://economia.awesomeapi.com.br/json/last/BTC-BRL.
    Realize a requisição e acesse o preço de compra (chave bid) dentro do dicionário 
    retornado.
    Lembre-se que o valor da API vem como string, você deve convertê-lo para float.
    Pergunte ao usuário: "Quanto você deseja investir em Bitcoin (R$)?".
    Calcule a quantidade de Bitcoin que ele compraria: investimento / preco_btc.
    Exiba o resultado: "Com R$ [valor], você compraria [quantidade] BTC hoje." 
    (use 8 casas decimais para o Bitcoin).
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


def compoe_uma_url() -> str:
    DOMINIO     = "economia.awesomeapi.com.br"
    PROTOCOLO   = "https"
    ENDPOINT    = "/json/last/BTC-BRL"
    
    return f"{PROTOCOLO}://{DOMINIO}{ENDPOINT}"

def obtem_o_json() -> str:
    "Pega apenas a parte referente em Real/Bitcoin."
    retorno = requests.get(compoe_uma_url())
    return retorno.json()["BTCBRL"]

def preco_de_um_bitcoin_em_reais() -> float:
    "Já entrega a ração de reais por bitcoin."
    return float(obtem_o_json()["bid"])

def valor_de_investimento() -> float:
    "Prompt para informar valor em real."
    return float(input("Digite o valor de compra(R$): "))

# Mostra um cabeçalho para o programa de 'casa de câmbio'.
criar_cabecalho("Casa de Câmbio de Bitcoin(BTC/R$)")

# Obtenção de valor ...
investido = valor_de_investimento()
# Processamento das conversões sendo realizadas.
taxa = preco_de_um_bitcoin_em_reais()
unidades = investido / taxa 
# Já converte para 'satoshi'. Um BTC equivale a 100 milhões de 'satoshis'.
satoshis = int(unidades * 10e8)


print("Você pode comprar %0.8f BTC com R$%0.2f" % (unidades, investido))
print("Algo em torno de %d satoshis." % satoshis)


    
    