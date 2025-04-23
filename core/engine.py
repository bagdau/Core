class CoreEngine:
    def __init__(self, db_conn):
        self.conn = db_conn

    def fetch_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        return [dict(row) for row in cur.fetchall()]

    def add_user(self, name, email):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()
        return {"status": "added"}
