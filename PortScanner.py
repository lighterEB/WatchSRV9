# -*- coding: utf-8 -*-

# Date：2018-12-16
#
# Created by: Hu Shangpengcheng
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from MainWin import Ui_MainWindow
from ChildWin import Ui_Dialog
from GetDate import DateGet
from PyQt5.QtCore import *

class MainForm(QMainWindow,  Ui_MainWindow):
    def __init__(self):
        super(MainForm,  self).__init__()
        self.setupUi(self)

        self.action_C.triggered.connect(self.childShow)
        self.action_O_2.triggered.connect(self.childShow1)
        self.timer = QTimer(self)       
        self.timer.start(1000)

        self.timer.timeout.connect(self.showTime)
    
        
    
    def showTime(self):
        txt = '''     更新维护by：DaddyHu_CN'''
        time =  QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.author.setText(txt+'\n'+timeDisplay)
                
    def childShow(self):
        self.child = ChildrenForm()
        self.child.show()
    
    def childShow1(self):
        self.child1 = DateGet()
        self.child1.show()
    
class ChildrenForm(QWidget,  Ui_Dialog):
    def __init__(self):
        super(ChildrenForm,  self).__init__()
        self.setupUi(self)
        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
