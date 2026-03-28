import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PySide6.QtCore import Slot

from sign_ui import Ui_loginButton   # 引入UI
import sqlite3
from db import init_db  #引入数据库
from PySide6.QtCore import QSettings


from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Circle


from main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QInputDialog, QMessageBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Circle


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Circle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("主界面")

        # 数据存储
        self.center = None
        self.radius = None

        # 创建中央组件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # 创建按钮
        self.btn_center = QPushButton("输入圆心")
        self.btn_radius = QPushButton("输入半径")
        self.btn_draw = QPushButton("绘制圆")

        # 绑定按钮点击事件
        self.btn_center.clicked.connect(self.set_center)
        self.btn_radius.clicked.connect(self.set_radius)
        self.btn_draw.clicked.connect(self.draw_circle)

        # matplotlib 画布
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # 布局设置
        layout.addWidget(self.btn_center)
        layout.addWidget(self.btn_radius)
        layout.addWidget(self.btn_draw)
        layout.addWidget(self.canvas)

        central_widget.setLayout(layout)

    # 输入圆心
    def set_center(self):
        x, ok1 = QInputDialog.getDouble(self, "输入圆心", "x坐标")
        y, ok2 = QInputDialog.getDouble(self, "输入圆心", "y坐标")

        if ok1 and ok2:
            self.center = (x, y)

    # 输入半径
    def set_radius(self):
        r, ok = QInputDialog.getDouble(self, "输入半径", "半径")
        if ok and r > 0:
            self.radius = r

    # 绘制圆
    def draw_circle(self):
        if self.center is None or self.radius is None:
            QMessageBox.warning(self, "错误", "请先输入圆心和半径")
            return

        x, y = self.center
        r = self.radius

        # 清空画布，保证只显示一个圆
        self.ax.clear()

        # 绘制圆形
        circle = Circle((x, y), r, fill=False)
        self.ax.add_patch(circle)

        # 设置坐标轴
        self.ax.set_aspect('equal')
        self.ax.set_xlim(x - r - 1, x + r + 1)
        self.ax.set_ylim(y - r - 1, y + r + 1)
        self.ax.grid(True)

        # 刷新画布
        self.canvas.draw()



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