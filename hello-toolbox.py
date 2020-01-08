import sys
from PyQt5 import QtGui, QtCore, QtWidgets

def jendela():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget ()
    b = QtWidgets.QLabel (w)
    b.setText("Welcome to Maghfur World")
    w.setGeometry(100,100,250,50)
    b.move(50,20)
    w.setWindowTitle("hnifmaghfur")
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    jendela()
