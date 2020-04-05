# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 05:41:17 2020
@author: gabriel rocco
"""


from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

from geopy.geocoders import Nominatim
import pandas as pl

import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import numpy

import googlemaps
import geopandas

import shutil

import glob

from waitress import serve




"""
-------------------------------------------------------------------------------------------------------------------
VARIAVEIS GLOBAIS
-------------------------------------------------------------------------------------------------------------------
"""

#Inicializa a base google utilizando Pandas
googleDatabase=pl.DataFrame
database = pl.DataFrame



#Inicializa a instancia Flask
app = Flask(__name__)


#Google Geocoding API
APIKey = ""
#Nome da base de dados a atualizar
nomeDataBase = ""
#.json credenciais


caminhoDatabase = ""

#Google Sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#Credenciais JSON para atualizar a base de dados


sheet = gspread.models.Worksheet





"""
-------------------------------------------------------------------------------------------------------------------
FIM VARIAVEIS GLOBAIS
-------------------------------------------------------------------------------------------------------------------
"""






"""
-------------------------------------------------------------------------------------------------------------------
DATABASE START:
-------------------------------------------------------------------------------------------------------------------
"""



"""
Faz a leitura da base de dados CSV principal
"""
def make_database(file):
    print()





"""
Faz a leitura das credenciais para o API Geolocator para a planilha
"""
def make_sheets_database_connection(client):
    print()





def readCredenciais(credencialFile):
    print()

"""
-------------------------------------------------------------------------------------------------------------------
FIM DATABASE START
-------------------------------------------------------------------------------------------------------------------
"""














"""
-------------------------------------------------------------------------------------------------------------------
FUNCOES MESTRE:
Funcoes principais do programa. Incluem tratamento de dados, buscas efetuadas,etc
-------------------------------------------------------------------------------------------------------------------
"""






"""
Retorna a latitude e a longitude de um endereco com o API do Google em vez do modulo Geopy


ATENCAO:
Para a utilizacao eh necessario gerar e colocar a key da respectiva API na variavel definida no inicio
do arquivo como APIKey.
"""
def serchCoordinatesById_GoogleGeocodingAPI(endereco):
    print()



"""
Utilizando uma databaseToUse a funcao atualiza a base de dados conectada na nuvem
"""
def atualizarCSVCloud(databaseToUse):
    print()






"""
Gera um arquivo SHP a partir de um CSV, permitindo uma importacao mais facil em programas como QGIS
"""
def generateSHPFileFromCSV(data):
    print()






"""
#FUNCAO ATUAL PARA PEGAR COORDENADAS COM ENDERECOS
#Utilizando o modulo geopy, permite encontrar as coordenadas utilizando uma string de endereco

Recebe uma string de endereco e retorna uma array bidimensional com [lat,long]

"""
def getXYFromEndereco(database_to_update,index):
    print()





def updateCSV(database_to_update,local):
    print()


def makeProcessoCompleto():
    global googleDatabase


    makeTypeCorrections()
    print("LOG:")
    print("Comecando o processo...")
    print("\nAtualizando coordenadas...\n")
    googleDatabase = updateCSV(googleDatabase,False)
    print("\nAtualizando arquivos na nuvem...")
    print("Pode demorar dependendo da quantidade de dados para atualizar...")
    atualizarCSVCloud(googleDatabase)
    print("\nGerando e exportando .SHP")
    generateSHPFileFromCSV(googleDatabase)
    print("\nATUZALIZACAO: EXECUCAO DO PROCESSO COMPLETADA\n\n")



def makeProcessoCompletoLocal():
    global database

    makeTypeCorrections()

    print("LOG:")
    print("Comecando o processo...")
    print("\nAtualizando coordenadas...\n")
    database = updateCSV(database,True)
    print("\nBase local atualizada")
    print("\nGerando e exportando .SHP")
    exportarCSV(database)
    generateSHPFileFromCSV(database)
    print("\nATUZALIZACAO: EXECUCAO DO PROCESSO COMPLETADA\n\n")





"""
-------------------------------------------------------------------------------------------------------------------
FIM FUNCOES MESTRE
-------------------------------------------------------------------------------------------------------------------
"""










"""
-------------------------------------------------------------------------------------------------------------------
UTILITARIOS:
Aqui encontram-se pequenas funcoes que auxiliam em processos
-------------------------------------------------------------------------------------------------------------------
"""


"""
Apos utilização dos arquivos do usuário os mesmos são destruídos no servidor para não armazenar dados
"""
def deleteContent():
    print()




"""
Remove entradas que nao possam ser convertidas por falta de informacao e ajuda na regularizacao de tipos
"""
def removeInuteisEajustaInteiros():
    print()





"""
Corrige a interpretacao de dados especificos com os tipos necessarios, caso contrario pode existir problemas
na hora da gravacao.
Exemplo: Gravar um numero que deveria ser do tipo inteiro como float.
Ja alterei o tipo de dado no Excel mas nao resultou entao manipulo isso aqui.
"""
def makeTypeCorrections():
       print()



"""
Transforma as colunas relacionadas com enderecos em uma string unica para possibilitar buscas. Faz isso numa ordem especifica e de modo a facilitar a interpretacao pelo API
"""
def handleEndereco(database, indexToSearch, utilizarCep):
    print()



"""
Exporta o CSV quando o processamento eh feito de forma local
"""
def exportarCSV(databaseToExport):
    print()
"""
-------------------------------------------------------------------------------------------------------------------
FIM UTILITARIOS
-------------------------------------------------------------------------------------------------------------------
"""










"""
-------------------------------------------------------------------------------------------------------------------
FLASK:
Cuida de toda a parte do back-end
Trata o input dos usuarios
-------------------------------------------------------------------------------------------------------------------
"""






#Helps upload
ALLOWED_EXTENSIONS = {'json'}
UPLOAD_FOLDER = "credUp"


"""
Cuida do processamento na nuvem, assim como input de informacoes necessarias
"""
@app.route("/", methods=["POST","GET"])
def index():
    print()


"""
Cuida do processamento local, assim como input de informacoes necessarias
"""
@app.route("/local", methods=["POST","GET"])
def processoLocal():
    print()

"""
Realiza o download do .zip apos processamento
"""
@app.route('/zipToDownload')
def download_file():
     print()



"""
Roda o servidor
"""
if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0')
    serve(app, host='0.0.0.0', port=80)



"""
-------------------------------------------------------------------------------------------------------------------
FIM FLASK
-------------------------------------------------------------------------------------------------------------------
"""
