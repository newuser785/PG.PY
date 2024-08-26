# Приложение для анализа файловой системы с использованием PostgreSQL и Python

## Описание

Этот проект создаёт систему, состоящую из двух контейнеров (PostgreSQL и Python-приложение), использующую Docker Compose. Python-приложение будет взаимодействовать с базой данных, создавая таблицы, добавляя записи и выводя данные.

## Структура проекта

Проект состоит из следующих файлов:

├── app.py        # Основной Python-скрипт

├── README.md     # руководство по использованию

├── Dockerfile    # Dockerfile для сборки Docker-образа Python-приложения

├── docker-compose.yml     # Docker Compose файл для координирования контейнеров

## Screenshots

├── docker.d  # docker desktop containers

├── terminal-conclusion   # вывод с данными из таблицы `employees`:

## Как использовать

### Предварительные требования

- Docker
- Docker Compose

### Шаги для запуска

1. Клонируйте репозиторий:

git clone https://github.com/newuser785/PG.PY.git

cd PG.PY

2. Запустите контейнеры с помощью Docker Compose:

docker-compose up

### Ожидаемый вывод

После выполнения команды `docker-compose up` вы должны увидеть вывод с данными из таблицы `employees`:


ID, Name, Age, Department

(1, 'Danielle', 40, 'Finance')

(2, 'Edward', 45, 'Legal')

(3, 'Fiona', 50, 'Finance')

# Docker Hub
Docker-образ doclinx/python-file-analyzer доступен по следующей ссылке: https://hub.docker.com/r/doclinx/python-file-analyzer
