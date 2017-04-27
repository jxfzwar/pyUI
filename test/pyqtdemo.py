# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from Ui_pyqtdemo import Ui_Dialog


class Pyqtdemo(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @QtCore.pyqtSignature("")
    def on_btn1_clicked(self):
        self.label.setText('fffff')
    
    @QtCore.pyqtSignature("")
    def on_btn2_clicked(self):
        self.label.setText('zzzzz')
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Pyqtdemo()
    dlg.show()
    sys.exit(app.exec_())
