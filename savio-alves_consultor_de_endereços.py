'''
Essa atividade visa testar seus conhecimentos acerca de requisições HTTP e manipulação de 
dicionários.  

Conceito:

Criar um programa que recebe um CEP do usuário e retorna o endereço completo (Rua, Bairro, 
Cidade e Estado) utilizando uma API pública.



Passos:

    Importe a biblioteca requests.
    Peça ao usuário para digitar um CEP (apenas números).
    Use a URL da API ViaCEP: https://viacep.com.br/ws/{CEP_DIGITADO}/json/.
    Faça uma requisição do tipo GET e converta a resposta para JSON (dicionário).
    Se o CEP for válido, exiba as informações no formato:
    "Logradouro: [logradouro] | Bairro: [bairro] | Cidade: [localidade] - [uf]".
    Caso o CEP não seja encontrado ou o formato esteja errado, exiba uma mensagem de erro 
    amigável.

Sinta-se livre para adicionar funcionalidades, como por exemplo: validar a entrada do 
usuário.
'''
import requests, json, sys
from pprint import (pprint as PPrint)


def tratamento_de_entrada(cpf: str) -> str:
    return cpf.replace('.', '').replace('-', '')

def invocar_prompt() -> str:    
    return input("Digite seu CPF: ")

def formata_uma_url(cpf: str) -> str:
    PROTOCOLO = "https"
    DOMINIO   = "viacep.com.br"
    ENDPOINT  = f"/ws/{tratamento_de_entrada(cpf)}/json/"
    
    return f"{PROTOCOLO}://{DOMINIO}{ENDPOINT}"


cpf_entrada = invocar_prompt()
url = formata_uma_url(cpf_entrada)

if __debug__:
    print(f"\nURL: {url}\n")
    
retorno = requests.get(url)

if retorno.status_code == 400:
    print("Houve um erro na requisição!")
    exit(2)

if __debug__:
    try:
        dados = retorno.json()
    except json.JSONDecodeError:
        print("Houve um erro.")
        PPrint(sys.exc_info(), indent=6, underscore_numbers=True)
    else:
        print("Tudo ocorreu muito bem.")
