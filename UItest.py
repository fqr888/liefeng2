# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UItest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 703)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 31, 308, 333))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.niandu = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.niandu.setFont(font)
        self.niandu.setSuffix("")
        self.niandu.setDecimals(4)
        self.niandu.setMaximum(999999999.0)
        self.niandu.setSingleStep(0.01)
        self.niandu.setObjectName("niandu")
        self.gridLayout.addWidget(self.niandu, 8, 1, 1, 1)
        self.deep1 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.deep1.setFont(font)
        self.deep1.setSuffix("")
        self.deep1.setDecimals(4)
        self.deep1.setMaximum(999999999.0)
        self.deep1.setSingleStep(0.01)
        self.deep1.setObjectName("deep1")
        self.gridLayout.addWidget(self.deep1, 3, 1, 1, 1)
        self.pai = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pai.setFont(font)
        self.pai.setSuffix("")
        self.pai.setDecimals(4)
        self.pai.setMaximum(999999999.0)
        self.pai.setSingleStep(0.01)
        self.pai.setProperty("value", 3.14)
        self.pai.setObjectName("pai")
        self.gridLayout.addWidget(self.pai, 10, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.lsl1 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lsl1.setFont(font)
        self.lsl1.setSuffix("")
        self.lsl1.setDecimals(4)
        self.lsl1.setMaximum(999999999.0)
        self.lsl1.setSingleStep(0.01)
        self.lsl1.setObjectName("lsl1")
        self.gridLayout.addWidget(self.lsl1, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 2, 1, 1)
        self.jybj = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.jybj.setFont(font)
        self.jybj.setSuffix("")
        self.jybj.setDecimals(4)
        self.jybj.setMaximum(999999999.0)
        self.jybj.setSingleStep(0.01)
        self.jybj.setObjectName("jybj")
        self.gridLayout.addWidget(self.jybj, 9, 1, 1, 1)
        self.deep2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.deep2.setFont(font)
        self.deep2.setSuffix("")
        self.deep2.setDecimals(4)
        self.deep2.setMaximum(999999999.0)
        self.deep2.setSingleStep(0.01)
        self.deep2.setObjectName("deep2")
        self.gridLayout.addWidget(self.deep2, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.time1 = QtWidgets.QTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.time1.setFont(font)
        self.time1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time1.setObjectName("time1")
        self.gridLayout.addWidget(self.time1, 1, 1, 1, 1)
        self.time2 = QtWidgets.QTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.time2.setFont(font)
        self.time2.setObjectName("time2")
        self.gridLayout.addWidget(self.time2, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.jisuan = QtWidgets.QPushButton(self.layoutWidget)
        self.jisuan.setObjectName("jisuan")
        self.gridLayout.addWidget(self.jisuan, 11, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 8, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 9, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.midu = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.midu.setFont(font)
        self.midu.setSuffix("")
        self.midu.setDecimals(4)
        self.midu.setMaximum(999999999.0)
        self.midu.setSingleStep(0.01)
        self.midu.setObjectName("midu")
        self.gridLayout.addWidget(self.midu, 7, 1, 1, 1)
        self.lsl2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lsl2.setFont(font)
        self.lsl2.setSuffix("")
        self.lsl2.setDecimals(4)
        self.lsl2.setMaximum(999999999.0)
        self.lsl2.setSingleStep(0.01)
        self.lsl2.setObjectName("lsl2")
        self.gridLayout.addWidget(self.lsl2, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(430, 30, 281, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.lsll = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.lsll.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lsll.sizePolicy().hasHeightForWidth())
        self.lsll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lsll.setFont(font)
        self.lsll.setObjectName("lsll")
        self.gridLayout_2.addWidget(self.lsll, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.lcdeep = QtWidgets.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdeep.sizePolicy().hasHeightForWidth())
        self.lcdeep.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lcdeep.setFont(font)
        self.lcdeep.setObjectName("lcdeep")
        self.gridLayout_2.addWidget(self.lcdeep, 2, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 2, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.lfkd = QtWidgets.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfkd.sizePolicy().hasHeightForWidth())
        self.lfkd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lfkd.setFont(font)
        self.lfkd.setObjectName("lfkd")
        self.gridLayout_2.addWidget(self.lfkd, 3, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 3, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.lsbj = QtWidgets.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lsbj.sizePolicy().hasHeightForWidth())
        self.lsbj.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lsbj.setFont(font)
        self.lsbj.setObjectName("lsbj")
        self.gridLayout_2.addWidget(self.lsbj, 4, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 4, 2, 1, 1)
        self.clear = QtWidgets.QPushButton(self.layoutWidget1)
        self.clear.setObjectName("clear")
        self.gridLayout_2.addWidget(self.clear, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 805, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionylcs = QtWidgets.QAction(MainWindow)
        self.actionylcs.setObjectName("actionylcs")
        self.menu_2.addAction(self.actionylcs)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.actionylcs)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.time1, self.time2)
        MainWindow.setTabOrder(self.time2, self.deep1)
        MainWindow.setTabOrder(self.deep1, self.deep2)
        MainWindow.setTabOrder(self.deep2, self.lsl1)
        MainWindow.setTabOrder(self.lsl1, self.lsl2)
        MainWindow.setTabOrder(self.lsl2, self.midu)
        MainWindow.setTabOrder(self.midu, self.niandu)
        MainWindow.setTabOrder(self.niandu, self.jybj)
        MainWindow.setTabOrder(self.jybj, self.pai)
        MainWindow.setTabOrder(self.pai, self.jisuan)
        MainWindow.setTabOrder(self.jisuan, self.lsll)
        MainWindow.setTabOrder(self.lsll, self.lcdeep)
        MainWindow.setTabOrder(self.lcdeep, self.lfkd)
        MainWindow.setTabOrder(self.lfkd, self.lsbj)
        MainWindow.setTabOrder(self.lsbj, self.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">钻进深度D1=</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失量V1=</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">钻进深度D2=</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span><span style=\" font-size:14pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">数据输入</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">g/cm</span><span style=\" font-size:14pt; vertical-align:super;\">3</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">钻井液密度=</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失时间T2=</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">钻井液粘度=</span></p></body></html>"))
        self.time1.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.time2.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失量V2=</span></p></body></html>"))
        self.jisuan.setText(_translate("MainWindow", "计算"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">s</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">井眼半径Ro=</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失时间T1=</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">圆周率Π=</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span><span style=\" font-size:14pt; vertical-align:super;\">3</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "关闭窗口"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">计算结果</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失流量=</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span><span style=\" font-size:14pt; vertical-align:super;\">3</span><span style=\" font-size:14pt;\">/h</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏层深度=</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">   m   </span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">裂缝宽度=</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">漏失半径=</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">m</span></p></body></html>"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionylcs.setText(_translate("MainWindow", "压力测试"))
