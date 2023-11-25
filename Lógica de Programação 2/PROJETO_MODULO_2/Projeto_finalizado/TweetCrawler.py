import re
import csv
from datetime import datetime
import pandas as pd
import json


def menu(modeloMenu):
    print("-----------------MENU-----------------")
    print("1 - Buscar tweets por data.")
    print("2 - Buscar tweets por termo.")
    print("3 - Buscar tweets por assunto.")

    if modeloMenu:
        print("4 - Salvar dados da busca anterior.")

    print("5 - Sair.")
    print("--------------------------------------")

    return validar_escolha(input('Insira o número da opção desejada: '), ['1', '2', '3', '5'] if not modeloMenu else ['1', '2', '3', '4', '5'])


def validar_escolha(escolha, listaValida):
    if escolha not in listaValida:
        while True:
            print(f'Desculpe, mas essa não é uma opção válida.')
            escolha = input('Insira o número da opção desejada: ')
            if escolha in listaValida:
                break

    return escolha


def coletar_assuntos():
    assuntos = []

    with open("tweets_2022.csv", 'r', newline='', encoding='utf-8') as aqv_csv:
        leitorCsv = csv.reader(aqv_csv)
        next(leitorCsv)

        for linha in leitorCsv:
            if linha[4] not in assuntos:
                assuntos.append(linha[4])

    return assuntos


def montar_consulta(opcao, consulta):
    dataset = []

    with open("tweets_2022.csv", 'r', newline='', encoding='utf-8') as aqv_csv:
        leitor_csv = csv.reader(aqv_csv)
        next(leitor_csv)
        contador = 0

        for linha in leitor_csv:
            data_formatada = formatar_data(linha[0].split()[0])
            nova_linha = None

            if opcao == 1 and consulta == data_formatada:
                nova_linha = [data_formatada, linha[3], linha[4]]
            elif opcao == 2 and consulta in linha[3]:
                nova_linha = [data_formatada, linha[3], linha[4]]
            elif opcao == 3 and consulta in linha[4]:
                nova_linha = [data_formatada, linha[3], linha[4]]

            if nova_linha:
                dataset.append(nova_linha)
                contador += 1

    return dataset, contador


def formatar_data(data):
    return datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

def montar_dicionario(dataset):
    dicionarios = []

    for item in dataset:
        item_adaptado = {
            "data": item[0],
            "conteudo": item[1],
            "assunto": item[2]
        }

        dicionarios.append(item_adaptado)

    return dicionarios


def main():
    print("--------------------------------------")
    print("-SISTEMA DE BUSCA EM DADOS DO TWITTER-")
    modeloMenu = 0
    salvo = 0

    while True:
        escolha = menu(modeloMenu)

        match escolha:
            case '1':
                consulta = input('Informe a data da consulta (dd/MM/YYYY): ')

                if not bool(re.match(r'\b\d{2}/\d{2}/\d{4}\b', consulta)):
                    while True:
                        print(f'Desculpe, mas essa não é uma data válida.')
                        consulta = input('Informe a data no formato dd/MM/YYYY: ')
                        if bool(re.match(r'\b\d{2}/\d{2}/\d{4}\b', consulta)):
                            break

                data, total = montar_consulta(1, consulta)

            case '2':
                consulta = input('Informe o termo da consulta: ').lower()
                data, total = montar_consulta(2, consulta)

            case '3':
                assuntos = coletar_assuntos()

                print('ASSUNTOS DISPONÍVEIS-----------------')
                for i in range(len(assuntos)):
                    print(f'{i+1} - {assuntos[i].title()}')

                consulta = assuntos[int(validar_escolha(input('Insira o número da opção desejada: '), [str(i+1) for i in range(len(assuntos))]))-1]
                data, total = montar_consulta(3, consulta)

            case '4':
                dicionarios = montar_dicionario(data)
                data.clear()

                consulta = consulta.replace(' ', '-')
                consulta = consulta.replace('/', '-')
                with open(f"tweets_{consulta}.json", 'w') as aqv_json:
                    json.dump(dicionarios, aqv_json, indent=4)

                salvo = 1

            case '5':
                print('\nObrigado por utilizar o sistema.')
                break

        if total and data:
            print(f'\nSua consulta por tweets referentes a "{consulta}" retornou {total} resultados na base de dados disponível.\n')
            modeloMenu = 1
        elif salvo:
            print(f'\nSua consulta por tweets referentes a "{consulta}" foi salva no arquivo "tweets_{consulta}.json".\n')
            salvo = 0
            modeloMenu = 0
        elif not total:
            print(f'\nSua consulta por tweets referentes a "{consulta}" não encontrou resultados na base de dados disponível.\n')
            modeloMenu = 0

        if data:
            df = pd.DataFrame(data, columns=['Data', 'Tweet', 'Assunto'])
            with pd.option_context('display.width', 1000, 'display.max_columns', None):
                print(df)
                print()


if __name__ == "__main__":
    main()