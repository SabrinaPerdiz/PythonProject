import sys
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QTableView
from modeloPandas import modeloPandas

class abreArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.view_tabela = QTableView()

    #Função para selecionar o arquivo
    def AbreArquivo(self):
        self.arquivo = QFileDialog.getOpenFileName(caption="Selecione o arquivo", filter="CSV (*.csv)")
        print(self.arquivo)
        self.arquivoPDataFrame()

    def arquivoPDataFrame(self):
        #Pega o arquivo selecionado e lê para DataFrame
        self.df = pd.read_csv(self.arquivo[0],sep=';')

        #Cria a tabela de exibição do DataFrame
        #self.view_tabela = QTableView()
        modelo_tabela = modeloPandas(self.df)
        self.view_tabela.setModel(modelo_tabela)
        self.view_tabela.resize(800, 600)
        self.view_tabela.show()

    def onTableClicked(self):
        print(self.view_tabela.selectedIndexes())
                