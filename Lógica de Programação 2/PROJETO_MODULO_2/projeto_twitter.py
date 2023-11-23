import csv

def carregando_base_dados():
    with open('projeto_LP_tweets_2022.csv', 'r') as arquivo_tweets:
        leitor_csv = csv.DictReader(arquivo_tweets)
        base_dados = [linha for linha in leitor_csv]
    return base_dados

