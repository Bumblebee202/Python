from dataclasses import dataclass

@dataclass
class ContactDTO:
    Id: int
    Name: str
    Phone: str
    Email: str
    Address: str
    Notes: str