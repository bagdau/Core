from core.engine import CoreEngine
from database.db import get_connection, initialize_database
from server import app

def main():
    # Создание таблиц, если их нет
    initialize_database()

    # Подключение к базе данных
    conn = get_connection()

    # Инициализация ядра с подключением к БД
    engine = CoreEngine(conn)

    # Пример работы: добавим пользователя и выведем всех
    print("🔧 Добавляем пользователя...")
    engine.add_user("Бағдаулет", "bagdat@example.com")

    print("📄 Все пользователи:")
    users = engine.fetch_all_users()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
