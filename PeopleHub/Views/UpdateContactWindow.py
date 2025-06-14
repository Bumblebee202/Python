from PySide6.QtWidgets import QDialog
from UI.ui_update_contact_dialog import Ui_UpdateContactDialog
from Storage.Models.ContactDTO import ContactDTO

class UpdateContactWindow(QDialog):



    def __init__(self, contact: ContactDTO):
        super().__init__()

        self.ui = Ui_UpdateContactDialog()
        self.ui.setupUi(self)

        self.ui.pushButton_save_changes.clicked.connect(self.accept) 
        self.ui.pushButton_cancel.clicked.connect(self.reject)

        self._contact = contact;
        self.ui.lineEdit_name.setText(contact.Name)
        self.ui.lineEdit_phone.setText(contact.Phone)
        self.ui.lineEdit_email.setText(contact.Email)
        self.ui.lineEdit_address.setText(contact.Address)
        self.ui.textEdit_notes.setText(contact.Notes)



    def GetContact(self):
        return ContactDTO(
            Id = self._contact.Id,
            Name = self.ui.lineEdit_name.text(),
            Phone = self.ui.lineEdit_phone.text(),
            Email = self.ui.lineEdit_email.text(),
            Address = self.ui.lineEdit_address.text(),
            Notes = self.ui.textEdit_notes.toPlainText()
        )