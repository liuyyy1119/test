from PySide6.QtWidgets import QApplication, QWidget, QLineEdit,QBoxLayout
from PySide6.QtCore import Qt


class MyWindow (QWidget,Ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication[()]
    window = MyWindow()
    window.show()
    app.exec()