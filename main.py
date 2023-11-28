import sys
from UItest import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


# 这里需要用继承的方法. 因为生成的文件可能会因为界面而改变, 直接继承就不用担心代码被覆盖.
class MyPyQT_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyPyQT_Form, self).__init__(parent=parent)
        self.setupUi(self)        # 这个是继承.ui文件的类里面来的.
        # self.retranslateUi(self)  # 这个是继承.ui文件的类里面来的.

        # 设置主窗口的标题
        self.setWindowTitle('裂缝漏失与防漏计算软件')


        # self.display()  # 添加此行代码以调用 display(self) 函数

    #实现pushbuttn计算数据按钮
    def pushButton_jisuan_click(self):
        # self.textEdit_display.setText("你点击了按钮")
        # 按键点击事件连接
        self.jisuan.clicked.connect(self.date_comput)

        # self.jisuan.clicked.connect(self.display)

        self.jisuan.clicked.connect(self.update_cylinders)

    #实现计算结果窗口数据清除
    def pushButton_clear_click(self):
        # self.textEdit_display.clear()
        # clear按钮点击事件连接
        self.clear.clicked.connect(self.result_clear)

    # 数据计算
    def date_comput(self):
        # 数据读取
        time1 = self.time1.time()  #开始漏失时间数据读取
        time1hour = time1.hour()
        time1minute = time1.minute()

        time2 = self.time2.time()  #结束漏失时间数据读取
        time2hour = time2.hour()
        time2minute = time2.minute()

        # 漏失时间lstime计算，单位（分钟）
        if time2minute - time1minute <= 0:
            lstime = (time2hour - time1hour) * 60 - time1minute + time2minute
        elif time2minute - time1minute >= 0:
            lstime = (time2hour - time1hour) * 60 + time2minute - time1minute

        deep1 = self.deep1.value()     # 钻井深度数据读取
        deep2 = self.deep2.value()     # 钻井深度数据读取
        lsl1 = self.lsl1.value()       # 钻井液漏失量数据读取
        lsl2 = self.lsl2.value()       # 钻井液漏失量数据读取
        midu = self.midu.value()       # 钻井液密度数据读取
        midu = midu * 1000             # 钻井液密度单位转换（克每立方厘米->千克每立方米）
        niandu = self.niandu.value()   # 钻井粘度数据读取
        jybanjing = self.jybj.value()  # 井眼半径数据读取
        pai = self.pai.value()         # 圆周率数据读取

        # 模型计算
        lsll = lsl2 / lstime * 60                   #漏失流量数据计算

        vpc = (deep2 - deep1) / lstime * 60         #漏层深度计算
        lstime1 = lsl1 / lsll
        lcdeep = deep1 - (lstime1*vpc)

        # lfkd = ((lsll * 6 * niandu)/(pai * jybanjing * midu * 9.8 * lcdeep)) ** 1/3     #裂缝宽度计算
        lfkd1 = lsll * 6 * niandu
        lfkd2 = pai * jybanjing * midu * 9.8 * lcdeep
        lfkd3 = lfkd1 / lfkd2
        self.lfkddate = pow(lfkd3,1/3)

        # lsbj = ((jybanjing * jybanjing) + (lsll / (2 * pai * lfkd))) ** 2             #漏失半径计算
        lsbj1 = pow(jybanjing,2)
        lsbj2 = 2 * pai * self.lfkddate
        lsbj3 = lsll / lsbj2
        lsbj4 = lsbj3 + lsbj1
        lsbj = pow(lsbj4,0.5)


        # 数据转换成字符串输出
        lslldp = format(lsll, '.4f')
        lcdeepdp = format(lcdeep, '.4f')
        lfkddp = format(self.lfkddate, '.4f')
        lsbjdp = format(lsbj, '.4f')
        # lsbj = format(lsbj, '.4f')

        # 数据显示
        self.lsll.setPlainText(lslldp)
        self.lcdeep.setPlainText(lcdeepdp)
        self.lfkd.setPlainText(lfkddp)
        self.lsbj.setPlainText(lsbjdp)



    #计算结果清空
    def result_clear(self):
        self.lsll.clear()
        self.lcdeep.clear()
        self.lfkd.clear()
        self.lsbj.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/chouyouji.ico'))
    w = MyPyQT_Form()
    w.show()
    sys.exit(app.exec_())
