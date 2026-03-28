# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 589)
        self.verticalLayout_3 = QVBoxLayout(MainWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.canvas_widget = QWidget(MainWindow)
        self.canvas_widget.setObjectName(u"canvas_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.canvas_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.canvas_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_center = QPushButton(MainWindow)
        self.btn_center.setObjectName(u"btn_center")

        self.horizontalLayout.addWidget(self.btn_center)

        self.btn_radius = QPushButton(MainWindow)
        self.btn_radius.setObjectName(u"btn_radius")

        self.horizontalLayout.addWidget(self.btn_radius)

        self.btn_draw = QPushButton(MainWindow)
        self.btn_draw.setObjectName(u"btn_draw")

        self.horizontalLayout.addWidget(self.btn_draw)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_center.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5706\u5fc3", None))
        self.btn_radius.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u534a\u5f84", None))
        self.btn_draw.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u5706", None))
    # retranslateUi

