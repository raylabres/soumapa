import requests
import ast
import pandas as pd
import os
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

diretorio = 'C:/soumapa/'
diretorio_temp = f'{diretorio}temp'
diretorio_templates = f'{diretorio}templates'
url1 = ''
url2 = ''
url3 = ''


def verifica_diretorio():   
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    if not os.path.exists(diretorio_temp):
        os.makedirs(diretorio_temp)
    if not os.path.exists(diretorio_templates):
        os.makedirs(diretorio_templates)

def baixar_imagem():
    urls = [
        'https://raw.githubusercontent.com/raylabres/soumapa/main/carregando.png',
        'https://raw.githubusercontent.com/raylabres/soumapa/main/menu.png',
        'https://raw.githubusercontent.com/raylabres/soumapa/main/fundo_branco.png',
        'https://raw.githubusercontent.com/raylabres/soumapa/main/icone.ico'
    ]

    for pos_url, url in enumerate(urls):
        response = requests.get(url)
        if response.status_code == 200:
            nome_do_arquivo = url.split("/")[-1]
            caminho_arquivo = f'{diretorio_templates}/{nome_do_arquivo}'
            
            with open(caminho_arquivo, "wb") as arquivo:
                arquivo.write(response.content)

        else:
            erro = 'erro'

def busca_cep(busca):
    try:
        url = f'https://viacep.com.br/ws/{busca}/json/'

        resposta = requests.get(url)
        dados = resposta.json()
    except:
        dados = 'erro'

    return dados


def cria_base():
    try:
        with open(f'{diretorio}/temp/dados.txt', 'r') as arquivo_txt:
            conteudo = arquivo_txt.read()
            lista_dados = ast.literal_eval(conteudo)

            df = pd.DataFrame(lista_dados).transpose()
            colunas = ['CEP', 'Logradouro', 'Bairro', 'Cidade', 'Estado']
            df.columns = colunas
            df.to_excel(f'{diretorio}/temp/dados_exportados.xlsx', sheet_name='Consultas',index=False)
    except:
        try:
            df = pd.DataFrame()
            df.to_excel(f'{diretorio}/temp/dados_exportados.xlsx', index=False)
        except:
            erro = 'erro'

def apaga_arquivos():
    try:
        arquivos = os.listdir(f'{diretorio}/temp')
        for arquivo in arquivos:
            os.remove(f'{diretorio}/temp/{arquivo}')
    except:
        erro = 'erro'

baixar_imagem()