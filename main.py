# coding=utf-8
# -*- coding: utf-8 -*-
# made by gustavo-depaula

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from natsort import natsorted
from design import design  # Neste arquivo está a MainWindow que foi desenhada
import glob
import dicom
import sys  # Pegar infos do sistema
import os
import numpy
import pyqtgraph
import vtk

class MainWindow(QtGui.QMainWindow, design.Ui_MainWindow):
    dcmFiles = []  # lista onde guarda os arquivos da pasta selecionada
    index = 0
    ArrayDicom = []

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Project N")
        self.setWindowIcon(QtGui.QIcon('design\\brain_icon2.png'))

        imv = self.graphicsView

        #  esconder as coisas denecessárias para a maioria dos usos
        imv.ui.roiBtn.hide()
        imv.ui.menuBtn.hide()
        imv.ui.histogram.hide()

        #configuração dos btns
        self.actionSelecionar_Pasta.triggered.connect(self.browse_folder)
        self.btnLeft.clicked.connect(self.toTheLetf)
        self.btnRight.clicked.connect(self.toRight)
        self.hSlider.valueChanged.connect(self.changeWithSlider)
        self.btnXtra.clicked.connect(self.showBtns)


        PathDicom = "./dicom_images/"
        lstFilesDCM = []  # create an empty list
        for dirName, subdirList, fileList in os.walk(PathDicom):
            for filename in fileList:
                if ".dcm" in filename.lower():  # check whether the file's DICOM
                    lstFilesDCM.append(os.path.join(dirName, filename))

        # Get ref file
        RefDs = dicom.read_file(lstFilesDCM[0])

        # Load dimensions based on the number of rows, columns, and slices (along the Z axis)
        ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

        # Load spacing values (in mm)
        ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

        x = numpy.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0], ConstPixelSpacing[0])
        y = numpy.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])
        z = numpy.arange(0.0, (ConstPixelDims[2] + 1) * ConstPixelSpacing[2], ConstPixelSpacing[2])

        # The array is sized based on 'ConstPixelDims'
        self.ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

        # loop through all the DICOM files
        for filenameDCM in lstFilesDCM:
            # read the file
            ds = dicom.read_file(filenameDCM)
            # store the raw image data
            self.ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array


    def dumpDicomImg(self):
        imv = self.graphicsView
        imv.setImage(self.ArrayDicom[:, :, self.index])
        imv.getView()

    def dumpDicomInfo(self):
        self.listInfo.clear()

        file = self.dcmFiles[self.index]
        self.listInfo.addItem("file: %s" % file)
        data = dicom.read_file("%s" % file)

        keysWeWant = ['PatientName', 'PatientSex', 'PatientBirthDate', 'PerformedProcedureStepDescription', 'PerformedStationAETitle', 'InstitutionName', 'SliceLocation', 'SliceThickness', 'SpacingBetweenSlices']
        for key in data.dir():
            value = getattr(data, key, '')
            if type(value) is dicom.UID.UID or key == "PixelData":
                continue

            for k in keysWeWant:
                if key == k:
                    self.listInfo.addItem("%s : %s" % (key, value))

    def browse_folder(self):
        self.dcmFiles = natsorted(glob.glob("dicom_images\*.dcm"))
        self.hSlider.setMaximum(len(self.dcmFiles) - 1)
        self.dumpDicomInfo()
        self.dumpDicomImg()

    def toRight(self):
        if self.index + 1 != len(self.dcmFiles):
            self.index += 1
            self.hSlider.setValue(self.index)
            self.dumpDicomInfo()
            self.dumpDicomImg()

    def toTheLetf(self):
        if self.index > 0:
            self.index -= 1
            self.hSlider.setValue(self.index)
            self.dumpDicomInfo()
            self.dumpDicomImg()

    def changeWithSlider(self):
        self.index = self.hSlider.value()
        self.dumpDicomInfo()
        self.dumpDicomImg()

    def showBtns(self):
        imv = self.graphicsView
        if imv.ui.roiBtn.isVisible():
            imv.ui.roiBtn.hide()
            imv.ui.menuBtn.hide()
            imv.ui.histogram.hide()
        else:
            imv.ui.roiBtn.show()
            imv.ui.menuBtn.show()
            imv.ui.histogram.show()


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')

    app = QtGui.QApplication(sys.argv)  # uma nova instância do QApplication
    form = MainWindow()  # seta este formulários para o que esta no design
    form.show()  # mostra o form
    # form.iren.Initialize()
    app.exec_()  # e executa o app


if __name__ == '__main__':
    main()
