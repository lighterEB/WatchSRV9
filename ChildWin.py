# -*- coding: utf-8 -*-

# Date：2018-12-16
#
# Created by: Hu Shangpengcheng
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import configparser,  base64,  string,  random,  sys,  re,  requests

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setWindowIcon(QtGui.QIcon('asktao.ico'))
        Dialog.resize(390, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(390, 200))
        Dialog.setMaximumSize(QtCore.QSize(390, 200))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setWhatsThis("")
        self.dbHost = QtWidgets.QLineEdit(Dialog)
        self.dbHost.setGeometry(QtCore.QRect(171, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dbHost.setFont(font)
        self.dbHost.setText(self.getConfig()[0])
        #self.dbHost.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dbHost.setObjectName("dbHost")
        self.dbUser = QtWidgets.QLineEdit(Dialog)
        self.dbUser.setGeometry(QtCore.QRect(171, 50, 211, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dbUser.setFont(font)
        #self.dbUser.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dbUser.setText(self.getConfig()[1])
        self.dbUser.setObjectName("dbUser")
        self.dbPaswd = QtWidgets.QLineEdit(Dialog)
        self.dbPaswd.setGeometry(QtCore.QRect(171, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dbPaswd.setFont(font)
        self.dbPaswd.setText(self.getConfig()[2])
        #self.dbPaswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dbPaswd.setObjectName("dbPaswd")
        self.dbSec = QtWidgets.QLineEdit(Dialog)
        self.dbSec.setGeometry(QtCore.QRect(170, 110, 211, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dbSec.setFont(font)
        self.dbSec.setObjectName("dbSec")
        self.dbSec.setText(self.getConfig()[3])
        self.dbSec.setPlaceholderText('多个区组请以逗号分隔')
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 17, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 47, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 77, 120, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 107, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.okBtn = QtWidgets.QPushButton(Dialog)
        self.okBtn.setGeometry(QtCore.QRect(70, 150, 101, 31))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(220, 150, 101, 31))
        self.cancelBtn.setObjectName("cancelBtn")
        self.retranslateUi(Dialog)
        self.cancelBtn.clicked.connect(self.close)
        self.okBtn.clicked.connect(self.setConfig)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "区组信息配置"))
        self.label_3.setText(_translate("Dialog", "区组地址："))
        self.label_4.setText(_translate("Dialog", "游戏线地址："))
        self.label_5.setText(_translate("Dialog", "预处理区组地址："))
        self.label_6.setText(_translate("Dialog", "排除扫描区组："))
        self.okBtn.setText(_translate("Dialog", "确定"))
        self.cancelBtn.setText(_translate("Dialog", "取消"))
    
    def getConfig(self):
        conlist = []
        try:
            config = configparser.ConfigParser()
            config.read('WatchSvr.ini')
            host = base64.b64decode(config['global']['ccs_info'][9:]).decode('utf-8')
            user = base64.b64decode(config['global']['wd_gm_line'][9:]).decode('utf-8')
            passwd = base64.b64decode(config['global']['preprocessing_info'][9:]).decode('utf-8')
            time_out = base64.b64decode(config["global"]['excepted'][9:]).decode('utf-8')
            conlist.append(host)
            conlist.append(user)
            conlist.append(passwd)
            conlist.append(time_out)
            return conlist
        except:
            pass
    
    def genKey(self):
        gen_key = string.ascii_letters + string.digits
        return ''.join([ random.choice(gen_key) for i in range(9)])
    
    
    def setConfig(self):
        global host
        info = []
        puts = []
        complex = re.compile('(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?')
        host = self.dbHost.text()
        info.append(host)
        user = self.dbUser.text()
        info.append(user)
        pd = self.dbPaswd.text()
        info.append(pd)
        sec = self.dbSec.text()
        info.append(sec)
        for i in range(4):
                j = self.genKey() + base64.b64encode(info[i].encode('utf-8')).decode('utf-8')
                puts.append(j)
        if '' not in info[0:3] and complex.match(host) is not None and complex.match(user) is not None and complex.match(pd) is not None:
            config = configparser.ConfigParser()
            config.read('WatchSvr.ini')
            config.set('global', 'ccs_info', puts[0])
            config.set('global', 'wd_gm_line', puts[1])
            config.set('global', 'preprocessing_info', puts[2])
            config.set('global', 'excepted', puts[3])
            config.write(open('WatchSvr.ini',  'w'))
            self.yesOrNo()
            
        else:
            self.promptsFormFalse()


        
    
    def yesOrNo(self):
        self.thread = visitUrl()
        self.thread.trigger.connect(self.promptsFormTrue)
        self.thread.start()
    
    
    def promptsFormTrue(self,  text):
        if text == 'ok':
            self.msgBox = QMessageBox(QMessageBox.Information , "问道端口扫描", "区组信息配置修改成功！")
            self.reply = self.msgBox.addButton(self.tr("确定"),  QMessageBox.YesRole)
            self.msgBox.setWindowIcon(QtGui.QIcon('asktao.ico'))
            self.msgBox.exec_()
            self.close()
        else:
            self.promptsFormFalse()


    
    def promptsFormFalse(self):
        self.msgBox = QMessageBox(QMessageBox.Warning,  "问道端口扫描",  "修改失败，信息配置有误请重新输入！")
        self.reply = self.msgBox.addButton(self.tr("确定"),  QMessageBox.YesRole)
        self.msgBox.setWindowIcon(QtGui.QIcon('asktao.ico'))
        self.msgBox.exec_()
        
        
class visitUrl(QThread):
    trigger = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(visitUrl, self).__init__(parent)
    
    def run(self):
        res = requests.get(host, timeout=(3, 7))
        if "二〇一六" in res.text:
            self.trigger.emit('ok')
        else:
            self.trigger.emit('error')
        
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

