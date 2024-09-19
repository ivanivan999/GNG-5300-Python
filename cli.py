# cli.py
import argparse
import logging
import re

from phonebook.phonebook import PhoneBook, Contact

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_phone(phone):
    """Validate the phone number format."""
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    if not pattern.match(phone):
        raise ValueError(
            "Phone number must be in the format (###) ###-####. "
            "Please provide a valid phone number."
        )

def validate_email(email):
    """Validate the email address format."""
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    if email and not pattern.match(email):
        raise ValueError(
            "Invalid email address. Please provide a valid email address."
            )
    
def add_contact(args, phonebook):
    """Add a new contact to the phonebook."""
    if args.first_name and args.last_name and args.phone:
        try:
            validate_phone(args.phone)
            if args.email:
                validate_email(args.email)
            contact = Contact(
                args.first_name, args.last_name, args.phone, args.email, args.address
            )
            phonebook.add_contact(contact)
            logging.info("Contact added successfully.")
            print("Contact added successfully.")
        except ValueError as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")
    else:
        error_message = "First name, last name, and phone are required to add a contact."
        logging.error(f"Error: {error_message}")
        print(f"Error: {error_message}")
        raise ValueError(error_message)

def update_contact(args, phonebook):
    """Update an existing contact in the phonebook."""
    if args.index is not None:
        try:
            if args.phone:
                validate_phone(args.phone)
            if args.email:
                validate_email(args.email)
            phonebook.update_contact(
                args.index, args.first_name, args.last_name, 
                args.phone, args.email, args.address
            )
            logging.info("Contact updated successfully.")
            print("Contact updated successfully.")
        except ValueError as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")
    else:
        logging.error("Error: Index is required to update a contact.")
        print("Error: Please provide the index of the contact to update.")
        raise ValueError("Index is required to update a contact.")

def delete_contact(args, phonebook):
    """Delete a contact from the phonebook."""
    if args.index is not None:
        phonebook.delete_contact(args.index)
        logging.info("Contact deleted successfully.")
        print("Contact deleted successfully.")
    else:
        error_message = "Index is required to delete a contact."
        logging.error(f"Error: {error_message}")
        print("Error: Please provide the index of the contact to delete.")
        raise ValueError(error_message)

def delete_contacts(args, phonebook):
    """Delete multiple contacts from the phonebook."""
    if args.indices:
        indices = [int(index) - 1 for index in args.indices.split(',')]
        phonebook.delete_contacts(indices)
        logging.info("Contacts deleted successfully.")
        print("Contacts deleted successfully.")
    else:
        error_message = "Indices are required to delete contacts."
        logging.error(f"Error: {error_message}")
        print("Error: Please provide the indices of the contacts to delete.")
        raise ValueError(error_message)
    
def list_contacts(args, phonebook):
    """List all contacts in the phonebook."""
    contacts = phonebook.list_contacts()
    if contacts:
        for i, contact in enumerate(contacts):
            print_contact_info(i, contact)
        logging.info("Listed all contacts.")
    else:
        print("No contacts found.")
        logging.info("No contacts found.")


def import_contacts(args, phonebook):
    """Import contacts from a CSV file."""
    if args.path:
        if args.path.endswith('.csv'):
            try:
                phonebook.import_contacts_from_csv(args.path)
                logging.info(f"Contacts imported from {args.path}.")
                print(f"Contacts imported from {args.path}.")
            except FileNotFoundError:
                logging.error(f"Error: The file '{args.path}' was not found. Please check the file path and try again.")
                print(f"Error: The file '{args.path}' was not found. Please check the file path and try again.")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print(f"An unexpected error occurred: {e}")
        else:
            logging.error("Error: The file must be in CSV format.")
            print("Error: The file must be in CSV format.")
    else:
        logging.error("Error: Path to CSV file is required to import contacts.")
        print("Error: Please provide the path to the CSV file to import contacts.")


def export_contacts(args, phonebook):
    """Export contacts to a CSV file."""
    if args.path:
        if args.path.endswith('.csv'):
            try:
                phonebook.export_contacts_to_csv(args.path)
                logging.info(f"Contacts exported to {args.path}.")
                print(f"Contacts exported to {args.path}.")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print(f"An unexpected error occurred: {e}")
        else:
            logging.error("Error: The file must be in CSV format.")
            print("Error: The file must be in CSV format.")
    else:
        logging.error("Error: Path to CSV file is required to export contacts.")
        print("Error: Please provide the path to the CSV file to export contacts.")


def sort_contacts(args, phonebook):
    """Sort contacts in the phonebook."""
    if args.key:
        phonebook.sort_contacts(args.key)
        logging.info(f"Contacts sorted by {args.key}.")
        sorted_contacts = phonebook.list_contacts()
        for i, contact in enumerate(sorted_contacts):
            print_contact_info(i, contact)
        print(f"Contacts sorted by {args.key}.")
    else:
        logging.error("Error: Key is required to sort contacts.")
        print("Error: Please provide the key to sort contacts.")


def print_contact_info(i, contact):
    print(f"Contact {i + 1}:")
    print(f"  First Name: {contact.first_name}")
    print(f"  Last Name: {contact.last_name}")
    print(f"  Phone: {contact.phone}")
    print(f"  Email: {contact.email}")
    print(f"  Address: {contact.address}")
    print(f"  Created At: {contact.created_at}")
    print(f"  Updated At: {contact.updated_at}")
    print()


def group_contacts(args, phonebook):
    """Group contacts in the phonebook."""
    if args.key:
        grouped = phonebook.group_contacts(args.key)
        for key, group in grouped.items():
            print(f"\nGroup: {key}")
            print("=" * 50)
            for i, contact in enumerate(group):
                print_contact_info(i, contact)
                print("-" * 50)
        logging.info(f"Contacts grouped by {args.key}.")
        print(f"Contacts grouped by {args.key}.")
    else:
        logging.error("Error: Key is required to group contacts.")
        print("Error: Please provide the key to group contacts.")


def search_contacts(args, phonebook):
    """Search for contacts in the phonebook."""
    if args.query:
        results = phonebook.search_contacts(args.query)
        if results:
            print("\nSearch Results:")
            print("=" * 50)
            for i, contact in enumerate(results):
                print_contact_info(i, contact)
                print("-" * 50)
            logging.info(f"Searched contacts with query: {args.query}.")
        else:
            print("No contacts found matching the query.")
            logging.info(f"No contacts found with query: {args.query}.")
    else:
        logging.error("Error: Query is required to search contacts.")
        print("Error: Please provide a search query.")


def filter_contacts(args, phonebook):
    """Filter contacts by a time frame in the phonebook."""
    if args.start_date and args.end_date:
        results = phonebook.filter_contacts_by_time_frame(args.start_date, args.end_date)
        if results:
            print("\nFiltered Contacts:")
            print("=" * 50)
            for i, contact in enumerate(results):
                print_contact_info(i, contact)
                print("-" * 50)
            logging.info(f"Filtered contacts by time frame: {args.start_date} to {args.end_date}.")
        else:
            print("No contacts found within the specified time frame.")
            logging.info(f"No contacts found from {args.start_date} to {args.end_date}.")
    else:
        logging.error("Error: Start date and end date are required to filter contacts.")
        print("Error: Please provide both start date and end date to filter contacts.")

def main():
    """Main function to parse arguments and execute the corresponding action."""
    # Welcome message
    print("Welcome to the PhoneBook CLI!")
    print("You can perform various operations like adding, viewing, searching, updating, and deleting contacts.")
    print("Use the --help option to see available commands and options.")
    print("=" * 50)

    parser = argparse.ArgumentParser(description="PhoneBook CLI")
    parser.add_argument("action", choices=["add", "update", "delete", "delete_batch", "list", "import", "export", "sort", "group", "search", "filter"])
    parser.add_argument("--first_name", help="First name of the contact")
    parser.add_argument("--last_name", help="Last name of the contact")
    parser.add_argument("--phone", help="Phone number of the contact")
    parser.add_argument("--email", help="Email of the contact")
    parser.add_argument("--address", help="Address of the contact")
    parser.add_argument("--index", type=int, help="Index of the contact to update or delete")
    parser.add_argument("--indices", help="Comma-separated indices of contacts to delete")
    parser.add_argument("--path", help="Path to the CSV file to import/export contacts")
    parser.add_argument("--key", help="Key to sort or group by")
    parser.add_argument("--query", help="Search query for wildcard search")
    parser.add_argument("--start_date", help="Start date for filtering contacts (YYYY-MM-DD)")
    parser.add_argument("--end_date", help="End date for filtering contacts (YYYY-MM-DD)")

    args = parser.parse_args()
    phonebook = PhoneBook()

    actions = {
        "add": add_contact,
        "update": update_contact,
        "delete": delete_contact,
        "delete_batch": delete_contacts,
        "list": list_contacts,
        "import": import_contacts,
        "export": export_contacts,
        "sort": sort_contacts,
        "group": group_contacts,
        "search": search_contacts,
        "filter": filter_contacts
    }

    action = actions.get(args.action)
    if action:
        action(args, phonebook)
    else:
        logging.error("Invalid action.")
        print("Invalid action. Please choose from 'add', 'update', 'delete', 'delete_batch', 'list', 'import', 'export', 'sort', 'group', 'search', or 'filter'.")

if __name__ == "__main__":
    main()