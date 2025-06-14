from PySide6.QtWidgets import QDialog
from UI.ui_create_contact_dialog import Ui_CreateContactDialog
from Storage.Models.ContactDTO import ContactDTO

class CreateContactWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_CreateContactDialog()
        self.ui.setupUi(self)

        self.ui.pushButton_save.clicked.connect(self.accept) 
        self.ui.pushButton_cancel.clicked.connect(self.reject)


    def GetContact(self):
        return ContactDTO(
            Id = None,
            Name = self.ui.lineEdit_name.text(),
            Phone = self.ui.lineEdit_phone.text(),
            Email = self.ui.lineEdit_email.text(),
            Address = self.ui.lineEdit_address.text(),
            Notes = self.ui.textEdit_notes.toPlainText()
        )