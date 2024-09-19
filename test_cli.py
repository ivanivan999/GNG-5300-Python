import unittest
from unittest.mock import MagicMock, patch
from phonebook import PhoneBook, Contact

# test_cli.py
from cli import (
    validate_phone, validate_email, add_contact, update_contact, delete_contact,
    list_contacts, import_contacts, export_contacts, sort_contacts, group_contacts,
    search_contacts, filter_contacts
)

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.phonebook = MagicMock(spec=PhoneBook)
        self.args = MagicMock()

    def test_validate_phone_valid(self):
        validate_phone("(123) 456-7890")  # Should not raise an exception

    def test_validate_phone_invalid(self):
        with self.assertRaises(ValueError):
            validate_phone("123-456-7890")

    def test_validate_email_valid(self):
        validate_email("test@example.com")  # Should not raise an exception

    def test_validate_email_invalid(self):
        with self.assertRaises(ValueError):
            validate_email("test@com")

    def test_add_contact_success(self):
        self.args.first_name = "John"
        self.args.last_name = "Doe"
        self.args.phone = "(123) 456-7890"
        self.args.email = "john.doe@example.com"
        self.args.address = "123 Main St"
        add_contact(self.args, self.phonebook)
        self.phonebook.add_contact.assert_called_once()

    def test_add_contact_missing_fields(self):
        self.args.first_name = None
        self.args.last_name = None
        self.args.phone = None
        self.args.email = None
        self.args.address = None

        with self.assertRaises(ValueError):
            add_contact(self.args, self.phonebook)


    def test_update_contact_success(self):
        self.args.index = 0
        self.args.first_name = "John"
        self.args.last_name = "Doe"
        self.args.phone = "(123) 456-7890"
        self.args.email = "john.doe@example.com"
        self.args.address = "123 Main St"
        update_contact(self.args, self.phonebook)
        self.phonebook.update_contact.assert_called_once()

    def test_update_contact_missing_index(self):
        self.args.index = None
        with self.assertRaises(ValueError):
            update_contact(self.args, self.phonebook)

    def test_delete_contact_success(self):
        self.args.index = 0
        delete_contact(self.args, self.phonebook)
        self.phonebook.delete_contact.assert_called_once()

    def test_delete_contact_missing_index(self):
        self.args.index = None
        with self.assertRaises(ValueError):
            delete_contact(self.args, self.phonebook)

    def test_list_contacts(self):
        self.args = MagicMock()
        list_contacts(self.args, self.phonebook)
        self.phonebook.list_contacts.assert_called_once()

    @patch('builtins.print')
    def test_import_contacts_success(self, mock_print):
        self.args.path = "contacts.csv"
        import_contacts(self.args, self.phonebook)
        self.phonebook.import_contacts_from_csv.assert_called_once_with("contacts.csv")
        mock_print.assert_called_with("Contacts imported from contacts.csv.")

    @patch('builtins.print')
    def test_import_contacts_invalid_path(self, mock_print):
        self.args.path = "contacts.txt"
        import_contacts(self.args, self.phonebook)
        mock_print.assert_called_with("Error: The file must be in CSV format.")

    @patch('builtins.print')
    def test_export_contacts_success(self, mock_print):
        self.args.path = "contacts.csv"
        export_contacts(self.args, self.phonebook)
        self.phonebook.export_contacts_to_csv.assert_called_once_with("contacts.csv")
        mock_print.assert_called_with("Contacts exported to contacts.csv.")

    @patch('builtins.print')
    def test_export_contacts_invalid_path(self, mock_print):
        self.args.path = "contacts.txt"
        export_contacts(self.args, self.phonebook)
        mock_print.assert_called_with("Error: The file must be in CSV format.")

    def test_sort_contacts(self):
        self.args.key = "last_name"
        sort_contacts(self.args, self.phonebook)
        self.phonebook.sort_contacts.assert_called_once_with("last_name")

    def test_group_contacts(self):
        self.args.key = "last_name"
        group_contacts(self.args, self.phonebook)
        self.phonebook.group_contacts.assert_called_once_with("last_name")

    def test_search_contacts(self):
        self.args.query = "John"
        search_contacts(self.args, self.phonebook)
        self.phonebook.search_contacts.assert_called_once_with("John")

    def test_filter_contacts(self):
        self.args.start_date = "2023-01-01"
        self.args.end_date = "2023-12-31"
        filter_contacts(self.args, self.phonebook)
        self.phonebook.filter_contacts_by_time_frame.assert_called_once_with("2023-01-01", "2023-12-31")

if __name__ == '__main__':
    unittest.main()