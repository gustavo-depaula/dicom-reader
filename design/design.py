# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfacegráfica.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(681, 463)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("brain_icon2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = ImageView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(450, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnLeft = QtGui.QPushButton(self.centralwidget)
        self.btnLeft.setObjectName(_fromUtf8("btnLeft"))
        self.horizontalLayout_2.addWidget(self.btnLeft)
        self.btnRight = QtGui.QPushButton(self.centralwidget)
        self.btnRight.setObjectName(_fromUtf8("btnRight"))
        self.horizontalLayout_2.addWidget(self.btnRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listInfo = QtGui.QListWidget(self.centralwidget)
        self.listInfo.setObjectName(_fromUtf8("listInfo"))
        self.verticalLayout_2.addWidget(self.listInfo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hSlider = QtGui.QSlider(self.centralwidget)
        self.hSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider.setObjectName(_fromUtf8("hSlider"))
        self.verticalLayout.addWidget(self.hSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSelecionar_Pasta = QtGui.QAction(MainWindow)
        self.actionSelecionar_Pasta.setObjectName(_fromUtf8("actionSelecionar_Pasta"))
        self.menuFile.addAction(self.actionSelecionar_Pasta)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnLeft.setText(_translate("MainWindow", "<", None))
        self.btnRight.setText(_translate("MainWindow", ">", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSelecionar_Pasta.setText(_translate("MainWindow", "Selecionar Pasta", None))

from pyqtgraph import ImageView
