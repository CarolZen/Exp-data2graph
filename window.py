# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit

import sys
app=QApplication([])
window=QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('Simple')

textEdit=QPlainTextEdit(window)
textEdit.setPlainText('X轴')
textEdit.move(10, 25)
textEdit.resize(50,20)

button=QPushButton('生成',window)
button.move(380, 80)

window.show()

exit(app.exec_())

'''
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QPlainTextEdit,QMessageBox,QFileDialog,QTextEdit
import sys

    
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.tx=QTextEdit(self)
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('关注微信公众号：学点编程吧--保存、打印文件')
        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)
        self.bt1=QPushButton('open', self)
        self.bt1.clicked.connect(self.openfile)
        self.show()
    def openfile(self):
        fname=QFileDialog.getOpenFileName(self,'choose')
        if fname[0]: 
               # with open(fname, 'r',encoding='gb18030',errors='ignore') as f:
            self.tx.append(fname[0])
    
    #系统exit()方法确保应用程序干净的退出
    #的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    

if __name__ == '__main__':
    #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    #QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    ex=Example()
    sys.exit(app.exec_())