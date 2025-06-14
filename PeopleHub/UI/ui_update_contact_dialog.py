# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateContactDialog.ui'
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

class Ui_UpdateContactDialog(object):
    def setupUi(self, UpdateContactDialog):
        if not UpdateContactDialog.objectName():
            UpdateContactDialog.setObjectName(u"UpdateContactDialog")
        UpdateContactDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(UpdateContactDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(UpdateContactDialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_name = QLabel(UpdateContactDialog)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(UpdateContactDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_name)

        self.label_phone = QLabel(UpdateContactDialog)
        self.label_phone.setObjectName(u"label_phone")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_phone)

        self.lineEdit_phone = QLineEdit(UpdateContactDialog)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_phone)

        self.label_email = QLabel(UpdateContactDialog)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(UpdateContactDialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_email)

        self.label_address = QLabel(UpdateContactDialog)
        self.label_address.setObjectName(u"label_address")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_address)

        self.lineEdit_address = QLineEdit(UpdateContactDialog)
        self.lineEdit_address.setObjectName(u"lineEdit_address")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_address)

        self.label_notes = QLabel(UpdateContactDialog)
        self.label_notes.setObjectName(u"label_notes")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_notes)

        self.textEdit_notes = QTextEdit(UpdateContactDialog)
        self.textEdit_notes.setObjectName(u"textEdit_notes")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.textEdit_notes)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer)

        self.pushButton_save_changes = QPushButton(UpdateContactDialog)
        self.pushButton_save_changes.setObjectName(u"pushButton_save_changes")

        self.horizontalLayout_buttons.addWidget(self.pushButton_save_changes)

        self.pushButton_cancel = QPushButton(UpdateContactDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_buttons.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)


        self.retranslateUi(UpdateContactDialog)

        QMetaObject.connectSlotsByName(UpdateContactDialog)
    # setupUi

    def retranslateUi(self, UpdateContactDialog):
        UpdateContactDialog.setWindowTitle(QCoreApplication.translate("UpdateContactDialog", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.label_title.setText(QCoreApplication.translate("UpdateContactDialog", u"<h3>\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u041a\u043e\u043d\u0442\u0430\u043a\u0442</h3>", None))
        self.label_name.setText(QCoreApplication.translate("UpdateContactDialog", u"\u0406\u043c'\u044f:", None))
        self.label_phone.setText(QCoreApplication.translate("UpdateContactDialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.label_email.setText(QCoreApplication.translate("UpdateContactDialog", u"Email:", None))
        self.label_address.setText(QCoreApplication.translate("UpdateContactDialog", u"\u0410\u0434\u0440\u0435\u0441\u0430:", None))
        self.label_notes.setText(QCoreApplication.translate("UpdateContactDialog", u"\u041f\u0440\u0438\u043c\u0456\u0442\u043a\u0430:", None))
        self.pushButton_save_changes.setText(QCoreApplication.translate("UpdateContactDialog", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0417\u043c\u0456\u043d\u0438", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("UpdateContactDialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi

