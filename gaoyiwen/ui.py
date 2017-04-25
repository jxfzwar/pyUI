# -*- coding: utf-8 -*-

import sys
import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from Ui_ui import Ui_GaoYiWen


class Gao(QtGui.QDialog, Ui_GaoYiWen):
    
    GoodNumber = 0
    GoodNumberCopy = 0
    
    MoneyPocket = 100
    MoneyPocketCopy = 100
    MoneyMarket = 0
    summoney = 100
    
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    number1copy = 0
    number2copy = 0
    number3copy = 0
    number4copy = 0
    
    price1 = 1
    price2 = 5
    price3 = 10
    price4 = 20
    
    level = 1
    PerCostDay = 2
    MaximumGood = 10
    
    name = 'username'
    
    day = 1
   
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @QtCore.pyqtSignature("")
    def on_selectagain_clicked(self):
        Gao.number1 = Gao.number1copy
        Gao.number2 = Gao.number2copy
        Gao.number3 = Gao.number3copy
        Gao.number4 = Gao.number4copy
        
        Gao.MoneyPocket = Gao.MoneyPocketCopy
        Gao.GoodNumber = Gao.GoodNumberCopy
        
        self.number1.setText(str(Gao.number1))
        self.number2.setText(str(Gao.number2))
        self.number2.setText(str(Gao.number2))
        self.number2.setText(str(Gao.number2))
        
        self.moneyleft.setText(str('$' + Gao.MoneyPocket))
        self.placeleft.setText(str(Gao.MaximumGood - Gao.GoodNumber))
        
    @QtCore.pyqtSignature("")
    def on_nextday_clicked(self):
        Gao.day = Gao.day + 1
        
        price1copy = Gao.price1
        price2copy = Gao.price2
        price3copy = Gao.price3
        price4copy = Gao.price4
        
        # need to be modified
        Gao.price1 = Gao.price1
        Gao.price2 = Gao.price2
        Gao.price3 = Gao.price3
        Gao.price4 = Gao.price4
        
        Gao.MoneyMarket = Gao.price1 * Gao.number1 + Gao.price2 * Gao.number2 + Gao.price3 * Gao.number3 + Gao.price4 * Gao.number4
        Gao.MoneyPocket = Gao.MoneyPocket - Gao.PerCostDay
        Gao.summoney = Gao.MoneyMarket + Gao.MoneyPocket
        
        updown1 = 100 * (Gao.price1 - price1copy) / price1copy
        updown2 = 100 * (Gao.price2 - price2copy) / price2copy
        updown3 = 100 * (Gao.price3 - price3copy) / price3copy
        updown4 = 100 * (Gao.price4 - price4copy) / price4copy
        
        self.day.setText(str(Gao.day))
        
        self.price1.setText('$' + str(Gao.price1))
        self.price2.setText('$' + str(Gao.price2))
        self.price3.setText('$' + str(Gao.price3))
        self.price4.setText('$' + str(Gao.price4))
        self.updown1.setText(str(updown1) + '%')
        self.updown2.setText(str(updown2) + '%')
        self.updown3.setText(str(updown3) + '%')
        self.updown4.setText(str(updown4) + '%')
        
        self.moneyleft_2.setText('$' + str(Gao.MoneyPocket))
        self.placeleft_2.setText(str(Gao.MaximumGood - Gao.GoodNumber))
        self.moneyleft_3.setText('$' + str(Gao.MoneyMarket))
        self.summoney.setText('$' + str(Gao.summoney))
        
        if Gao.day == 50:
            if Gao.summoney >= 10000:
                self.label_2.setText('CONGRADUATION! YOU WIN!')
                if os.path.exists('record'):
                    pass
                else:
                    recordinit = open('record', 'w')
                    recordinit.write('%s\n%s' % ('NULL', str(0),  'NULL'))
                    recordinit.close()
                recordread = open('record')
                record = recordread.readlines()
                recordread.close()
                if Gao.summoney > float(record[1]):
                    recordmodify = open('record','w')
                    recordmodify.write('%s\n%s' % (Gao.name, str(Gao.summoney),  'at day 50'))
                    recordmodify.close()
            else:
                self.label_2.setText('SORRY! YOU LOSE!')
                
    @QtCore.pyqtSignature("")
    def on_check_clicked(self):
        Gao.MoneyPocketCopy = Gao.MoneyPocket
        Gao.MoneyPocket = Gao.MoneyPocket + Gao.price1 * self.sell1.value() + Gao.price2 * self.sell2.value() + Gao.price3 * self.sell3.value() + Gao.price4 * self.sell4.value() \
        - Gao.price1 * self.buy1.value() - Gao.price2 * self.buy2.value() - Gao.price3 * self.buy3.value() - Gao.price4 * self.buy4.value()
        
        Gao.GoodNumberCopy = Gao.GoodNumber
        Gao.GoodNumber = Gao.GoodNumber - self.sell1.value() - self.sell2.value() - self.sell3.value() - self.sell4.value() \
        + self.buy1.value() + self.buy2.value() + self.buy3.value() + self.buy4.value()
        
        self.moneyleft.setText('$' + str(Gao.MoneyPocket))
        self.placeleft.setText(str(Gao.MaximumGood - Gao.GoodNumber))
        
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText,QtCore.Qt.blue) 
        qe = QtGui.QPalette()
        qe.setColor(QtGui.QPalette.WindowText,QtCore.Qt.red)
        if Gao.MaximumGood == 'inf':
            if Gao.MoneyPocket >= Gao.PerCostDay:
                self.afterdayresult_2.setText('No probelm! You can click next day or select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.MoneyPocket < Gao.PerCostDay and Gao.MoneyPocket >=0:
                self.afterdayresult_2.setText('No money for storage! Select again!')
                self.afterdayresult_2.setPalette(qe) 
            elif Gao.MoneyPocket < 0:
                self.afterdayresult_2.setText('No enough money for buy and sell! Select again!')
                self.afterdayresult_2.setPalette(qe) 
        else:
            if Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket >= Gao.PerCostDay:
                self.afterdayresult_2.setText('No probelm! You can click next day or select again!')
                self.afterdayresult_2.setPalette(pe) 
            elif Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket < Gao.PerCostDay and Gao.MoneyPocket >= 0:
                self.afterdayresult_2.setText('No money for storage! Select again!')
                self.afterdayresult_2.setPalette(qe) 
            elif Gao.GoodNumber <= Gao.MaximumGood and Gao.MoneyPocket < 0:
                self.afterdayresult_2.setText('No enough money for buy and sell! Select again!')
                self.afterdayresult_2.setPalette(qe) 
            elif Gao.GoodNumber > Gao.MaximumGood:
                self.afterdayresult_2.setText('No enough place for storage! Select again!')
                self.afterdayresult_2.setPalette(qe) 
                
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
        Gao.name = self.name.text()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Gao()
    dlg.show()
    sys.exit(app.exec_())
