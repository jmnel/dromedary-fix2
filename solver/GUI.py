#tmp.py
from PySide2.QtWidgets import (QApplication,  QMainWindow, QMenu, QMessageBox)
from solver import res
import sys

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.setupHelpMenu()


    def setupHelpMenu(self):
        helpMenu = QMenu("&Help", self)
        self.menuBar().addMenu(helpMenu)
        helpMenu.addAction("&About", self.about)


    def about(self):
        QMessageBox.about(self, "About", "This is a demo")


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 512)
    window.show()
    QMessageBox.about(window,'Optimal Result',str(res.x))
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
