#import openFile as oF
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QTableView
from PyQt5.QtGui import QIcon
from pathlib import Path
from abreArquivo import abreArquivo
import modeloPandas



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

#Cria objeto abreArquivo
ab = abreArquivo("")

def setView():
    #Cria a tabela de exibição do DataFrame
    view_tabela = QTableView()
    modelo_tabela = modeloPandas(ab.arquivo)
    view_tabela.setModel() 

#Evento click do botão
btn_abreArquivo.clicked.connect(ab.AbreArquivo)
btn_abreArquivo.clicked.connect(setView())

#Seta o CSS
#btn_abreArquivo.setStyleSheet("")

#Cria label
label_titulo = QLabel("Analisador Foda", janela)
label_titulo.move(250,100)
label_titulo.setStyleSheet("font-size: 30px;")

#Mostra a janela e executa a aplicação
janela.show()
app.exec()
