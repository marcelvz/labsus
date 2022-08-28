''' 
Esse código foi criado para simular uma ETL simples que coleta os dados de uma 
planilha excel, seleciona os dados importantes e salva em um banco de dados simples

Quando for implantado o LabSUS vai utilizar a infraestrutura do Data Lake que a
RNDS possue. 

'''

from tinydb import TinyDB, Query
import pandas as pd

pesquisa_br = TinyDB('pesquisa_br.json')

planilha = pd.read_excel('planilha.xlsx')

selecao = ['Código', 'UF', 'Município', 'Ano', 'Título','Palavras Chaves', 
           'Resumo', 'Subagenda','Instituição','Valor Total', 'Valor DECIT',
           'Modalidade de Fomento', 'Aplicabilidade ao SUS', 
           'Resultados Encontrados', 'Recomendação para o SUS','Link da Pesquisa'] 

planilha_filtrada = planilha.fillna('completar').filter(selecao)


for pesquisa in planilha_filtrada.iloc:
  pesquisa_br.insert({'codigo':pesquisa[0], 'titulo':pesquisa[4], 'palavras_chave':pesquisa[5].split(';')})
