#import openFile as oF
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFileDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from pathlib import Path
import pandas as pd

#Função para selecionar o arquivo
def AbreArquivo():
    arquivo = QFileDialog.getOpenFileName(caption="Selecione o arquivo", filter= "CSV (*.csv)")[0]
    with open (arquivo, 'r', encoding='utf8') as a:
        dados = a.read() #str
    dados = dados.replace("\n",";")
    df = pd.read_csv(dados, sep=";")
    
        


#Cria aplicação
app = QApplication(sys.argv)

#Cria Janela
janela = QWidget()
janela.resize(700,700)
janela.setWindowTitle("Analisador Foda")

#Cria Botão
btn_abreArquivo = QPushButton("Abrir Arquivo",janela)
#Define a posição e tamanho do botão
btn_abreArquivo.setGeometry(300,300,100,30)

#Evento click do botão
btn_abreArquivo.clicked.connect(AbreArquivo)

#Seta o CSS
#btn_abreArquivo.setStyleSheet("")

#Cria label
label_titulo = QLabel("Analisador Foda", janela)
label_titulo.move(250,100)
label_titulo.setStyleSheet("font-size: 30px;")


#Mostra a janela e executa a aplicação
janela.show()
app.exec()
