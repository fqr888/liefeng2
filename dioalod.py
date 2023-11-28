import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据库表添加示例")
        self.button = QPushButton("Add", self)
        self.button.clicked.connect(self.add_dialog)
        self.setCentralWidget(self.button)

    def add_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("添加新表")
        layout = QVBoxLayout(dialog)

        label = QLabel("表名:", dialog)
        layout.addWidget(label)
        table_name_input = QLineEdit(dialog)
        layout.addWidget(table_name_input)

        confirm_button = QPushButton("确认", dialog)
        confirm_button.clicked.connect(lambda: self.create_table(table_name_input.text(), dialog))
        layout.addWidget(confirm_button)

        dialog.exec_()

    def create_table(self, table_name, dialog):
        # 连接数据库
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # 执行创建表的SQL语句
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT PRIMARY KEY, name TEXT);"
        cursor.execute(create_table_sql)
        conn.commit()

        cursor.close()
        conn.close()

        # 关闭对话框
        dialog.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())