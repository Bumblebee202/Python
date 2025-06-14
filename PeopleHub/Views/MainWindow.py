from PySide6.QtWidgets import QMainWindow, QDialog, QTableView, QMessageBox, QHeaderView
from PySide6.QtCore import Qt, QAbstractTableModel
from UI.ui_main_dialog import Ui_MainWindow
from Views.CreateContactWindow import CreateContactWindow
from Views.UpdateContactWindow import UpdateContactWindow
from Storage.Models.ContactDTO import ContactDTO
from Storage.Repositories.ContactRepository import ContactRepository
from Storage.DatabaseContext import DatabaseContext

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._dbContext = DatabaseContext()
        self._contactRepository = ContactRepository(self._dbContext)

        self.ui.pushButton_add.clicked.connect(self.AddContactClick)
        self.ui.pushButton_edit.clicked.connect(self.UpdateContactClick)
        self.ui.pushButton_delete.clicked.connect(self.DeleteContactClick)

        self.contacts_table_model = ContactsTableModel()
        self.ui.tableWidget_contacts.setModel(self.contacts_table_model)
        self.ui.tableWidget_contacts.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_contacts.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableWidget_contacts.setSelectionMode(QTableView.SingleSelection)

        self.LoadContacts()

    def LoadContacts(self):
        """Завантажує контакти з репозиторію та оновлює таблицю."""
        try:
            contacts = self._contactRepository.GetAll() # Отримуємо список ContactDTO
            self.contacts_table_model.SetContacts(contacts) # Передаємо їх моделі таблиці
        except Exception as e:
            QMessageBox.critical(self, "Помилка завантаження", f"Не вдалося завантажити контакти: {e}")

    def AddContactClick(self):
        dialog = CreateContactWindow()

        if dialog.exec() == QDialog.Accepted:
            try:
                contact = dialog.GetContact()
                self._contactRepository.CreateContact(contact)
                self.LoadContacts()
            except Exception as e:
                    QMessageBox.critical(self, "Помилка видалення", f"Не вдалося створити контакт: {e}")

    def UpdateContactClick(self):
        selected_indexes = self.ui.tableWidget_contacts.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Помилка", "Будь ласка, оберіть контакт для оновлення.")
            return
        
        rowIndex = selected_indexes[0].row()

        contactToUpdate = self.contacts_table_model.GetContactAtRow(rowIndex)

        dialog = UpdateContactWindow(contactToUpdate)

        if dialog.exec() == QDialog.Accepted:
            try:
                contact = dialog.GetContact()
                self._contactRepository.UpdateContact(contact)
                self.LoadContacts()
            except Exception as e:
                QMessageBox.critical(self, "Помилка видалення", f"Не вдалося оновити контакт: {e}")


    def DeleteContactClick(self):
        selected_indexes = self.ui.tableWidget_contacts.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Помилка", "Будь ласка, оберіть контакт для видалення.")
            return
        
        rowIndex = selected_indexes[0].row()

        contactToDelete = self.contacts_table_model.GetContactAtRow(rowIndex)

        if contactToDelete:

            reply = QMessageBox.question(self, "Підтвердження видалення",
                                         f"Ви впевнені, що хочете видалити контакт '{contactToDelete.Name}'?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                
                try:
                    self._contactRepository.DeleteContact(contactToDelete.Id)
                    self.LoadContacts()

                except Exception as e:
                    QMessageBox.critical(self, "Помилка видалення", f"Не вдалося видалити контакт: {e}")

        





class ContactsTableModel(QAbstractTableModel):
    Headers = ["Id", "Ім'я", "Телефон", "Email", "Адреса", "Примітка"]

    def __init__(self, contactsData: ContactDTO = None, parent = None):
        super().__init__(parent)

        self._contacts: list[ContactDTO] = contactsData or []


    def SetContacts(self, contacts):
        self.beginResetModel()
        self._contacts = contacts
        self.endResetModel()


    def rowCount(self, parent = None):
        return len(self._contacts)
    

    def columnCount(self, parent = None):
        return len(self.Headers)
    

    def data(self, index: int, role = Qt.DisplayRole):
        if not index.isValid():
            return None
        
        if not (0 <= index.row() < self.rowCount() and 0 <= index.column() < self.columnCount()):
            return None

        contact: ContactDTO = self._contacts[index.row()]
        column = index.column()

        if role == Qt.DisplayRole:
            if column == 0: return contact.Id
            if column == 1: return contact.Name
            if column == 2: return contact.Phone
            if column == 3: return contact.Email
            if column == 4: return contact.Address
            if column == 5: return contact.Notes
        return None

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.Headers[section]
        return None

    def GetContactAtRow(self, row: int):
        if 0 <= row < len(self._contacts):
            return self._contacts[row]
        return None