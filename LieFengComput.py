#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 12:43
# @Author  : 米兰的小铁匠
# @File    : LieFengComput.py
# @Software: PyCharm

import sys
import imageSource_rc
from LieFengComputUI import Ui_LieFeng
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication,QTableView,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
from PyQt5.Qt import Qt, QRect, QCompleter, QSortFilterProxyModel
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QComboBox, QCompleter
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QInputDialog

# 这里需要用继承的方法. 因为生成的文件可能会因为界面而改变, 直接继承就不用担心代码被覆盖.
class LieFeng_comput(QtWidgets.QMainWindow, Ui_LieFeng):
    def __init__(self, parent=None):
        super(LieFeng_comput, self).__init__(parent=parent)
        self.setupUi(self)
        #设置MainWindow窗口默认大小且不可该表
        # self.setFixedSize(869, 556)

        #设置主窗口的标题
        self.setWindowTitle('裂缝计算')

        #数据库连接与创建
        self.open_sqlite()

        self.table_selector.setEditable(True)
        self.db = None  # 声明一个成员变量 db，用于存储数据库连接对象
        self.setup_table_selector()

        self.Push_button()

    def open_sqlite(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./db/database.db')
        if not self.db.open():
            alert = QMessageBox()
            alert.setText(self.db.lastError().text())
            alert.exec_()

    def add_table(self):
        # 获取用户输入的新表名
        new_table_name, ok = QInputDialog.getText(self, "新建", "输入井眼编号:")
        if ok:
            # 执行 SQL 命令创建新表
            query = QSqlQuery()  # 创建 QSqlQuery 对象，用于执行数据库查询操作
            create_table_sql = f"CREATE TABLE {new_table_name} (裂缝编号 INT, 漏失流量 INT, 漏失半径 INT, 裂缝宽度 INT, 漏层深度 INT, 漏失时间 INT)"
            query.exec_(create_table_sql)  # 执行 SQL 命令创建新表
            # 更新表名下拉菜单
            self.setup_table_selector()  # 调用自定义的方法，更新表名下拉菜单

    def delete_selected_table(self):
        # 从 QComboBox 中获取选中的表名
        selected_table_name = self.table_selector.currentText()

        # 获取数据库中的所有表名
        tables = QSqlDatabase.database().tables()
        # 执行 SQL 命令删除选中的表
        query = QSqlQuery()
        delete_table_sql = f"DROP TABLE IF EXISTS {selected_table_name}"

        if selected_table_name in tables:
            # 表存在，执行删除操作
            if query.exec_(delete_table_sql):
                QMessageBox.information(self, "提示", "表删除成功")
                self.table_selector.clear()
                self.setup_table_selector()
            else:
                QMessageBox.warning(self, "提示", f"表删除失败：{query.lastError().text()}")
        else:
            # 表不存在，弹出提示框
            QMessageBox.warning(self, "提示", "该表不存在")


    def setup_table_selector(self):
        """
        设置 table_selector 下拉菜单的显示和搜索自动补全功能
        """
        str_arr = []
        self.cvquery = QSqlQuery()
        sql = u"SELECT name from sqlite_master where type = 'table' order by name"
        if self.cvquery.exec_(sql):
            while self.cvquery.next():
                str_v = self.cvquery.value(0)
                str_arr.append(str_v)

        self.table_selector.clear()

        self.table_selector.addItems(str_arr)

        # 设置下拉菜单的搜索自动补全功能
        completer = QCompleter(str_arr)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.table_selector.setCompleter(completer)

    @pyqtSlot(str)
    def on_table_selector_currentIndexChanged(self, tbl_name):
        if tbl_name:
            model = QSqlTableModel()
            model.setTable('"' + tbl_name + '"')
            model.setEditStrategy(QSqlTableModel.OnManualSubmit)
            model.select()
            self.datadisplay.setModel(model)
            self.datadisplay.model().dataChanged.connect(self.changed)


    #实现数据库数据显示
    @QtCore.pyqtSlot(str)
    # 这是一个槽函数（Slot），用于接收从下拉菜单传递过来的字符串参数 tbl_name。
    def on_table_selector_currentIndexChanged(self, tbl_name):

        # 如果 tbl_name 不为空（即有选中的表名），则执行下面的代码，否则跳过。
        if tbl_name:

            # 创建一个 QSqlTableModel 对象 model，并将要操作的表名设置为 tbl_name。
            # 由于表名可能包含空格或特殊字符，所以在表名两端添加双引号进行包括，保证查询的正确性。
            model = QSqlTableModel()
            model.setTable('"' + tbl_name + '"')

            # 设置数据表的编辑策略为 OnManualSubmit，即仅在手动提交时更新数据库；
            # 如果需要实时更新数据库，可以使用 OnFieldChange。
            # 然后使用 select() 方法启动查询操作，并将查询结果储存在 model 中。
            model.setEditStrategy(QSqlTableModel.OnManualSubmit)
            # model.setEditStrategy(QSqlTableModel.OnFieldChange)
            model.select()

            # 这是一个可能存在但被注释掉的错误检查方法，如果需要对数据模型进行错误检查，可以将该方法取消注释。
            # 该方法用于检查并分析 model 中的错误，如果发现错误，会打印错误信息以便进行修复。
            # self.error_check(model)s

            # 将 model 设置为 self.datadisplay 的数据模型，self.datadisplay 是一个 QTableView 视图。
            self.datadisplay.setModel(model)

            # 连接 dataChanged 信号，当数据模型中的数据发生变化时，会触发 self.changed 方法来处理这些变化。
            self.datadisplay.model().dataChanged.connect(self.changed)

    def changed(self, i, j):
        # item = self.tableView.model().index(i.row(),i.column())
        # model->item(i,0)->setForeground(QBrush(QColor(255, 0, 0)));
        # self.tableView.model().record(num).value(1).toString()
        pass

    def close_db(self):
        if self.db:
            try:
                if self.db.isOpen():
                    self.db.close()
            except Exception as e:
                print(f"Error closing database connection: {e}")
            finally:
                self.db = None

    def Push_button(self):
        # clear按钮点击事件连接
        self.clear_1.clicked.connect(self.result_clear)

        # 实现pushbuttn计算数据按钮
        self.jisuan.clicked.connect(self.date_comput)

        self.add_table_button.clicked.connect(self.add_table)

        self.delete_table_button.clicked.connect(self.delete_selected_table)

    #数据计算
    def date_comput(self):
        # 数据读取
        time1 = self.time1.time()  # 开始漏失时间数据读取
        time1hour = time1.hour()
        time1minute = time1.minute()

        time2 = self.time2.time()  # 结束漏失时间数据读取
        time2hour = time2.hour()
        time2minute = time2.minute()

        # 漏失时间lstime计算，单位（分钟）
        if time2minute - time1minute <= 0:
            lstime = (time2hour - time1hour) * 60 - time1minute + time2minute
        elif time2minute - time1minute >= 0:
            lstime = (time2hour - time1hour) * 60 + time2minute - time1minute

        deep1 = self.deep1.value()  # 钻井深度数据读取
        deep2 = self.deep2.value()  # 钻井深度数据读取
        lsl1 = self.lsl1.value()  # 钻井液漏失量数据读取
        lsl2 = self.lsl2.value()  # 钻井液漏失量数据读取
        midu = self.midu.value()  # 钻井液密度数据读取
        midu = midu * 1000  # 钻井液密度单位转换（克每立方厘米->千克每立方米）
        niandu = self.niandu.value()  # 钻井粘度数据读取
        jybanjing = self.jybj.value()  # 井眼半径数据读取
        pai = self.pai.value()  # 圆周率数据读取

        # 模型计算
        lsll = lsl2 / lstime * 60  # 漏失流量数据计算

        vpc = (deep2 - deep1) / lstime * 60  # 漏层深度计算
        lstime1 = lsl1 / lsll
        lcdeep = deep1 - (lstime1 * vpc)

        # lfkd = ((lsll * 6 * niandu)/(pai * jybanjing * midu * 9.8 * lcdeep)) ** 1/3     #裂缝宽度计算
        lfkd1 = lsll * 6 * niandu
        lfkd2 = pai * jybanjing * midu * 9.8 * lcdeep
        lfkd3 = lfkd1 / lfkd2
        self.lfkddate = pow(lfkd3, 1 / 3)

        # lsbj = ((jybanjing * jybanjing) + (lsll / (2 * pai * lfkd))) ** 2             #漏失半径计算
        lsbj1 = pow(jybanjing, 2)
        lsbj2 = 2 * pai * self.lfkddate
        lsbj3 = lsll / lsbj2
        lsbj4 = lsbj3 + lsbj1
        lsbj = pow(lsbj4, 0.5)

        #数据转换成字符串输出
        lslldp = format(self.lsll, '.4f')
        lcdeepdp = format(self.lcdeep, '.4f')
        lfkddp = format(self.lfkddate, '.4f')
        lsbjdp = format(self.lsbj, '.4f')
        lsbj = format(lsbj, '.4f')

        #数据显示
        self.lsll.setText(lslldp)
        self.lcdeep.setText(lcdeepdp)
        self.lfkd.setText(lfkddp)
        self.lsbj.setText(lsbjdp)

    #计算结果清空
    def result_clear(self):
        self.lsll.clear()
        self.lcdeep.clear()
        self.lfkd.clear()
        self.lsbj.clear()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/chouyouji.ico'))
    w = LieFeng_comput()
    w.show()
    sys.exit(app.exec_())