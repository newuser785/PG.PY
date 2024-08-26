import psycopg2
from psycopg2 import sql
import time

# Устанавливаем задержку для обеспечения времени на запуск PostgreSQL
time.sleep(10)

# Данные подключения к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="db",  # имя сервиса в docker-compose
    port="5432"
)

cur = conn.cursor()

# Удаление таблицы employees, если она существует
cur.execute("DROP TABLE IF EXISTS employees")
conn.commit()

# Создание таблицы employees
cur.execute("""
CREATE TABLE employees (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(50),
    Age INTEGER,
    Department VARCHAR(50)
)
""")
conn.commit()

# Добавление данных в таблицу employees
cur.execute("""
INSERT INTO employees (Name, Age, Department) VALUES
('Danielle', 40, 'Finance'),
('Edward', 45, 'Legal'),
('Fiona', 50, 'Finance')
""")
conn.commit()

# Получение данных из таблицы employees
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

# Вывод данных
print("ID, Name, Age, Department")
for row in rows:
    print(row)

# Закрытие курсора и соединения
cur.close()
conn.close()
