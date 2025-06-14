from Storage.Models.ContactDTO import ContactDTO
from Storage.DatabaseContext import DatabaseContext

class ContactRepository:
    def __init__(self, context: DatabaseContext):
        self._dbContext = context


    def GetAll(self) -> list[ContactDTO]:
        sql = """
select *
from Contacts
"""

        with self._dbContext as connection:
            cursor = connection.cursor()

            cursor.execute(sql)
            rows = cursor.fetchall()

            return [ContactDTO(Id = row[0], Name = row[1], Phone = row[2], Email = row[3], Address = row[4], Notes = row[5]) for row in rows]
    
    def CreateContact(self, contact: ContactDTO):
        sql = """
insert into Contacts (Name, Phone, Email, Address, Notes)
values (?, ?, ?, ?, ?)
"""

        with self._dbContext as connection:
            cursor = connection.cursor()

            cursor.execute(sql, (
                contact.Name,
                contact.Phone,
                contact.Email,
                contact.Address,
                contact.Notes
            ))
            connection.commit()

            contact.Id = cursor.lastrowid



    def UpdateContact(self, contact: ContactDTO):
        sql = """
update contacts
set
    Name = ?,
    Phone = ?,
    Email = ?,
    Address = ?,
    Notes = ?
where Id = ?
"""

        with self._dbContext as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (
                contact.Name,
                contact.Phone,
                contact.Email,
                contact.Address,
                contact.Notes,
                contact.Id
            ))
            connection.commit()


    def DeleteContact(self, id: int):
        sql = """
delete from contacts
where Id = ?
"""

        with self._dbContext as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()