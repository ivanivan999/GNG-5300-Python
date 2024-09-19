# contact.py
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Contact:
    def __init__(self, first_name, last_name, phone, email=None, address=None, created_at=None, updated_at=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = created_at or datetime.now().isoformat()
        self.updated_at = updated_at or datetime.now().isoformat()
        logging.info(
            f"Contact created: {self.first_name} {self.last_name}, "
            f"Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
        )

    def update(self, first_name=None, last_name=None, phone=None, email=None, address=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        self.updated_at = datetime.now().isoformat()
        logging.info(
            f"Contact updated: {self.first_name} {self.last_name}, "
            f"Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
        )

    def to_dict(self):
        """Convert the contact to a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Contact instance from a dictionary."""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data["phone"],
            email=data.get("email"),
            address=data.get("address"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )