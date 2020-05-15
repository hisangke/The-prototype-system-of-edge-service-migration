import sys
from PySide2.QtWidgets import QApplication
from EdgeServiceMigrationUI import EdgeServiceMigrationUI
from MaximumFlow import MaximumFlow
import networkx as nx



from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash=QSplashScreen()
    pixmap=QtGui.QPixmap(QtGui.QImage("C:/Users/user/Desktop/monkey.png"))
    splash.setPixmap(pixmap)
    splash.show()


    mainWindow = EdgeServiceMigrationUI()
    w=1050
    h=350
    mainWindow.resize(w, h)
    mainWindow.setMaximumSize(w, h)
    mainWindow.setMinimumSize(w, h)


    mainWindow.show()
    splash.finish(mainWindow)
    sys.exit(app.exec_())
