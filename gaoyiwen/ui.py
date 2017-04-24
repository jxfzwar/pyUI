# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from Ui_ui import Ui_GaoYiWen


class Gao(QtGui.QDialog, Ui_GaoYiWen):
    
    GoodNumber = 0
    GoodNumberCopy = 0
    
    MoneyPocket = 100
    MoneyPocketCopy = 100
    
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    number1copy = 0
    number2copy = 0
    number3copy = 0
    number4copy = 0
    
    level = 1
    PerCostDay = 2
    MaximumGood = 10
   
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @QtCore.pyqtSignature("")
    def on_selectagain_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @QtCore.pyqtSignature("")
    def on_nextday_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @QtCore.pyqtSignature("")
    def on_check_clicked(self):
        Gao.MoneyPocketCopy = Gao.MoneyPocket
        Gao.MoneyPocket = Gao.MoneyPocket + self.sell1.value() + 5 * self.sell2.value() + 10 * self.sell3.value() + 20 * self.sell4.value() \
        - self.buy1.value() - 5 * self.buy2.value() - 10 * self.buy3.value() - 20 * self.buy4.value()
        
        Gao.GoodNumberCopy = Gao.GoodNumber
        Gao.GoodNumber = Gao.GoodNumber - self.sell1.value() - self.sell2.value() - self.sell3.value() - self.sell4.value() \
        + self.buy1.value() + self.buy2.value() + self.buy3.value() + self.buy4.value()
        
        self.moneyleft.setText(str(Gao.MoneyPocket))
        self.placeleft.setText(str(Gao.MaximumGood - Gao.GoodNumber))
        
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText,QtCore.Qt.blue) 
        if Gao.MaximumGood == 'inf':
            if Gao.MoneyPocket >= Gao.PerCostDay:
                self.afterdayresult_2.setText('No probelm! You can click next day or select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.MoneyPocket < Gao.PerCostDay and Gao.MoneyPocket >=0:
                self.afterdayresult_2.setText('No money for storage! Select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.MoneyPocket < 0:
                self.afterdayresult_2.setText('No enough money for buy and sell! Select again!')
                self.afterdayresult_2.setPalette(pe) 
        else:
            if Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket >= Gao.PerCostDay:
                self.afterdayresult_2.setText('No probelm! You can click next day or select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket < Gao.PerCostDay and Gao.MoneyPocket >= 0:
                self.afterdayresult_2.setText('No money for storage! Select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket < 0:
                self.afterdayresult_2.setText('No enough money for buy and sell! Select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.GoodNumber > Gao.MaximumGood:
                self.afterdayresult_2.setText('No enough place for storage! Select again!')
                self.afterdayresult_2.setPalette(pe) 
                
        if self.sell1.value() > Gao.number1 or self.sell2.value() > Gao.number2 \
        or self.sell3.value() > Gao.number3 or  self.sell4.value() > Gao.number4:
            self.afterdayresult_2.setText('No enough goods for sell! Select again!')
            
        Gao.number1copy = Gao.number1
        Gao.number2copy = Gao.number2
        Gao.number3copy = Gao.number3
        Gao.number4copy = Gao.number4
        Gao.number1  = Gao.number1 + self.buy1.value() - self.sell1.value()
        Gao.number2  = Gao.number2 + self.buy2.value() - self.sell2.value()
        Gao.number3  = Gao.number3 + self.buy3.value() - self.sell3.value()
        Gao.number4  = Gao.number4 + self.buy4.value() - self.sell4.value()
        self.number1.setText(str(Gao.number1))
        self.number2.setText(str(Gao.number2))
        self.number2.setText(str(Gao.number2))
        self.number2.setText(str(Gao.number2))
        
    @QtCore.pyqtSignature("")
    def on_levelok_clicked(self):
        if self.lv1.isChecked():
            Gao.level = 1
            Gao.PerCostDay = 2
            Gao.MaximumGood = 10
            RemainPlace = Gao.MaximumGood - Gao.GoodNumber
            self.remainplace.setText(str(RemainPlace))
        elif self.lv2.isChecked():
            Gao.level = 2
            Gao.PerCostDay = 5
            Gao.MaximumGood = 25
            RemainPlace = Gao.MaximumGood - Gao.GoodNumber
            self.remainplace.setText(str(RemainPlace))
        elif self.lv3.isChecked():
            Gao.level = 3
            Gao.PerCostDay = 10
            Gao.MaximumGood = 50
            RemainPlace = Gao.MaximumGood - Gao.GoodNumber
            self.remainplace.setText(str(RemainPlace))
        elif self.lv4.isChecked():
            Gao.level = 4
            Gao.PerCostDay = 20
            Gao.MaximumGood = 100
            RemainPlace = Gao.MaximumGood - Gao.GoodNumber
            self.remainplace.setText(str(RemainPlace))
        elif self.lvinf.isChecked():
            Gao.level = 5
            Gao.PerCostDay = 100
            Gao.MaximumGood = 'inf'
            self.remainplace.setText('inf')
            
    @QtCore.pyqtSignature("")
    def on_nameok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Gao()
    dlg.show()
    sys.exit(app.exec_())
