#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/22 14:39
# @Author  : 米兰的小铁匠
# @File    : DataGrid_Display.py
# @Software: PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def initializeModel(model):
    model.setTable('people')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal,'ID')
    model.setHeaderData(1, Qt.Horizontal,'姓名')
    model.setHeaderData(2, Qt.Horizontal,'地址')

def createView(titel,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(titel)
    return view


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/datebase.db')
    model = QSqlTableModel()
    delrow = -1
    initializeModel(model)
    view = createView("展示数据",model)


    sys.exit(app.exec())