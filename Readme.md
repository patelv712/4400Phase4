## Environment Setup

1. Install Python 3.9 or later.
2. Install MySQL Server 8.0 or later.
3. Install the required MySql connector for Python using pip: `pip install mysql-connector-python`

## Database Setup

Set up the database by following these steps:

1. Initialize the database for testing by executing the SQL script **`cs4400_phase3_flight_management_db_STARTING_POINT_v2.sql`**. This script will create the necessary tables and populate them with sample data.
2. Import the stored procedures and views used by the app by executing the SQL script **`cs4400_phase4_stored_procedures_team35.sql`**. 

Make sure to execute these scripts in your MySQL server before running the application to ensure that the database is set up correctly.

## Run the Application

Before running the application, make sure to update the database connection settings in the **`main.py`** file. Modify the **`localhost`**, **`user`**, and **`password`** fields to match your MySQL server's configuration.

To run the application, you can use your preferred IDE, or simply execute the following command in your terminal or command prompt: **`python main.py`** 

This command will launch the application, allowing you to interact with its features.

## Technology

1. **Tkinter**, a standard Python library, enables the creation of lightweight and responsive GUIs. As part of the Python standard library, Tkinter provides a wide range of widgets and tools that simplify the process of creating a user-friendly interface, without requiring additional installation.
2. **MySQL Connector** is a Python driver for communicating with MySQL databases. It allows our application to connect to the MySQL database, execute SQL queries, and retrieve results. It facilitates seamless integration between our application and the database.

## Teamwork Distribution

- Lu Liu: Query 3, 9, 19~25 GUI Development
- Wilton Chuah: Query 4, 13, 14, 15, 17, 18 GUI Development
- Yusen Su: Query 5, 10, 11, 12, 16 GUI Development
- Varun Patel: Query 1, 2, 6, 7, 8 GUI Development