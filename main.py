# coding=utf-8
# -*- coding: utf-8 -*-

from PyQt4 import QtGui # Importa o módulo do PyQT que precisamos
import dicom
import sys # Pegar infos do sistema
import os

from design import design # Neste arquivo está a MainWindow que foi desenhada


class ChooseFile(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # permite que acessamos variáveis e métodos do arquivo design.py
        super(self.__class__, self).__init__()
        self.setupUi(self)  # isso é definido no design.py

        self.btnBrowse.clicked.connect(self.browse_folder) # quando o botão for apertado executa a função
        self.btnSelect.clicked.connect(self.select_file)

    def browse_folder(self):
        self.listWidget.clear() # limpa a lista
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Escolha uma pasta!")

        if directory: # se usuário n escolheu, n continua
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

    def select_file(self):
        self.listDicom.clear()
        file = QtGui.QFileDialog.getOpenFileName(self, 'Escolha um arquivo DICOM.')

        print "%s" % file
        data = dicom.read_file("%s" % file)
        for key in data.dir():
            value = getattr(data, key, '')
            if type(value) is dicom.UID.UID or key == "PixelData":
                continue

            self.listDicom.addItem("%s : %s" % (key, value))

def main():
    #
    reload(sys)
    sys.setdefaultencoding('utf8')
    # para o programa reconhecer utf-8

    app = QtGui.QApplication(sys.argv)  # uma nova instância do QApplication
    form = ChooseFile()                 # seta este formulários para o que esta no design
    form.show()                         # mostra o form
    app.exec_()                         # e executa o app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()