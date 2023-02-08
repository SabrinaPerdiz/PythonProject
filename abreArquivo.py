import sys
import pandas as pd
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QAbstractTableModel

class abreArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    #Função para selecionar o arquivo
    def AbreArquivo(self):
        self.arquivo = pd.DataFrame(QFileDialog.getOpenFileName(caption="Selecione o arquivo", filter="CSV (*.csv)"))
        #data = self.arquivoPDataFrame
        #self.arquivo = data

    def getArquivo(self):
        print(self.arquivo)

    def arquivoPDataFrame(self):
        df = pd.DataFrame(self.arquivo)
        return df
    
    #def returnModel(QAbstractTableModel):
