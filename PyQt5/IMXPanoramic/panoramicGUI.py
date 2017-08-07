#!/usr/bin/env python3	
# -*- coding: utf-8 -*-
 
import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import datetime
import time
from functools import partial
 
 
class PanoramicGUI:
	def __init__(self):
		# LOAD THE FROM FROM UI FILE #
		self.MainWindow = uic.loadUi('panoramicGUI.ui')

		# CHOOSE PATH #
		self.MainWindow.ExperimentPathLineEdit.setText("Choose your path...")
		self.MainWindow.ExperimentPathChooseButton.clicked.connect(self.choose_path)

		# SET INITIAL SCREEN (2X1) #
		for i in [1,2,3]:
			for j in [1,2,3]:
				if j==1 and i!=3:
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + '.setVisible(True)')
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setVisible(True)')
				else:
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + '.setVisible(False)')
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setVisible(False)')
		self.MainWindow.HV1x1CheckBox.setChecked(True)				
		self.MainWindow.NumberofScreensComboBox.activated.connect(self.combo_changed)
		self.MainWindow.NumberofScreensComboBox.activated.connect(partial( self.check_box_states, 1, 1))
		
		# UPDATE THE CHECK BOX STATES #
		for i in [1,2,3]:
			for j in [1,2,3]:
				exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.clicked.connect(partial(self.check_box_states,' + str(i) + ', ' + str(j) + '))')
				

		self.MainWindow.SavePositionButton. clicked.connect(self.save_position)

		# ENABLE/DISEBLE START TOMO BUTTON #
		self.MainWindow.StartPanoramicTomographyButton.setEnabled(False)
		self.MainWindow.ExperimentPathLineEdit.textChanged.connect(self.start_button_state)
		self.MainWindow.PanoramicFolderNameLineEdit.textChanged.connect(self.start_button_state)
		self.MainWindow.SampleLengthLineEdit.textChanged.connect(self.start_button_state)

		# SET ONLY INT AVAIBLE TO LENGTH LINEEDIT #
		self.onlyInt = QtGui.QIntValidator(1,10)
		self.MainWindow.SampleLengthLineEdit.setValidator(self.onlyInt)




#############################################
################# FUNCTIONS #################
#############################################

	### ENABLE/DISEBLE START TOMO BUTTON ###
	def start_button_state(self):
		if self.MainWindow.ExperimentPathLineEdit.text() != "Choose your path..." and self.MainWindow.ExperimentPathLineEdit.text() != "Wrong folder, try again..." and self.MainWindow.PanoramicFolderNameLineEdit.text() != '' and self.MainWindow.SampleLengthLineEdit.text() != '':
			self.MainWindow.StartPanoramicTomographyButton.setEnabled(True)
		else:
			self.MainWindow.StartPanoramicTomographyButton.setEnabled(False)


	### SAVE SCREEN CORDINATES (x,y) ###
	def save_position(self):
		x=str(1)
		y=str(2)
		cordinate = x+', '+y
		for i in [1,2,3]:
			for j in [1,2,3]:
				if eval('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.isChecked()'):
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setText(cordinate)')


	### UPDATE THE CHECKBOX STATES ###
	def check_box_states(self, checked_i, checked_j):	
		for i in [1,2,3]:
			for j in [1,2,3]:
				if checked_i==i and checked_j==j:
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setChecked(True)')
				else:
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setChecked(False)')
					
					

	### Define o Número de telas ###
	def combo_changed(self):
		self.MainWindow.HV1x1CheckBox.setChecked(True)
		NumberofScreensValue = str(self.MainWindow.NumberofScreensComboBox.currentText())
		
		for i in [1,2,3]:
			for j in [1,2,3]:
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + '.setVisible(False)')
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setVisible(False)')
		
		for i in range(1, int(NumberofScreensValue[0])+1):
			for j in range(1, int(NumberofScreensValue[2])+1):
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + '.setVisible(True)')
					exec('self.MainWindow.HV' + str(i) + 'x' + str(j) + 'CheckBox.setVisible(True)')
					
				

	
	### CHOOSE PATH TO SAVE IMAGE AND CALIBRATION FILE ###
	def choose_path(self):
		
		cmd = "python3 Functions/FolderDialog.py"
		path = (subprocess.check_output(cmd, shell=True)).decode("utf-8")
		self.MainWindow.ExperimentPathLineEdit.setText(path)
	
        		
	### SHOW IMAGE ON QLABEL WIDGET ###        
	def show_frame(self):
		# Tomamos una captura desde la webcam.
		ok, img = self.webcam.read()

		if not ok:
		    return

		# Creamos una imagen a partir de los datos.
		#
		# QImage
		# (
		#   Los pixeles que conforman la imagen,
		#   Ancho de de la imagen,
		#   Alto de de la imagen,
		#   Numero de bytes que conforman una linea (numero_de_bytes_por_pixel * ancho),
		#   Formato de la imagen
		# )
		# 
		# img.shape
		# (
		#   Alto,
		#   Ancho,
		#   Planos de color/canales/bytes por pixel
		# )
		image = QtGui.QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QtGui.QImage.Format_RGB888)

		# Creamos un pixmap a partir de la imagen.
		# OpenCV entraga los pixeles de la imagen en formato BGR en lugar del tradicional RGB,
		# por lo tanto tenemos que usar el metodo rgbSwapped() para que nos entregue una imagen con
		# los bytes Rojo y Azul intercambiados, y asi poder mostrar la imagen de forma correcta.
		pixmap = QtGui.QPixmap()
		pixmap.convertFromImage(image.rgbSwapped())

		# Mostramos el QPixmap en la QLabel.
		self.MainWindow.lblWebcam.setPixmap(pixmap)


		self.MainWindow.lblWebcam.mousePressEvent = self.get_pixel_position


	### GET CLICKED PIXEL POSITION ###
	def get_pixel_position(self , event):
		x = event.pos().x()
		y = event.pos().y() 
		print(x,y)
 
if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	panoramic = PanoramicGUI()
	panoramic.MainWindow.show()
	app.exec_()

