import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PySide6.QtCore import Slot

from sign_ui import Ui_loginButton   # 引入UI
import sqlite3
from db import init_db  #引入数据库
from PySide6.QtCore import QSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        # self.resize(800, 600) 


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_loginButton()
        self.ui.setupUi(self)
        self.ui.registerButton.clicked.connect(self.register)
        # 绑定事件
        self.ui.pushButton.clicked.connect(self.login)
        self.settings = QSettings("MyApp", "Login")

    @Slot()
    def login(self):
        # 👇 所有数据库逻辑必须放在 login 方法内部（缩进正确）
        username = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        result = cursor.fetchone()
        conn.close()

        if result:
            self.main = MainWindow()
            self.main.showMaximized()
            self.close()
        else:
            QMessageBox.warning(self, "错误", "账号或密码错误")

    # ✅ 修复：register 方法所有代码全部缩进内部
    @Slot()
    def register(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        if not username or not password:
            QMessageBox.warning(self, "错误", "请输入账号和密码")
            return

        # 👇 下面所有数据库代码都要缩进在 register 方法里！
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            QMessageBox.information(self, "成功", "注册成功！")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "错误", "用户名已存在！")
        finally:
            conn.close()          


if __name__ == "__main__":
    init_db()   #初始化数据库
    
    app = QApplication(sys.argv)

    win = LoginWindow()
    win.show()

    sys.exit(app.exec())