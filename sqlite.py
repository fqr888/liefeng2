# coding=utf-8
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5 import uic
from PyQt5 import QtCore

TYPE_DICT = {1: "BOOLEAN", 2: "INTEGER", 6: "NUMERIC", 10: "TEXT", 12: "BLOB", 13: "DATE"}


class WindowClass(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.resize(800, 480)

        self.setWindowTitle("SQLite GUI")
        self.initUI()
        self.tree_model = QStandardItemModel()
        self.treeView.setModel(self.tree_model)


    def initUI(self):
        uic.loadUi('sqlite.ui', self)


    def load_sqlite(self):
        path, _ = QFileDialog.getOpenFileName(self, u"打开sqlite文件", os.getcwd(), "sqlite db(*.db)")
        if path:
            self.data_file = path
            self.connect_db()


    def load_table(self):
        str_arr = []
        if not self.db.open():
            return

        self.cvquery = QSqlQuery()
        sql = u"SELECT name from sqlite_master where type = 'table' order by name"
        if self.cvquery.exec_(sql):
            while self.cvquery.next():
                str_v = self.cvquery.value(0)
                str_arr.append(str_v)
        return str_arr


    def connect_db(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        filename = os.path.join(os.path.dirname(__file__), self.data_file)
        self.db.setDatabaseName(filename)

        if not self.db.open():
            alert = QMessageBox()
            alert.setText(self.db.lastError().text())
            alert.exec_()

        # self.load_table_group()
        tb_names = self.load_table()

        self.table_selector.clear()
        for name in tb_names:
            self.table_selector.addItem(name)

        self.update_tables_table()


    def update_tables_table(self):
        self.tree_model.clear()
        self.tree_model.setHorizontalHeaderLabels(['Name', 'Type', 'Schema'])

        if not self.db.open():
            return

        self.cvquery = QSqlQuery()
        sql = u"SELECT name from sqlite_master where type = 'table' order by name"
        if self.cvquery.exec_(sql):
            while self.cvquery.next():
                str_v = self.cvquery.value(0)
                tab = QStandardItem('%ss (%d)' % (str_v, 0))
                self.tree_model.appendRow(tab)

                driver = self.db.driver()
                rec = driver.record(str_v)
                for i in range(rec.count()):
                    col_name = QStandardItem(rec.field(i).name())
                    type_id = rec.field(i).type()
                    if type_id in TYPE_DICT:
                        type_str = TYPE_DICT[type_id]
                    else:
                        type_str = str(type_id)
                    col_type = QStandardItem(type_str)

                    tab.appendRow([col_name, col_type])


    def close_db(self):
        if self.db:
            if self.db.isOpen():
                pass


    def on_tableView_currentItemChanged(self, pre, current):
        print("edit")
        # twitem.setBackgroundColor(QColor(0,60,10))


    # ui binding
    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        save_file_dialog = QFileDialog.getSaveFileName(self, "Name of new database")
        if save_file_dialog[0]:
            self.loadDatabase(save_file_dialog[0])


    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.load_sqlite()


    @QtCore.pyqtSlot(str)
    def on_table_selector_currentIndexChanged(self, tbl_name):
        if tbl_name:
            model = QSqlTableModel()
            model.setTable('"' + tbl_name + '"')
            model.setEditStrategy(QSqlTableModel.OnManualSubmit)
            # model.setEditStrategy(QSqlTableModel.OnFieldChange)
            model.select()

            # self.error_check(model)s
            self.tableView.setModel(model)

            self.tableView.model().dataChanged.connect(self.changed)


    def changed(self, i, j):
        # item = self.tableView.model().index(i.row(),i.column())
        # model->item(i,0)->setForeground(QBrush(QColor(255, 0, 0)));
        # self.tableView.model().record(num).value(1).toString()
        pass


    @QtCore.pyqtSlot()
    def on_deleteRecordButton_pressed(self):
        model = self.tableView.model()
        model.removeRow(self.tableView.currentIndex().row())
        model.submitAll()
        model.select()
        # QMessageBox.warning(self, "Delete",
        #                 "The database reported an error: %s" % model.lastError().text())


    @QtCore.pyqtSlot()
    def on_newRecordButton_pressed(self):
        model = self.tableView.model()
        model.submitAll()
        result = model.insertRows(model.rowCount(), 1)

        if not result:
            self.error_check(model)


    @QtCore.pyqtSlot()
    def on_submitChange_pressed(self):
        model = self.tableView.model()
        model.database().transaction()
        if model.submitAll():
            model.database().commit()
        else:
            model.database().rollback()
            QMessageBox.warning(self, "Cached Table",
                                "The database reported an error: %s" % self.model.lastError().text())


    @QtCore.pyqtSlot()
    def on_rollback_pressed(self):
        model = self.tableView.model()
        model.database().transaction()
        model.revertAll();


if __name__ == '__main__':
    app = QApplication([])
    mw = WindowClass()
    mw.show()
    app.exec_()