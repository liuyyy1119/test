# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_loginButton(object):
    def setupUi(self, loginButton):
        if not loginButton.objectName():
            loginButton.setObjectName(u"loginButton")
        loginButton.resize(284, 240)
        loginButton.setWindowOpacity(0.900000000000000)
        self.verticalLayout_3 = QVBoxLayout(loginButton)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(loginButton)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.usernameEdit = QLineEdit(loginButton)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.horizontalLayout.addWidget(self.usernameEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(loginButton)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.passwordEdit = QLineEdit(loginButton)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.passwordEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox = QCheckBox(loginButton)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.registerButton = QPushButton(loginButton)
        self.registerButton.setObjectName(u"registerButton")

        self.horizontalLayout_3.addWidget(self.registerButton)

        self.pushButton = QPushButton(loginButton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(loginButton)

        QMetaObject.connectSlotsByName(loginButton)
    # setupUi

    def retranslateUi(self, loginButton):
        loginButton.setWindowTitle(QCoreApplication.translate("loginButton", u"\u767b\u9646\u9875\u9762", None))
        self.label_2.setText(QCoreApplication.translate("loginButton", u"\u7528\u6237\u540d", None))
        self.usernameEdit.setPlaceholderText(QCoreApplication.translate("loginButton", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("loginButton", u"\u5bc6\u7801   ", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("loginButton", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("loginButton", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.registerButton.setText(QCoreApplication.translate("loginButton", u"\u6ce8\u518c", None))
        self.pushButton.setText(QCoreApplication.translate("loginButton", u"\u767b\u5f55", None))
    # retranslateUi

