import getpass
# # Função para ler o arquivo de configuração
# def ler_config(arquivo):
#     dados = {}
#     with open(arquivo, "r", encoding="utf-8") as file:
#         for linha in file:
#             if "=" in linha:
#                 chave, valor = linha.strip().split("=", 1)
#                 dados[chave] = valor
#     return dados

# # Ler credenciais do arquivo config.txt
# config = ler_config("config.txt")

# Capturar valores do arquivo
USUARIO = input("Digite a Chapa: ")
SENHA = getpass.getpass("Digite a senha do Beehome: ")
SENHA_BI = getpass.getpass("Digite a senha do Power BI: ")