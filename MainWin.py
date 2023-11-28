#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/17 12:26
# @Author  : 米兰的小铁匠
# @File    : MainWin.py
# @Software: PyCharm

import sys
import imageSource_rc
from MainWinUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon

# 这里需要用继承的方法. 因为生成的文件可能会因为界面而改变, 直接继承就不用担心代码被覆盖.
class Main_QtWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_QtWin, self).__init__(parent=parent)
        self.setupUi(self)


        #设置MainWindow窗口默认大小且不可该表
        self.setFixedSize(960, 633)

        # 这个是继承.ui文件的类里面来的.

        # self.retranslateUi(self)

        # 这个是继承.ui文件的类里面来的.

        # 设置图片的相对路径
       # self.MainWindow.setStyleSheet("#centralwidget{border-image:url(./image/DQoil.png);}")


        # 设置主窗口的标题
        self.setWindowTitle('裂缝漏失与防漏计算软件')

        # 窗口居中显示函数


    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/chouyouji.ico'))
    w = Main_QtWin()
    w.show()
    sys.exit(app.exec_())