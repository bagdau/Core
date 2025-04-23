from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_mysql():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="YOUR_PASSWORD",
            database="Admin"
        )
        cursor = conn.cursor()
        
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"🕐 Время на сервере MySQL: {result[0]}"
    except mysql.connector.Error as err:
        return f"❌ Ошибка подключения к MySQL: {err}"

if __name__ == "__main__":
    app.run(debug=True)
