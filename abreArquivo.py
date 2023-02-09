import sys
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QTableView, QApplication
from PyQt5.QtCore import QAbstractTableModel
from modeloPandas import modeloPandas

class abreArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    #Função para selecionar o arquivo
    def AbreArquivo(self):
        self.arquivo = QFileDialog.getOpenFileName(caption="Selecione o arquivo", filter="CSV (*.csv)")
        print(self.arquivo)
        self.arquivoPDataFrame()

    def getArquivo(self):
        return self.arquivo

    def arquivoPDataFrame(self):
        #self.df = pd.DataFrame(zip(self.arquivo))
        self.df = pd.read_csv(self.arquivo[0],sep=';')
        #Cria a tabela de exibição do DataFrame
        self.view_tabela = QTableView()
        modelo_tabela = modeloPandas(self.df)
        self.view_tabela.setModel(modelo_tabela)
        self.view_tabela.resize(800, 600)
        self.view_tabela.show()