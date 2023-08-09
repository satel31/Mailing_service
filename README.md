## Django project "Сервис рассылок"
Проект, написанный на Python с использованием Django.

# Description
Сервис рассылок, позволяющий автоматически отправлять e-mail сообщения заданному списку пользователей.

# Запуск проекта:
1. Создайте файл .env по образцу в файле .env.sample
2. Установите зависимости проекта, указанные в файле pyproject.toml
3. Установите redis (ссылка на пакет: https://github.com/microsoftarchive/redis/releases)
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. Выполните миграции
6. При необходимости загрузите тестовые данные с помощью фикстуры или же внесите свои собственные данные.
7. Для создания superuser выполните команду csu
    ```bash
   python manage.py csu
   ```
8. Для запуска рассылок необходимо выполнить команду schedule (настройки находятся в файле schedule по пути
   apps/mailings/management/commands)
    ```bash
   python manage.py schedule
   ```
    
