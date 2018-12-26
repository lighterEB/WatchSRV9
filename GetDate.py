# -*- coding: utf-8 -*-

# Date：2018-12-16
#
# Created by: Hu Shangpengcheng
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


import sys, os, subprocess


class DateGet(QWidget):
    def __init__(self,  parent=None):
        super(DateGet,  self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('选择日期')
        self.setWindowIcon(QtGui.QIcon('asktao.ico'))
        self.resize(180,  90)
        self.setMinimumSize(180,  90)
        self.setMaximumSize(180,  90)
        self.setWindowModality(Qt.ApplicationModal)
        vlayout = QVBoxLayout()
        self.dateEdit =QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(12)
        font.setWeight(200)
        self.dateEdit.setFont(font)
        self.okBtn = QPushButton('确定')
        vlayout.addWidget( self.dateEdit)
        vlayout.addWidget( self.okBtn)
        self.dateEdit.setCalendarPopup( True)
        self.setLayout(vlayout)
        
        
        self.okBtn.clicked.connect(self.updateInfo)
        
        
        
        
    def updateInfo(self):
        a = self.dateEdit.text().strip(' ')
        if os.path.exists('ErrorLog\\%s.log'%a):
            subprocess.Popen(['NOTEPAD', "ErrorLog\\%s.log"%a])
            
        else:
            self.msgBox = QMessageBox(QMessageBox.Warning,  "错误",  "您选择的日期没有日志信息。")
            self.msgBox.setWindowIcon(QIcon('asktao.ico'))
            self.reply = self.msgBox.addButton(self.tr("确定"),  QMessageBox.YesRole)
            self.msgBox.exec_()
        


        
        





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DateGet()
    win.show()
    sys.exit(app.exec_())
