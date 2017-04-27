# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jxfzwar/Documents/PyUi/topopt2d/topoptui.ui'
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
        Dialog.resize(330, 310)
        Dialog.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 56, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 56, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.nx = QtGui.QLineEdit(Dialog)
        self.nx.setGeometry(QtCore.QRect(222, 60, 81, 30))
        self.nx.setObjectName(_fromUtf8("nx"))
        self.ny = QtGui.QLineEdit(Dialog)
        self.ny.setGeometry(QtCore.QRect(222, 100, 81, 30))
        self.ny.setObjectName(_fromUtf8("ny"))
        self.volfrac = QtGui.QLineEdit(Dialog)
        self.volfrac.setGeometry(QtCore.QRect(222, 140, 81, 30))
        self.volfrac.setObjectName(_fromUtf8("volfrac"))
        self.rmin = QtGui.QLineEdit(Dialog)
        self.rmin.setGeometry(QtCore.QRect(222, 180, 81, 30))
        self.rmin.setObjectName(_fromUtf8("rmin"))
        self.p = QtGui.QLineEdit(Dialog)
        self.p.setGeometry(QtCore.QRect(222, 220, 81, 30))
        self.p.setObjectName(_fromUtf8("p"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.exit = QtGui.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(20, 270, 78, 28))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.start = QtGui.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(230, 270, 78, 28))
        self.start.setObjectName(_fromUtf8("start"))
        self.closefig = QtGui.QPushButton(Dialog)
        self.closefig.setGeometry(QtCore.QRect(130, 270, 78, 28))
        self.closefig.setObjectName(_fromUtf8("closefig"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nx", None))
        self.label_2.setText(_translate("Dialog", "Ny", None))
        self.label_3.setText(_translate("Dialog", "Sum of Volume", None))
        self.label_4.setText(_translate("Dialog", "Distance of Filter", None))
        self.label_5.setText(_translate("Dialog", "Penalty Coefficient", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#0000ff;\">2D TOPOLOGICAL OPTIMIZATION BY OC METHOD</span></p></body></html>", None))
        self.exit.setText(_translate("Dialog", "EXIT", None))
        self.start.setText(_translate("Dialog", "START", None))
        self.closefig.setText(_translate("Dialog", "CLOSE FIG", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

