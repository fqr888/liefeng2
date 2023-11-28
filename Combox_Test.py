from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QCompleter, QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from ui_liefeng import Ui_LieFeng


class LieFeng_comput(QMainWindow, Ui_LieFeng):
    def __init__(self, parent=None):
        super(LieFeng_comput, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = None  # 声明一个成员变量 db，用于存储数据库连接对象
        self.open_sqlite()
        self.setup_table_selector()

    def open_sqlite(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./db/database.db')
        if not self.db.open():
            alert = QMessageBox()
            alert.setText(self.db.lastError().text())
            alert.exec_()

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

            # 设置表格内容自适应列宽
            horizontal_header = self.datadisplay.horizontalHeader()
            horizontal_header.setSectionResizeMode(QHeaderView.Stretch)

    def changed(self, i, j):
        pass