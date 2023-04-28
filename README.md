# Проект - Телеграм-бот с доступом к данным в БД
От любой базы данных нет никакого толку, если она не используется в каком-то сервисе. Чаще всего в роли сервиса выступает какое-либо веб-приложение. При этом веб-приложение - это необязательно сайт. Им может быть любая связка "интерфейс пользователя" - "сервер", например, приложение для смартфона или телеграм-бот. В этом задании мы научимся создавать телеграм-ботов, которые будут подключаться к нашей базе данных.

# Постановка задачи
Наш проект можно разделить на 4 большие части:

1. Сервер, который будет размещать ссылки на файлы со статистикой
2. Модуль для доступа к БД: описание моделей данных и api взаимодействия с этими моделями
3. Модуль взаимодействия с Телеграмом
4. Сама база данных.

# Архитектура проекта будет следующей. Структура файлов:

bot
- __init__.py
- app.py
- telegram.py
- database
   - __init__.py
   - dbapi.py
   - models.py

Таким образом, наш проект будет включать три независимых модуля. Модуль сервера и модуль телеграма будут использовать функционал модуля БД в своем коде, поэтому договоритесь о протоколе взаимодействия этих модулей заранее.

# Какой бот будем писать?
Напишем бот для обмена книгами. Он должен будет иметь следующий функционал:

- добавление книги в общую библиотеку
- взятие книги из библиотеки для чтения
- возвращение книги в библиотеку после чтения
- удаление книги из библиотеки (например, из-за износа)
- формирование файла со статистикой использования книги и отправление 
- ссылки на скачивание этого файла
