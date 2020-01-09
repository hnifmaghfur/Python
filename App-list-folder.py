import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class List(QtWidgets.QDialog):
    def __init__ ( self, parent=None ):
        super(List, self).__init__( parent )

        bg = QtWidgets.QVBoxLayout()
        self.box1 = QtWidgets.QPushButton( "Folder A" )
        self.box1.clicked.connect ( self.fd )
        self.setWindowTitle( "Button demo" )
        bg.addWidget( self.box1 )

    def fd( self ):
        w = QtWidgets.QWidget ()
        b = QtWidgets.QLabel ( w )
        b.setText( "Welcome to Maghfur World" )
        w.setGeometry( 100,100,250,50 )
        b.move( 50,20 )
        w.setWindowTitle( "hnifmaghfur" )

def main():
    app =  QtWidgets.QApplication()
    x = List()
    x.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()