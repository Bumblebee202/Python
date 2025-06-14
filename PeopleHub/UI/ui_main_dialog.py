# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.tableWidget_contacts = QTableView(self.centralwidget)
        self.tableWidget_contacts.setObjectName(u"tableWidget_contacts")

        self.verticalLayout.addWidget(self.tableWidget_contacts)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.horizontalLayout_buttons.addWidget(self.pushButton_add)

        self.pushButton_edit = QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.horizontalLayout_buttons.addWidget(self.pushButton_edit)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_buttons.addWidget(self.pushButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PeopleHub", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<h2>\u0421\u043f\u0438\u0441\u043e\u043a \u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0456\u0432</h2>", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442", None))
    # retranslateUi

