# Используем базовый образ Python
FROM python:3.10-slim

# Установка зависимостей
RUN pip install psycopg2-binary

# Установка рабочей директории
WORKDIR /app

# Копирование файлов в контейнер
COPY app.py .

# Запуск скрипта app.py
CMD ["python", "app.py"]
