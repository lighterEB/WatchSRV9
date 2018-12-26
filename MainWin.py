# -*- coding: utf-8 -*-

# Date：2018-12-16
#
# Created by: Hu Shangpengcheng
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time, winsound, requests, socket, configparser,  base64, json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 580)
        MainWindow.setMinimumSize(QtCore.QSize(940, 580))
        MainWindow.setWindowIcon(QtGui.QIcon('asktao.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 0, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 0, 3, 1, 1)
        self.tableWidget_7=QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_7.setObjectName("treeWidget_7")
        self.gridLayout_3.addWidget(self.tableWidget_7, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setShowGrid(False)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_8)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_8.addWidget(self.pushButton_22, 0, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_8.addWidget(self.pushButton_23, 0, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_8.addWidget(self.pushButton_24, 0, 3, 1, 1)
        self.tableWidget_8=QtWidgets.QTableWidget(self.groupBox_8)
        self.tableWidget_8.setObjectName("treeWidget_8")
        self.gridLayout_8.addWidget(self.tableWidget_8, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_8, 0, 1, 1, 1)
        self.tableWidget_8.setColumnCount(5)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 0, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 0, 3, 1, 1)
        self.tableWidget_4=QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_4.setObjectName("treeWidget_4")
        self.gridLayout_4.addWidget(self.tableWidget_4, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_7.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_7.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 0, 3, 1, 1)
        self.tableWidget_3=QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_3.setObjectName("treeWidget_3")
        self.gridLayout_7.addWidget(self.tableWidget_3, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 0, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_5.addWidget(self.pushButton_17, 0, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_5.addWidget(self.pushButton_18, 0, 3, 1, 1)
        self.tableWidget_6=QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget_6.setObjectName("treeWidget_6")
        self.gridLayout_5.addWidget(self.tableWidget_6, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.tableWidget_6.setColumnCount(5)
        self.tableWidget_6.setShowGrid(False)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_6.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_6.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_6.addWidget(self.pushButton_15, 0, 3, 1, 1)
        self.tableWidget_5=QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_5.setObjectName("treeWidget_5")
        self.gridLayout_6.addWidget(self.tableWidget_5, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox_5, 2, 1, 1, 1)
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.setHorizontalHeaderLabels(['IP', '服务器名称', '端口', '发生时间', '错误信息' ])
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_P = QtWidgets.QMenu(self.menubar)
        self.menu_P.setObjectName("menu_P")
        self.menu_T = QtWidgets.QMenu(self.menubar)
        self.menu_T.setObjectName("menu_T")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("问道端口扫描第九版")
        self.closeWindow = QtWidgets.QAction(MainWindow)
        self.closeWindow.setObjectName("closeWindow")
        self.action_C = QtWidgets.QAction(MainWindow)
        self.action_C.setObjectName("action_C")
        self.action_P = QtWidgets.QAction(MainWindow)
        self.action_P.setObjectName("action_P")
        self.action_S = QtWidgets.QAction(MainWindow)
        self.action_S.setObjectName("action_S")
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_F = QtWidgets.QAction(MainWindow)
        self.action_F.setObjectName("action_F")
        self.action_A = QtWidgets.QAction(MainWindow)
        self.action_A.setObjectName("action_A")
        self.action_O_2 = QtWidgets.QAction(MainWindow)
        self.action_O_2.setObjectName("action_O_2")
        self.menu.addSeparator()
        self.menu.addAction(self.closeWindow)
        self.menu_P.addAction(self.action_C)
        self.menu_T.addAction(self.action_P)
        self.menu_T.addAction(self.action_S)
        self.menu_T.addAction(self.action_O)
        self.menu_T.addAction(self.action_F)
        self.menu_H.addAction(self.action_A)
        self.menu_H.addAction(self.action_O_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_P.menuAction())
        self.menubar.addAction(self.menu_T.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.pushButton_20.setEnabled(False)
        self.pushButton_23.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        
        self.tableWidget_7.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_8.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_8.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        
        self.retranslateUi(MainWindow)
        
        QToolTip.setFont(QtGui.QFont("微软雅黑", 10))
        self.action_P.setStatusTip("开启所有端口扫描")
        self.action_S.setStatusTip("关闭所有端口扫描")
        self.action_O.setStatusTip("打开所有声音")
        self.action_F.setStatusTip("关闭所有声音")
        txt = '''     更新维护by：DaddyHu_CN'''
        time =  QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.author = QLabel(txt+'\n'+timeDisplay)
        self.statusbar.addPermanentWidget(self.author)
        
        self.action_A.triggered.connect(self.tips)

        #初始化线程
        self.thread = ScannerCcs1(False)
        self.thread1 = ScannerCcs2(False)
        self.thread2 = ScannerCcs3(False)
        self.thread3 = ScannerCcs4(False)
        self.thread4 = ScannerGs(False)
        self.thread5 = ScannerCcs5(False)
        
        

        


    
        #关闭窗口
        self.closeWindow.triggered.connect(self.close)
        
        #开启扫描
        self.pushButton_19.clicked.connect(self.optionBtn1Start) 
        self.pushButton_22.clicked.connect(self.optionBtn2Start)
        self.pushButton_10.clicked.connect(self.optionBtn3Start)
        self.pushButton_7.clicked.connect(self.optionBtn4Start)
        self.pushButton_16.clicked.connect(self.optionBtn5Start)
        self.pushButton_13.clicked.connect(self.optionBtn6Start)
        
        #关闭扫描
        self.pushButton_20.clicked.connect(self.optionBtn1Stop)
        self.pushButton_23.clicked.connect(self.optionBtn2Stop)
        self.pushButton_11.clicked.connect(self.optionBtn3Stop)
        self.pushButton_8.clicked.connect(self.optionBtn4Stop)
        self.pushButton_17.clicked.connect(self.optionBtn5Stop)
        self.pushButton_14.clicked.connect(self.optionBtn6Stop)
        
        #打开声音
        self.pushButton_21.clicked.connect(self.openWav1)
        self.pushButton_24.clicked.connect(self.openWav2)
        self.pushButton_12.clicked.connect(self.openWav3)
        self.pushButton_9.clicked.connect(self.openWav4)
        self.pushButton_18.clicked.connect(self.openWav5)
        self.pushButton_15.clicked.connect(self.openWav6)
   

        #打开所有声音
        self.action_O.triggered.connect(self.openAllWav)  
        
        #关闭所有声音
        self.action_F.triggered.connect(self.closeAllWav)  
        
        #打开所有扫描
        self.action_P.triggered.connect(self.allScan)
        
        #关闭所有扫描
        self.action_S.triggered.connect(self.allStop)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def closeEvent(self,  event):
        self.msgBox = QMessageBox(QMessageBox.Question, '提示', '日志可以在ErrorLogs文件夹查看，是否退出问道端口扫描？')
        self.msgBox.setWindowIcon(QtGui.QIcon('asktao.ico'))
        self.msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        okBtn = self.msgBox.button(QMessageBox.Yes)
        okBtn.setText('先走一步')
        noBtn = self.msgBox.button(QMessageBox.No)
        noBtn.setText('我再想想')
        self.msgBox.exec_()
        if self.msgBox.clickedButton() == okBtn:
            event.accept()
        elif self.msgBox.clickedButton() == noBtn:
            event.ignore()

        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "《》端口扫描程序"))
        self.groupBox_7.setTitle(_translate("MainWindow", "<AAA_8001>"))
        self.label.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_19.setText(_translate("MainWindow", "扫描"))
        self.pushButton_20.setText(_translate("MainWindow", "停止"))
        self.pushButton_21.setText(_translate("MainWindow", "打开声音"))
        
        

        self.groupBox_8.setTitle(_translate("MainWindow", "<DBA_9030>"))
        self.label_6.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_22.setText(_translate("MainWindow", "扫描"))
        self.pushButton_23.setText(_translate("MainWindow", "停止"))
        self.pushButton_24.setText(_translate("MainWindow", "打开声音"))

        self.groupBox_4.setTitle(_translate("MainWindow", "<SPA_9040>"))
        self.label_2.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_10.setText(_translate("MainWindow", "扫描"))
        self.pushButton_11.setText(_translate("MainWindow", "停止"))
        self.pushButton_12.setText(_translate("MainWindow", "打开声音"))

        self.groupBox_3.setTitle(_translate("MainWindow", "<CCS_9020>"))
        self.label_5.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_7.setText(_translate("MainWindow", "扫描"))
        self.pushButton_8.setText(_translate("MainWindow", "停止"))
        self.pushButton_9.setText(_translate("MainWindow", "打开声音"))

        self.groupBox_6.setTitle(_translate("MainWindow", "<GS_9010>"))
        self.label_3.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_16.setText(_translate("MainWindow", "扫描"))
        self.pushButton_17.setText(_translate("MainWindow", "停止"))
        self.pushButton_18.setText(_translate("MainWindow", "打开声音"))

        self.groupBox_5.setTitle(_translate("MainWindow", "<TTS_9050>"))
        self.label_4.setText(_translate("MainWindow", "准备扫描..."))
        self.pushButton_13.setText(_translate("MainWindow", "扫描"))
        self.pushButton_14.setText(_translate("MainWindow", "停止"))
        self.pushButton_15.setText(_translate("MainWindow", "打开声音"))

        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_P.setTitle(_translate("MainWindow", "配置(&P)"))
        self.menu_T.setTitle(_translate("MainWindow", "扫描(&T)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.closeWindow.setText(_translate("MainWindow", "退出(&X)"))
        self.closeWindow.setShortcut(_translate("MainWindow", "Alt+X"))
        self.action_C.setText(_translate("MainWindow", "配置区组信息(&C)"))
        self.action_P.setText(_translate("MainWindow", "全部扫描(&P)"))
        self.action_S.setText(_translate("MainWindow", "全部停止(&S)"))
        self.action_O.setText(_translate("MainWindow", "打开声音(&O)"))
        self.action_F.setText(_translate("MainWindow", "关闭声音(&F)"))
        self.action_A.setText(_translate("MainWindow", "关于(&A)"))
        self.action_O_2.setText(_translate("MainWindow", "日志信息查询(&O)"))
        
    def playAlert(self, text):
        if text == 'p':
            if self.pushButton_21.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)

    def playAlert1(self, text):
        if text == 'p':
            if self.pushButton_24.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)

    def playAlert2(self, text):
        if text == 'p':
            if self.pushButton_12.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)

    def playAlert3(self, text):
        if text == 'p':
            if self.pushButton_9.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)

    def playAlert4(self, text):
        if text == 'p':
            if self.pushButton_18.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)
         
    def playAlert5(self, text):
        if text == 'p':
            if self.pushButton_15.text() == '关闭声音':
                winsound.PlaySound('alert', winsound.SND_ASYNC)

        
        
    
    def allScan(self):
        self.optionBtn1Start()
        self.optionBtn2Start()
        self.optionBtn3Start()
        self.optionBtn4Start()
        self.optionBtn5Start()
        self.optionBtn6Start()
    
    def allStop(self):
        self.optionBtn1Stop()
        self.optionBtn2Stop()
        self.optionBtn3Stop()
        self.optionBtn4Stop()
        self.optionBtn5Stop()
        self.optionBtn6Stop()
        

    #设置所有关闭开关    
    def optionBtn1Start(self):#1
        self.pushButton_20.setEnabled(True)
        self.pushButton_19.setEnabled(False)
        self.thread = ScannerCcs1(True)
        self.thread.start()
        self.thread.sinOut.connect(self.refreshLabel)
        self.thread.sinOut1.connect(self.fshText)
        self.thread.sinOut2.connect(self.freshText)
        self.thread.sinOut3.connect(self.playAlert)
        

            
    
    def optionBtn2Start(self):#2
        self.pushButton_23.setEnabled(True)
        self.pushButton_22.setEnabled(False)
        self.thread1 = ScannerCcs2(True)
        self.thread1.start()
        self.thread1.sinOut.connect(self.refreshLabel1)
        self.thread1.sinOut2.connect(self.freshText1)
        self.thread1.sinOut1.connect(self.fshText)
        self.thread1.sinOut3.connect(self.playAlert1)


    def optionBtn3Start(self):#3
        self.pushButton_11.setEnabled(True)
        self.pushButton_10.setEnabled(False)
        self.thread2 = ScannerCcs3(True)
        self.thread2.start()
        self.thread2.sinOut.connect(self.refreshLabel2)
        self.thread2.sinOut2.connect(self.freshText2)
        self.thread2.sinOut1.connect(self.fshText)
        self.thread2.sinOut3.connect(self.playAlert2)


    def optionBtn4Start(self):#4
        self.pushButton_8.setEnabled(True)
        self.pushButton_7.setEnabled(False)
        self.thread3 = ScannerCcs4(True)
        self.thread3.start()
        self.thread3.sinOut.connect(self.refreshLabel3)
        self.thread3.sinOut2.connect(self.freshText3)
        self.thread3.sinOut1.connect(self.fshText)
        self.thread3.sinOut3.connect(self.playAlert3)


    def optionBtn5Start(self):#5
        self.pushButton_17.setEnabled(True)
        self.pushButton_16.setEnabled(False)
        self.thread4 = ScannerGs(True)
        self.thread4.start()
        self.thread4.sinOut.connect(self.refreshLabel4)
        self.thread4.sinOut2.connect(self.freshText4)
        self.thread4.sinOut1.connect(self.fshText)
        self.thread4.sinOut3.connect(self.playAlert4)
        

    def optionBtn6Start(self):#6
        self.pushButton_14.setEnabled(True)
        self.pushButton_13.setEnabled(False)
        self.thread5 = ScannerCcs5(True)
        self.thread5.start()
        self.thread5.sinOut.connect(self.refreshLabel5)
        self.thread5.sinOut2.connect(self.freshText5)
        self.thread5.sinOut1.connect(self.fshText)
        self.thread5.sinOut3.connect(self.playAlert5)
        
    
    #设置所有停止开关
    def optionBtn1Stop(self):
        self.thread.stop()
        try:
            self.thread.sinOut1.disconnect(self.fshText)
            self.thread1.sinOut.disconnect(self.refreshLabel)
            self.thread2.sinOut2.disconnect(self.freshText)
        except:
            pass
        self.pushButton_20.setEnabled(False)
        self.pushButton_19.setEnabled(True)
        self.label.setText("准备扫描...")

    def optionBtn2Stop(self):
        self.thread1.stop()
        try:
            self.thread1.sinOut1.disconnect(self.fshText)
            self.thread1.sinOut.disconnect(self.refreshLabel1)
            self.thread1.sinOut2.disconnect(self.freshText1)
        except:
            pass
        self.pushButton_23.setEnabled(False)
        self.pushButton_22.setEnabled(True)
        self.label_6.setText("准备扫描...")
    
    def optionBtn3Stop(self):
        self.thread2.stop()
        try:
            self.thread2.sinOut1.disconnect(self.fshText)
            self.thread2.sinOut.disconnect(self.refreshLabel2)
            self.thread2.sinOut2.disconnect(self.freshText2)
        except:
            pass
        self.pushButton_11.setEnabled(False)
        self.pushButton_10.setEnabled(True)
        self.label_2.setText("准备扫描...")

    def optionBtn4Stop(self):
        self.thread3.stop()
        try:
            self.thread3.sinOut1.disconnect(self.fshText)
            self.thread3.sinOut.disconnect(self.refreshLabel3)
            self.thread3.sinOut2.disconnect(self.freshText3)
        except:
            pass
        self.pushButton_8.setEnabled(False)
        self.pushButton_7.setEnabled(True)
        self.label_5.setText("准备扫描...")
    
    def optionBtn5Stop(self):
        self.thread4.stop()
        try:
            self.thread4.sinOut1.disconnect(self.fshText)
            self.thread4.sinOut.disconnect(self.refreshLabel4)
            self.thread4.sinOut2.disconnect(self.freshText4)
        except:
            pass
        self.pushButton_17.setEnabled(False)
        self.pushButton_16.setEnabled(True)
        self.label_3.setText("准备扫描...")
    
    def optionBtn6Stop(self):
        self.thread5.stop()
        try:
            self.thread5.sinOut1.disconnect(self.fshText)
            self.thread5.sinOut.disconnect(self.refreshLabel5)
            self.thread5.sinOut2.disconnect(self.freshText5)
        except:
            pass
        self.pushButton_14.setEnabled(False)
        self.pushButton_13.setEnabled(True)
        self.label_4.setText("准备扫描...")
    

                

        
    
    def fshText(self, text):
        if text == 'e':
            self.allStop()
            self.msgBox = QMessageBox(QMessageBox.Information , "问道端口扫描", "请检查网络连接！")
            self.msgBox.setWindowIcon(QtGui.QIcon('asktao.ico'))
            self.reply = self.msgBox.addButton(self.tr("确定"),  QMessageBox.YesRole)
            self.msgBox.show()
            
        
    def freshText(self,  val):
        self.tableWidget_7.clearContents()
        self.tableWidget_7.setRowCount(len(val))
        self.tableWidget_7.setUpdatesEnabled(False)
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('8001')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_7.setItem(i, 0, ip )
            self.tableWidget_7.setItem(i, 1, appName )
            self.tableWidget_7.setItem(i, 2, appPort)
            self.tableWidget_7.setItem(i, 3, htime )
            self.tableWidget_7.setItem(i, 4, eInfo )
        self.tableWidget_7.setUpdatesEnabled(True)
    
    def freshText1(self,  val):
        self.tableWidget_8.clearContents()
        self.tableWidget_8.setRowCount(len(val))
        self.tableWidget_8.setUpdatesEnabled(False)
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('9030')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_8.setItem(i, 0, ip )
            self.tableWidget_8.setItem(i, 1, appName )
            self.tableWidget_8.setItem(i, 2, appPort)
            self.tableWidget_8.setItem(i, 3, htime )
            self.tableWidget_8.setItem(i, 4, eInfo )
        self.tableWidget_8.setUpdatesEnabled(True)
            
    def freshText2(self,  val):
        self.tableWidget_4.clearContents()
        self.tableWidget_4.setRowCount(len(val))
        self.tableWidget_4.setUpdatesEnabled(False)
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('9040')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_4.setItem(i, 0, ip )
            self.tableWidget_4.setItem(i, 1, appName )
            self.tableWidget_4.setItem(i, 2, appPort)
            self.tableWidget_4.setItem(i, 3, htime )
            self.tableWidget_4.setItem(i, 4, eInfo )
        self.tableWidget_4.setUpdatesEnabled(True)

    def freshText3(self,  val):
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(len(val))
        self.tableWidget_3.setUpdatesEnabled(False)
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('9020')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(i, 0, ip )
            self.tableWidget_3.setItem(i, 1, appName )
            self.tableWidget_3.setItem(i, 2, appPort)
            self.tableWidget_3.setItem(i, 3, htime )
            self.tableWidget_3.setItem(i, 4, eInfo )
        self.tableWidget_3.setUpdatesEnabled(True)

    def freshText4(self,  val):
        self.tableWidget_6.clearContents()
        self.tableWidget_6.setRowCount(len(val))
        self.tableWidget_6.setUpdatesEnabled(False)
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('9010')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_6.setItem(i, 0, ip )
            self.tableWidget_6.setItem(i, 1, appName )
            self.tableWidget_6.setItem(i, 2, appPort)
            self.tableWidget_6.setItem(i, 3, htime )
            self.tableWidget_6.setItem(i, 4, eInfo )
        self.tableWidget_6.setUpdatesEnabled(True)
    
    def freshText5(self,  val):
        self.tableWidget_5.clearContents()
        self.tableWidget_5.setRowCount(len(val))
        for i in range(len(val)):
            ip = QTableWidgetItem(val[i][0]) 
            appName = QTableWidgetItem(val[i][1])
            appPort = QTableWidgetItem('9050')
            htime = QTableWidgetItem(val[i][3])
            eInfo = QTableWidgetItem(val[i][4])
            ip.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appName.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            appPort.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            htime.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setForeground(QtGui.QBrush(QtGui.QColor(255,  0 , 0)))
            eInfo.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_5.setItem(i, 0, ip )
            self.tableWidget_5.setItem(i, 1, appName )
            self.tableWidget_5.setItem(i, 2, appPort)
            self.tableWidget_5.setItem(i, 3, htime )
            self.tableWidget_5.setItem(i, 4, eInfo )
            
            
    def refreshLabel(self,  val):
        self.label.setText(val[0] +"  "+ str(val[1]))
    
    def refreshLabel1(self,  val):
        self.label_6.setText(val[0] +"  "+ str(val[1]))
    
    def refreshLabel2(self,  val):
        self.label_2.setText(val[0] +"  "+ str(val[1]))
    
    def refreshLabel3(self,  val):
        self.label_5.setText(val[0] +"  "+ str(val[1]))
    
    def refreshLabel4(self,  val):
        self.label_3.setText(val[0] +"  "+ val[1])
    
    def refreshLabel5(self,  val):
        self.label_4.setText(val[0] +"  "+ str(val[1]))
    
    
    
    def openWav1(self):
        if self.pushButton_21.text() == "打开声音":
            self.pushButton_21.setText("关闭声音")
        else:
            self.pushButton_21.setText("打开声音")
    
    def openWav2(self):
        if self.pushButton_24.text() == "打开声音":
            self.pushButton_24.setText("关闭声音")
        else:
            self.pushButton_24.setText("打开声音")
    
    def openWav3(self):
        if self.pushButton_12.text() == "打开声音":
            self.pushButton_12.setText("关闭声音")
        else:
            self.pushButton_12.setText("打开声音")
    
    def openWav4(self):
        if self.pushButton_9.text() == "打开声音":
            self.pushButton_9.setText("关闭声音")
        else:
            self.pushButton_9.setText("打开声音")
    
    def openWav5(self):
        if self.pushButton_18.text() == "打开声音":
            self.pushButton_18.setText("关闭声音")
        else:
            self.pushButton_18.setText("打开声音")
    
    def openWav6(self):
        if self.pushButton_15.text() == "打开声音":
            self.pushButton_15.setText("关闭声音")
        else:
            self.pushButton_15.setText("打开声音")
    
    
    def openAllWav(self):
        self.pushButton_21.setText("关闭声音")
        self.pushButton_24.setText("关闭声音")
        self.pushButton_12.setText("关闭声音")
        self.pushButton_9.setText("关闭声音")
        self.pushButton_18.setText("关闭声音")
        self.pushButton_15.setText("关闭声音")

    def closeAllWav(self):
        self.pushButton_21.setText("打开声音")
        self.pushButton_24.setText("打开声音")
        self.pushButton_12.setText("打开声音")
        self.pushButton_9.setText("打开声音")
        self.pushButton_18.setText("打开声音")
        self.pushButton_15.setText("打开声音")
    
    def tips(self):
        doc =  '''
1、所有错误记录均保存在ErrorLog文件夹的以日期命名的log文件中,您可以在程序内按日期查询错误记录。
2、更改了区组获取方式，新增了排除区组的功能，优化了扫描线程。
3、默认报警声音未开启，可以手动开启报警提示。
                                
                                       
                                              2018-12-16'''
        self.msg = QMessageBox(QMessageBox.Information,"说明", doc )
        self.msg.setWindowIcon(QtGui.QIcon('asktao.ico'))
        self.reply = self.msg.addButton(self.tr("确定"), QMessageBox.YesRole)
        self.msg.exec_()

class findConfig:
    def visitUrl():
        conlist = []
        config = configparser.ConfigParser()
        config.read('WatchSvr.ini')
        host = base64.b64decode(config['global']['ccs_info'][9:]).decode('utf-8')
        user = base64.b64decode(config['global']['wd_gm_line'][9:]).decode('utf-8')
        passwd = base64.b64decode(config['global']['preprocessing_info'][9:]).decode('utf-8')
        app_name = base64.b64decode(config['global']['excepted'][9:]).decode('utf-8')
        conlist.append(host)
        conlist.append(user)
        conlist.append(passwd)
        conlist.append(app_name)
        return conlist

    
class ScannerGs(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerGs, self).__init__()
        self.working = True
    
    def stop(self):
        self.working = False

        
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[1], timeout=(3, 7))
                soup = res.text
                txt = json.loads(soup)
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                expected = app_list[3] + expected.strip('[]')
                line = txt['data'].strip('[]')
                line = eval(line)
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], a[i]['port_num']])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                s.connect((str(a[j]['ip']),int(a[j]['port_num'])))
                                s.close()
                            except socket.error as e:
                                s.close()
                                errcount += 1
                                if errcount == 3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')[0] + einfo.split(' ')[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], a[j]['port_num'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], a[j]['port_num'], a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
    
                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')
        


class ScannerCcs1(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerCcs1, self).__init__()
        self.working = working
    
    def stop(self):
        self.working = False
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[0], timeout=(3, 7))
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                expected = app_list[3] + expected.strip('[]')
                soup = res.text
                txt = json.loads(soup)
                line = txt['data'].strip('[]')
                line = eval(line)
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], 8001])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                else:
                                    s.connect((a[j]['ip'], 8001))
                                    s.close()
                            except socket.error as e:
                                s.close()
                                errcount += 1
                                if errcount == 3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')
                                    einfo = einfo[0] + einfo[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], 8001, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], 8001, a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
                                    
                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')

class ScannerCcs2(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerCcs2, self).__init__()
        self.working = True
    
    def stop(self):
        self.working = False
        
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[0], timeout=(3, 7))
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                soup = res.text
                txt = json.loads(soup)
                line = txt['data'].strip('[]')
                line = eval(line)
                expected = app_list[3] + expected.strip('[]')
            
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], 9030])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                else:
                                    s.connect((a[j]['ip'], 9030))
                                    s.close()
                            except socket.error as e:
                                s.close()
                                errcount += 1
                                if errcount==3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')
                                    einfo = einfo[0] + einfo[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], 9030, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], 9030, a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
    
                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')

class ScannerCcs3(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerCcs3, self).__init__()
        self.working = True
    
    def stop(self):
        self.working = False
        
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[0], timeout=(3, 7))
                soup = res.text
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                expected = app_list[3] + expected.strip('[]')
                txt = json.loads(soup)
                line = txt['data'].strip('[]')
                line = eval(line)
                
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], 9040])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
    
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                else:
                                    s.connect((a[j]['ip'], 9040))
                                    s.close()
                            except socket.error as e:
                                errcount += 1
                                if errcount == 3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')
                                    einfo = einfo[0] + einfo[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], 9040, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], 9040, a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
                                        
                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')

class ScannerCcs4(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerCcs4, self).__init__()
        self.working = True
    
    def stop(self):
        self.working = False

        
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[0], timeout=(3, 7))
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                expected = app_list[3] + expected.strip('[]')
                soup = res.text
                txt = json.loads(soup)
                line = txt['data'].strip('[]')
                line = eval(line)
                
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], 9020])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                else:
                                    s.connect((a[j]['ip'], 9020))
                                    s.close()
                            except socket.error as e:
                                s.close()
                                errcount += 1
                                if errcount == 3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')
                                    einfo = einfo[0] + einfo[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], 9020, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], 9020, a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
                    

                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')

class ScannerCcs5(QThread):
    sinOut = pyqtSignal(list)
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(str)
    
    def __init__(self, working):
        super(ScannerCcs5, self).__init__()
        self.working = True
    
    def stop(self):
        self.working = False
        
    
    def run(self):
        if self.working == True:
            try:
                app_list = findConfig.visitUrl()
                res = requests.get(app_list[0], timeout=(3, 7))
                soup = res.text
                txt = json.loads(soup)
                line = txt['data'].strip('[]')
                line = eval(line)
                expected = requests.get(app_list[2], timeout=(3, 7))
                expected = json.loads(expected.text)['data']
                expected = app_list[3] + expected.strip('[]')
                
                while self.working == True:
                    count = 0
                    for i in range(10):
                        try:
                            requests.get(app_list[1], timeout=(3, 7))
                        except:
                            count += 1
                    if count == 10:
                        self.sinOut1.emit('e')
                    a=[]
                    errorinfo = []
                
                    for i in range(len(line)):
                        a.append(line[i])
                        self.sinOut.emit([a[i]['ip'], 9050])
                        time.sleep(0.01)
                    self.sinOut.emit(['0', ' '])
                    for j in range(len(a)):
                        errcount = 0
                        for x in range(3):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                if a[j]['sub_name'] in expected:
                                    pass
                                else:
                                    s.connect((a[j]['ip'], 9050))
                                    s.close()
                            except socket.error as e:
                                s.close()
                                errcount += 1
                                if errcount == 3:
                                    einfo = str(e)
                                    einfo = einfo.split(' ')
                                    einfo = einfo[0] + einfo[1]
                                    errorinfo.append([a[j]['ip'], a[j]['sub_name'], 9050, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), einfo])
                                    with open('ErrorLog\%s.log' % time.strftime("%Y-%m-%d", time.localtime()), 'a+') as f:
                                        f.write('{0:{5}^10}\t{1:{5}^10}\t{2:{5}^6}\t{3:{5}^6}\t{4:{5}^6}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), a[j]['ip'], 9050, a[j]['sub_name'], einfo, chr(12288)))
                                        f.close()
    
                    self.sinOut2.emit(errorinfo)
                    if len(errorinfo):
                        self.sinOut3.emit('p')
                    time.sleep(10)
            except:
                self.sinOut1.emit('e')

        

           
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

