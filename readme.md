# PhoneBook CLI Documentation

Welcome to the PhoneBook CLI! This command-line interface allows you to manage your contacts efficiently. You can perform various operations like adding, viewing, searching, updating, and deleting contacts. This document will guide you through the usage of the PhoneBook CLI.

## Table of Contents

1. Installation
2. Data Structure
3. Usage
   - [Add a Contact](#add-a-contact)
   - [Update a Contact](#update-a-contact)
   - [Delete a Contact](#delete-a-contact)
   - [List All Contacts](#list-all-contacts)
   - [Import Contacts from CSV](#import-contacts-from-csv)
   - [Export Contacts to CSV](#export-contacts-to-csv)
   - [Sort Contacts](#sort-contacts)
   - [Group Contacts](#group-contacts)
   - [Search Contacts](#search-contacts)
   - [Filter Contacts by Time Frame](#filter-contacts-by-time-frame)
4. [Input Validation](#input-validation)
5. [Logging and Auditing](#logging-and-auditing)

## Installation

1. **Clone the repository**:
    First, you need to clone the repository from GitHub to your local machine. Open your terminal and run the following command:
    ```sh
    git clone https://github.com/ivanivan999/GNG-5300-Python.git
    ```
    This command will create a directory named `phonebook-cli` in your current working directory and download all the project files into it.

2. **Navigate to the project directory**:
    Change your current directory to the project directory:
    ```sh
    cd phonebook-cli
    ```

3. **Run the application**:
    You can now run the PhoneBook CLI application. Use the following command to see the available options:
    ```sh
    python cli.py --help
    ```

By following these steps, you will have the PhoneBook CLI set up and ready to use on your local machine.

## Data Structure

### Contact

Each contact in the PhoneBook CLI is represented as a dictionary with the following keys:

- `first_name` (string): The first name of the contact.
- `last_name` (string): The last name of the contact.
- `phone` (string): The phone number of the contact in the format `(###) ###-####`.
- `email` (string, optional): The email address of the contact.
- `address` (string, optional): The physical address of the contact.

Example:
```python
contact = {
    "first_name": "John",
    "last_name": "Doe",
    "phone": "(123) 456-7890",
    "email": "john.doe@example.com",
    "address": "123 Main St"
}
```

### PhoneBook

The phonebook is a list of contacts. Each contact is stored as a dictionary within this list.

Example:
```python
phonebook = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "(123) 456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main St"
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "phone": "(555) 123-4567",
        "email": "alice.smith@example.com",
        "address": "456 Elm St"
    }
]
```

The phonebook allows you to perform various operations such as adding, updating, deleting, and searching for contacts.



## Usage

### Add a Contact

To add a new contact, use the [`add`] action with the required fields: `first_name`, `last_name`, and `phone`. Optional fields include `email` and `address`. Note that the contact cannot be a duplicate; if a contact with the same first name, last name, email, address, and phone number already exists, it will not be added or imported.

```sh
python cli.py add --first_name "John" --last_name "Doe" --phone "(123) 456-7890" --email "john.doe@example.com" --address "123 Main St"
```

### Update a Contact

To update an existing contact, use the [`update`] action with the `index` of the contact and the fields you want to update.

```sh
python cli.py update --index 0 --phone "(987) 654-3210" --email "john.new@example.com"
```

### Delete a Contact

To delete a contact, use the [`delete`] action with the `index` of the contact.

```sh
python cli.py delete --index 0
```
### Batch Delete Contacts

To delete multiple contacts from the phonebook, provide a comma-separated list of indices:

```sh
python cli.py delete_batch --indices "1,2,3"
```


### List All Contacts

To list all contacts, use the [`list`] action.

```sh
python cli.py list
```

### Import Contacts from CSV

To import contacts from a CSV file, use the [`import`] action with the `path` to the CSV file. The CSV file should have the following columns: `first_name`, `last_name`, `phone`, `email`, `address`.

```sh
python3 cli.py import --path "data/contacts.csv"
```
### Export Contacts to CSV

To export all contacts to a CSV file, use the following command:

```sh
python cli.py export --path "exported_contacts.csv"
```

### Sort Contacts

To sort contacts, use the [`sort`] action with the `key` to sort by (e.g., `first_name`, `last_name`, `phone`).

```sh
python cli.py sort --key "last_name"
```

### Group Contacts

To group contacts, use the [`group`] action with the `key` to group by (e.g., `first_name`, `last_name`).

```sh
python cli.py group --key "last_name"
```

### Search Contacts

To search for contacts, use the [`search`] action with the `query` for wildcard search.

```sh
python cli.py search --query "John"
```

### Filter Contacts by Time Frame

To filter contacts added within a specific time frame, use the [`filter`] action with `start_date` and `end_date`.

```sh
python cli.py filter --start_date "2023-01-01" --end_date "2023-12-31"
```

## Add and Import Validation

### Add Validation

- **Phone Number**: Must be in the format `(###) ###-####`.
- **Email Address**: Must be a valid email address format.

### Duplicate Contact Prevention

If a contact with the same first name, last name, email, address and phone number already exists in the phonebook, the new contact will not be added. This validation helps maintain the integrity of the contact list by preventing duplicate entries.

## Logging and Auditing

All operations performed in the application are logged with timestamps. You can view the logs to see a history of changes made to individual contacts.

## Example

Here is an example of a typical session:

1. Add a contact:
    ```sh
    python cli.py add --first_name "Alice" --last_name "Smith" --phone "(555) 123-4567" --email "alice.smith@example.com" --address "456 Elm St"
    ```

2. List all contacts:
    ```sh
    python cli.py list
    ```

3. Update a contact:
    ```sh
    python cli.py update --index 0 --phone "(555) 765-4321"
    ```

4. Search for a contact:
    ```sh
    python cli.py search --query "Alice"
    ```

5. Delete a contact:
    ```sh
    python cli.py delete --index 0
    ```

6. Batch delete contacts:
   ```sh
    python cli.py delete_batch --indices "1,2,3"
    ```

7. Import contacts from a CSV file:
    ```sh
    python cli.py import --path "data/contacts.csv"
    ```
8. Export Contacts to CSV file:
    ```sh
    python3 cli.py export --path "data/exported_contacts.csv"
    ```

9.  Sort contacts by last name:
    ```sh
    python cli.py sort --key "last_name"
    ```

10. Group contacts by first name:
    ```sh
    python cli.py group --key "first_name"
    ```

11. Filter contacts by time frame:
    ```sh
    python cli.py filter --start_date "2023-01-01" --end_date "2023-12-31"
    ```
## Test
### Running Unit Tests
To ensure the functionality of the CLI and the phonebook application, unit tests have been created. These tests verify that the various commands and features work as expected.

To run the unit tests, use the following command:

```sh
python -m unittest tests/test_cli.py
```

## Conclusion

The Phonebook CLI is a command-line application designed to manage contacts efficiently. It supports various operations such as adding, updating, deleting, searching, and sorting contacts. The application is built with Python and provides a user-friendly interface for managing contact lists. It also includes functionalities for importing and exporting contacts in CSV format and supports features like logging and auditing. For any further assistance, refer to the help option:

```sh
python cli.py --help
```

Thank you for using the PhoneBook CLI!