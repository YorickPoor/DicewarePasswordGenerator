# coding: utf-8
__author__ = 'yorick'

from PyQt4 import QtGui, QtCore
import sys
import src.Method as Meth


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(500, 300, 355, 275)
        self.setWindowTitle('Password generator')
        self.setWindowIcon(QtGui.QIcon('icons/main_icon.png'))
        # create tab
        self.tab = QtGui.QTabWidget(self)
        self.setCentralWidget(self.tab)
        self.group_1 = QtGui.QGroupBox('Generator', self)
        self.tab.addTab(self.group_1, 'Diceware password generator')
        # generate 1 combobox
        self.cbb1 = QtGui.QComboBox(self.group_1)
        self.cbb1.addItem("Length of password", 0)
        self.cbb1.model().item(0).setEnabled(False)
        self.cbb1.addItem("Big length (+-16 characters)", 1)
        self.cbb1.addItem("Middle length (+-12 characters)", 2)
        self.cbb1.addItem("Low length (+-8 characters)", 3)
        self.cbb1.setGeometry(0, 30, 350, 35)
        self.cbb2 = QtGui.QComboBox(self.group_1)
        # generate 2 combobox
        self.cbb2.setGeometry(0, 70, 350, 35)
        self.cbb2.addItem("Password complexity", 0)
        self.cbb2.model().item(0).setEnabled(False)
        self.cbb2.addItem("Hard password", 1)
        self.cbb2.addItem("Middle strength password", 2)
        self.cbb2.addItem("Normal Diceware password", 3)
        self.lineout = QtGui.QLineEdit('', self.group_1)
        self.lineout.setGeometry(0, 110, 350, 35)
        self.btnGo = QtGui.QPushButton('Generate', self.group_1)
        self.btnGo.setGeometry(0, 150, 350, 35)
        self.btnCopy = QtGui.QPushButton('Copy password to clipboard', self.group_1)
        self.btnCopy.setGeometry(0, 190, 350, 35)
        self.connect(self.btnGo, QtCore.SIGNAL('clicked()'), self.go)
        self.connect(self.btnCopy, QtCore.SIGNAL('clicked()'), self.copy)

    def go(self):
        if self.cbb1.currentIndex() == 1:
            if self.cbb2.currentIndex() == 1:
                answer = Meth.voider(7)
                answer = Meth.strength_hard(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 2:
                answer = Meth.voider(7)
                answer = Meth.strenght_middle(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 3:
                answer = Meth.voider(7)
                self.lineout.setText(answer)
        elif self.cbb1.currentIndex() == 2:
            if self.cbb2.currentIndex() == 1:
                answer = Meth.voider(4)
                answer = Meth.strength_hard(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 2:
                answer = Meth.voider(4)
                answer = Meth.strenght_middle(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 3:
                answer = Meth.voider(4)
                self.lineout.setText(answer)
        elif self.cbb1.currentIndex() == 3:
            if self.cbb2.currentIndex() == 1:
                answer = Meth.voider(2)
                answer = Meth.strength_hard(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 2:
                answer = Meth.voider(2)
                answer = Meth.strenght_middle(answer)
                self.lineout.setText(answer)
            elif self.cbb2.currentIndex() == 3:
                answer = Meth.voider(2)
                self.lineout.setText(answer)

    def copy(self):
        clipboard = QtGui.QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.lineout.text())


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
