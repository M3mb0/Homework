import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("complaint_db.db")
        self.my_cursor = self.connection.cursor()
        self.table = self.my_cursor.execute(
            """CREATE TABLE IF NOT EXISTS "complaints"(
                "id"	INTEGER NOT NULL UNIQUE,
                "name" TEXT NOT NULL,
                "complaint" TEXT NOT NULL,
                "date" datetime DEFAULT CURRENT_TIMESTAMP,
                "status" INTEGER DEFAULT 0
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            """)

    def add_complaint(self, name, compliant):

        self.my_cursor.execute("""INSERT INTO complaints ('name', 'complaint', 'date') 
        VALUES (?, ?, datetime('now', 'localtime'));""", (name, compliant))
        self.connection.commit()

    def select_compliant(self, user_id):

        id_select = self.my_cursor.execute("""SELECT * FROM complaints WHERE id IN(?);""", (user_id,))
        print(id_select.fetchall())

    def modify_status_solved(self, user_id):

        self.my_cursor.execute("""UPDATE complaints SET status=1 WHERE id IN(?);""", (user_id,))
        self.connection.commit()
        print(f"Complaint with id {user_id} is solved")

    def select_complaint_by_status(self, status):

        status = self.my_cursor.execute("""SELECT * FROM complaints WHERE status=?;""", (status,))
        print(status.fetchall())

    def select_all_complaints(self):

        complaints = self.my_cursor.execute("""SElECT * FROM complaints;""")
        print(complaints.fetchall())