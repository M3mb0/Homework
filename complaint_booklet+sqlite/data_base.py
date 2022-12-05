"""This script reads, insert and creates data in SQlite database and contains the fallowing:

Class:
-------------
    Database:
        class takes 3 attributes
Method:
-------------
    add_complaint:
        adding a complaint to the table
    select_complaint:
        selecting a complaint
    solve_complaint:
        mark as solved a certain complaint
    select_complaint_by_status:
        selects complaints for view by status(solved or not)
    select_all_complaints:
        prints all complaints

Other imports:
-------------
    sqlite3:
        for iterating through the database and inserting info into it
"""


import sqlite3


class Database:
    """Class is used to create a table which contain id, name, email, complaint, date and status.
    Class has 3 attributes which are already set.

    Attributes:
    -------------
        self.connection:
            creates the connection with the database
        self.my_cursor:
            creates the cursor
        self.table:
            creates the table if not exists
    """
    def __init__(self):
        self.connection = sqlite3.connect("complaint_db.db")
        self.my_cursor = self.connection.cursor()
        self.table = self.my_cursor.execute(
            """CREATE TABLE IF NOT EXISTS "complaints"(
                "id"	INTEGER NOT NULL UNIQUE,
                "name" TEXT NOT NULL,
                "email" TEXT NOT NULL UNIQUE,
                "complaint" TEXT NOT NULL,
                "date" TEXT NOT NULL,
                "status" INTEGER DEFAULT 0,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            """)

    def add_complaint(self, name, email, compliant, date):
        """Adding a complaint in the table and method takes 4 arguments.

        Arguments:
        -------------
            name: str
                the name of the person
            email: str
                the email address of the person
            complaint: str
                the actual complaint that the person has
            date: str
                date when the complaint has made
        """
        self.my_cursor.execute("""INSERT INTO complaints ('name', 'email', 'complaint', 'date') 
        VALUES (?, ?, ?, ?);""", (name, email, compliant, date))
        self.connection.commit()

    def select_compliant(self, user_id):
        """selecting a complaint by ID and returns it if exists.Method takes 1 argument

        Arguments:
        -------------
            user_id = int
                the id number of the person you are searching for
        """
        id_select = self.my_cursor.execute("""SELECT * FROM complaints WHERE id IN(?);""", (user_id,))
        fetch = id_select.fetchall()
        if fetch:
            return fetch

    def solve_complaint(self, user_id):
        """mark a complaint as solved and method takes 1 argument.If id is found it prints solved
        otherwise it prints that the id is not found
        Arguments:
        -------------
            user_id = int
                the id number of the person you are searching for
        """
        if Database.select_compliant(self, user_id):
            self.my_cursor.execute("""UPDATE complaints SET status=1 WHERE id IN(?);""", (user_id,))
            self.connection.commit()
            print(f"Complaint with id {user_id} is solved")
        else:
            print(f"ID {user_id} not found")

    def select_complaint_by_status(self, status):
        """selects a complaint by status (solved or not) and prints the complaint.
        method takes one argument.

        Arguments:
        -------------
            status: int
                1 for solved or 0 for those which needs to be solved
        """
        my_status = self.my_cursor.execute("""SELECT * FROM complaints WHERE status=?;""", (status,))
        print(my_status.fetchall())

    def select_all_complaints(self):
        """selects all complaints and prints them. Method takes 0 arguments"""
        complaints = self.my_cursor.execute("""SElECT * FROM complaints;""")
        print(complaints.fetchall())
