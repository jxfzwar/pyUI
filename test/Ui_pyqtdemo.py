# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jxfzwar/Documents/PyUi/test/pyqtdemo.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.btn1 = QtGui.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(60, 50, 78, 28))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.btn2 = QtGui.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(50, 110, 78, 28))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btnClose = QtGui.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(60, 180, 78, 28))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 110, 56, 18))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn1.setText(_translate("Dialog", "1", None))
        self.btn2.setText(_translate("Dialog", "2", None))
        self.btnClose.setText(_translate("Dialog", "3", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">halo</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

