import sqlite3


class Database:

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

        self.my_cursor.execute("""INSERT INTO complaints ('name', 'email', 'complaint', 'date') 
        VALUES (?, ?, ?, ?);""", (name, email, compliant, date))
        self.connection.commit()

    def select_compliant(self, user_id):

        id_select = self.my_cursor.execute("""SELECT * FROM complaints WHERE id IN(?);""", (user_id,))
        fetch = id_select.fetchall()
        if fetch:
            return fetch

    def solve_complaint(self, user_id):

        if Database.select_compliant(self, user_id):
            self.my_cursor.execute("""UPDATE complaints SET status=1 WHERE id IN(?);""", (user_id,))
            self.connection.commit()
            print(f"Complaint with id {user_id} is solved")
        else:
            print(f"ID {user_id} not found")

    def select_complaint_by_status(self, status):

        status = self.my_cursor.execute("""SELECT * FROM complaints WHERE status=?;""", (status,))
        print(status.fetchall())

    def select_all_complaints(self):

        complaints = self.my_cursor.execute("""SElECT * FROM complaints;""")
        print(complaints.fetchall())
