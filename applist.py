import os
import sys
import subprocess
from PyQt5 import QtGui, QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__( parent )
		self.resize(530,350)		#ukuran frame
		self.move(300,200) 			#letak posisi window
		self.setWindowTitle( "Launcer Belajar" )

		self.home()

	def home(self):
		self.btn = QtWidgets.QLabel( "Masukan Pilihan",self )
		self.btn.resize(150,40)
		self.btn.move(60,19)

		self.btn1 = QtWidgets.QPushButton( "Pilih",self )
		self.btn1.clicked.connect( self.clicked )
		self.btn1.resize(70,20)
		self.btn1.move(60,50)

		self.show()

	def clicked(self):		#membuka file dialog
		self.dialg = QtWidgets.QFileDialog.getOpenFileName( self, 'Open File', 'D:\\Shortcut\\',"Shortcut files (*.lnk)" )
		# if self.dialg.exec_():
		# 	dialgText = str(self.dialg.currentText())
		self.isiDialg = self.dialg[0]
		#link, sc = self.dialg
		#baseDir = 'D:\\Shortcut'+'\\'+str(len(link))
		
		self.label = QtWidgets.QLabel( str(self.isiDialg)[12:], self )
		self.label.resize(150,40)
		self.label.move(140,80)

		self.btn = QtWidgets.QPushButton( "Open",self )
		self.btn.clicked.connect( self.clicked2 )
		self.btn.resize(70,20)
		self.btn.move(60,90)

		self.label.show()
		self.btn.show()


	def clicked2(self):
		self.text = str(self.isiDialg)
		os.startfile(self.text)



def main():
	app = QtWidgets.QApplication(sys.argv)
	ex = MainWindow()
	ex.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()