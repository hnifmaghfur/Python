import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class List(QtWidgets.QDialog):
    def __init__ ( self, parent=None ):
        super(List, self).__init__( parent )

        bg = QtWidgets.QVBoxLayout()
        self.box1 = QtWidgets.QPushButton( "Folder A" )
        self.box1.setCheckable( True )
        self.box1.clicked.connect ( self.fd )
        self.setWindowTitle( "Button demo" )
        self.setLayout( bg )
        bg.addWidget( self.box1 )

    def fd( self,w ):
        self.w = QtWidgets.QDialog()
        self.b = QtWidgets.QLabel (self.w)
        self.b.setText( "Welcome to Maghfur World" )
        self.b.move(100,20)
        self.w.setWindowTitle( "hnifmaghfur" )
        self.w.exec_()

def main():
    app =  QtWidgets.QApplication( sys.argv )
    x = List()
    x.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()