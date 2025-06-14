# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateContactDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_CreateContactDialog(object):
    def setupUi(self, CreateContactDialog):
        if not CreateContactDialog.objectName():
            CreateContactDialog.setObjectName(u"CreateContactDialog")
        CreateContactDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(CreateContactDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(CreateContactDialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_name = QLabel(CreateContactDialog)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(CreateContactDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_name)

        self.label_phone = QLabel(CreateContactDialog)
        self.label_phone.setObjectName(u"label_phone")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_phone)

        self.lineEdit_phone = QLineEdit(CreateContactDialog)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_phone)

        self.label_email = QLabel(CreateContactDialog)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(CreateContactDialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_email)

        self.label_address = QLabel(CreateContactDialog)
        self.label_address.setObjectName(u"label_address")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_address)

        self.lineEdit_address = QLineEdit(CreateContactDialog)
        self.lineEdit_address.setObjectName(u"lineEdit_address")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_address)

        self.label_notes = QLabel(CreateContactDialog)
        self.label_notes.setObjectName(u"label_notes")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_notes)

        self.textEdit_notes = QTextEdit(CreateContactDialog)
        self.textEdit_notes.setObjectName(u"textEdit_notes")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.textEdit_notes)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(CreateContactDialog)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_buttons.addWidget(self.pushButton_save)

        self.pushButton_cancel = QPushButton(CreateContactDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_buttons.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)


        self.retranslateUi(CreateContactDialog)

        QMetaObject.connectSlotsByName(CreateContactDialog)
    # setupUi

    def retranslateUi(self, CreateContactDialog):
        CreateContactDialog.setWindowTitle(QCoreApplication.translate("CreateContactDialog", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.label_title.setText(QCoreApplication.translate("CreateContactDialog", u"<h3>\u041d\u043e\u0432\u0438\u0439 \u041a\u043e\u043d\u0442\u0430\u043a\u0442</h3>", None))
        self.label_name.setText(QCoreApplication.translate("CreateContactDialog", u"\u0406\u043c'\u044f:", None))
        self.label_phone.setText(QCoreApplication.translate("CreateContactDialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.label_email.setText(QCoreApplication.translate("CreateContactDialog", u"Email:", None))
        self.label_address.setText(QCoreApplication.translate("CreateContactDialog", u"\u0410\u0434\u0440\u0435\u0441\u0430:", None))
        self.label_notes.setText(QCoreApplication.translate("CreateContactDialog", u"\u041f\u0440\u0438\u043c\u0456\u0442\u043a\u0430:", None))
        self.pushButton_save.setText(QCoreApplication.translate("CreateContactDialog", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("CreateContactDialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi

