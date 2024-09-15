Overview

In this assignment, you are tasked with developing an advanced command-line Python application that serves as a phone book manager. The application should be equipped to handle a wide array of functionalities, including complex search queries, data validation, batch operations, and more.
Requirements

    User Interface
        Develop a user-friendly command-line interface that facilitates users in performing operations like adding, viewing, searching, updating, and deleting contacts seamlessly.

    Contact Information
        Each contact entry should encompass the following fields:
            First Name
            Last Name
            Phone Number
            Email Address (Optional)
            Address (Optional)

    CRUD Operations
        Your application should enable users to perform the following operations:
            Create new contacts, either individually or through batch imports from a CSV file.
            Retrieve contacts using different parameters such as name or phone number.
            Update existing contacts.
            Delete contacts, individually or in batch mode.

    Search Functionality
        Incorporate advanced search functionality that supports:
            Wildcard searches, allowing partial matches in names and phone numbers.
            Filters to search for contacts added within a specific time frame.

    Sorting and Grouping
        Implement features to sort and group contacts based on various parameters like alphabetical sorting, or grouping by the initial letter of the last name.

    Logging and Auditing
        Develop features to log and audit activities, such as:
            Recording all operations performed in the application along with timestamps.
            Enabling users to view a history of changes made to individual contacts.

    Input Validation
        Instigate comprehensive input validation methods, including:
            Ensuring phone numbers adhere to a pre-defined format (###) ###-####.
            Validating email addresses based on standard criteria.

    Documentation
        Your code should be thoroughly documented, featuring docstrings for functions and comments that elucidate complex code sections.

Steps

    Set up your Python development environment and create necessary files and folders.

    Create a Contact class representing a contact entry with attributes including timestamps for created and updated time.

    Develop the PhoneBook class, which houses methods facilitating CRUD operations along with advanced functionalities like sorting and grouping.

    Create a script that establishes a command-line interface, allowing users to interact with the PhoneBook class and undertake a myriad of operations.

    Incorporate input validation, error handling, and logging mechanisms within your application.

    Test your application exhaustively to ensure that all functionalities operate as intended.

Evaluation Criteria

Your assignment will be assessed based on the following aspects:

    Code Quality and Organization
    Successful Implementation of Advanced Features
    Comprehensive Input Validation and Error Handling
    Effective Logging and Auditing
    Detailed Documentation
