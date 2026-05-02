import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="user",
        password="password"
    )

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from PostgreSQL!'")
        result = cur.fetchone()
        cur.close()
        conn.close()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(result[0].encode())

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
