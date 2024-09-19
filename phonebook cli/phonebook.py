# phonebook.py
import json
import logging
from datetime import datetime
import fnmatch
import csv

from contact import Contact

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PhoneBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
        logging.info("PhoneBook initialized")

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump([contact.to_dict() for contact in self.contacts], f, indent=4)
        logging.info("Contacts saved to file")

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                logging.info("Contacts loaded from file")
                return [Contact.from_dict(data) for data in json.load(f)]
        except FileNotFoundError:
            logging.warning("Contacts file not found, starting with an empty phonebook")
            return []

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        logging.info(
            f"Contact added: {contact.first_name} {contact.last_name}, "
            f"Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}"
        )

    def update_contact(self, index, first_name=None, last_name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            self.contacts[index].update(first_name, last_name, phone, email, address)
            self.save_contacts()
            logging.info(f"Contact at index {index} updated")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            contact = self.contacts.pop(index)
            self.save_contacts()
            logging.info(
                f"Contact deleted: {contact.first_name} {contact.last_name}, "
                f"Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}"
            )

    def list_contacts(self):
        logging.info("Listing all contacts")
        return self.contacts

    def sort_contacts(self, key):
        self.contacts.sort(key=lambda contact: getattr(contact, key))
        self.save_contacts()
        logging.info(f"Contacts sorted by {key}")

    def group_contacts(self, key):
        grouped = {}
        for contact in self.contacts:
            group_key = getattr(contact, key)
            if group_key not in grouped:
                grouped[group_key] = []
            grouped[group_key].append(contact)
        logging.info(f"Contacts grouped by {key}")
        return grouped

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if (
                fnmatch.fnmatch(contact.first_name, f"*{query}*")
                or fnmatch.fnmatch(contact.last_name, f"*{query}*")
                or fnmatch.fnmatch(contact.phone, f"*{query}*")
            ):
                results.append(contact)
        logging.info(f"Contacts searched with query: {query}")
        return results

    def filter_contacts_by_time_frame(self, start_date, end_date):
        results = []
        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)
        for contact in self.contacts:
            created_at = datetime.fromisoformat(contact.created_at)
            if start_date <= created_at <= end_date:
                results.append(contact)
        logging.info(f"Contacts filtered by time frame: {start_date} to {end_date}")
        return results

    def import_contacts_from_csv(self, csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    phone=row['phone'],
                    email=row.get('email'),
                    address=row.get('address')
                )
                self.add_contact(contact)
        logging.info(f"Contacts imported from CSV file: {csv_file}")

    def export_contacts_to_csv(self, csv_file):
        """Export contacts to a CSV file."""
        with open(csv_file, mode='w', newline='') as file:
            fieldnames = ['first_name', 'last_name', 'phone', 'email', 'address', 'created_at', 'updated_at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
        logging.info(f"Contacts exported to CSV file: {csv_file}")