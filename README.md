# Infrastructure Template

Шаблон для развертывания различных инструментов в Docker-контейнерах, с интеграцией с Grafana для мониторинга и сбора метрик.

## Структура проекта

### Основные файлы и папки

- **`docker/Dockerfile`**: Dockerfile для сборки образа. Этот файл описывает, как собрать контейнер для конкретного инструмента.
- **`docker/docker-compose.yml`**: Конфигурация Docker Compose для упрощенного развертывания и запуска нескольких контейнеров одновременно.
- **`docker/config/tool.yml`**: Основная конфигурация для инструмента, который будет развернут. Этот файл описывает параметры самого инструмента (например, порт, API ключи, зависимости).
- **`docker/config/datasources/grafana-datasource.yml`**: Конфигурация источника данных для Grafana, подключающего инструмент для мониторинга.
- **`docker/config/datasources/tool-datasource.yml`**: Конфигурация источника данных для самого инструмента (например, Prometheus или другой мониторинг).
- **`docker-entrypoint.sh`**: Скрипт для старта контейнера и инициализации сервисов.
- **`.gitignore`**: Файл для игнорирования временных и системных файлов, таких как логи, конфигурации с паролями и файлы PyCharm.
- **`README.md`**: Документация проекта.
- **`tutorials/`**: Папка с примерами и инструкциями по настройке и использованию инструментов.

# Развертывание локально

### Требования

- Docker
- Docker Compose

## Шаги

1. ### Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/infrastructure-template.git
   cd infrastructure-template

2. ### Соберите Docker-образ:

   ```bash
   docker build -t my-tool .

3. ### Запустите контейнеры с помощью Docker Compose:
   ```bash
   docker-compose up -d
4. ### Запустите контейнеры с помощью Docker Compose:
   Адрес Grafana -  http://localhost:3000 | Адрес TimescaleDB http://localhost:5432
5. ### Соеденение Grafana и TimescaleDB
   Переходим в http://localhost:3000 -> connections -> Add new connection -> Ищем PostgreSQL -> Add new data source -> Далее заполняем форму подключения (Host URL: timescaledb:5432, TLS/SSL Mode: disable)
6. ### Запустите контейнеры с помощью Docker Compose:
   ```bash
   docker-compose logs
7. ### Для остановки контейнеров:
   ```bash
   docker-compose down


# Развертывание на Linux сервере

### Требования

- Docker
- Docker Compose

### Шаги

1. ### Подключитесь к серверу:

   ```bash
   ssh user@your-server-ip

2. ### Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/infrastructure-template.git
   cd infrastructure-template
   
3. ### Соберите Docker-образ:
   ```bash
   sudo docker build -t my-tool .

4. ### Запустите контейнеры с помощью Docker Compose:
   ```bash
   sudo docker-compose up -d

5. ### Перейдите на Grafana
   Адрес Grafana -  http://localhost:3000 | Адрес TimescaleDB http://localhost:5432
6. ### Соеденение Grafana и TimescaleDB
   Переходим в http://localhost:3000 -> connections -> Add new connection -> Ищем PostgreSQL -> Add new data source -> Далее заполняем форму подключения (Host URL: timescaledb:5432, TLS/SSL Mode: disable)
7. ### Для остановки контейнеров
   ```bash
   sudo docker-compose down
