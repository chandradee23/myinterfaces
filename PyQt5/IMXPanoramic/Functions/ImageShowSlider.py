# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageShowSlider.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from H5Files import getArray
import numpy as np

class Ui_ImageShowWidget(object):
    def setupUi(self, ImageShowWidget):
        ImageShowWidget.setObjectName("ImageShowWidget")
        ImageShowWidget.resize(659, 527)
        self.gridLayout = QtWidgets.QGridLayout(ImageShowWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ImageShowLineEdit = QtWidgets.QLineEdit(ImageShowWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageShowLineEdit.sizePolicy().hasHeightForWidth())
        self.ImageShowLineEdit.setSizePolicy(sizePolicy)
        self.ImageShowLineEdit.setObjectName("ImageShowLineEdit")
        self.gridLayout_2.addWidget(self.ImageShowLineEdit, 1, 1, 1, 1)
        self.ImageShowSlider = QtWidgets.QSlider(ImageShowWidget)
        self.ImageShowSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ImageShowSlider.setObjectName("ImageShowSlider")
        self.gridLayout_2.addWidget(self.ImageShowSlider, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(ImageShowWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.retranslateUi(ImageShowWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageShowWidget)

    def retranslateUi(self, ImageShowWidget):
        _translate = QtCore.QCoreApplication.translate
        ImageShowWidget.setWindowTitle(_translate("ImageShowWidget", "Image Show"))
        
        self.ImageShowSlider.sliderMoved.connect(self.Moved)
        
        

        
    def Moved(self):
		
		
        tomo_path = "/mnt/Data/IMX/Data/Pitch_Roll_BIC_Test/tomo.h5"#sys.argv[1]
        dark_path = "/mnt/Data/IMX/Data/Pitch_Roll_BIC_Test/tomo_dark_before.h5"#sys.argv[2]
        flat_path = "/mnt/Data/IMX/Data/Pitch_Roll_BIC_Test/tomo_flats.h5"#sys.argv[3]

        data = getArray(tomo_path, dark_path, flat_path)
        face = np.asarray(data, dtype=np.float32)
        face.reshape([2048, 2048])
        print(face)
        #self.label.setPixmap(QtGui.QPixmap("LNLS_logo_mini.jpg"))
        self.label.setPixmap(QtGui.QPixmap.loadFromData(data))
        #self.label.setPixmap(QtGui.QPixmap.fromImage(face))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageShowWidget = QtWidgets.QWidget()
    ui = Ui_ImageShowWidget()
    ui.setupUi(ImageShowWidget)
    ImageShowWidget.show()
    sys.exit(app.exec_())

