# Django-ORM-standalone

Программма показывает активные карты доступа, список пользователей в хранилище и визиты в хранилище каждого пользователя. Программа берёт данные из базы данных и создаёт сайт.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте .env файл с содержимым
```
DATABASE_URL=
ALLOWED_HOSTS=
DEBUG=
SECRET_KEY=
```
и вставьте чувствительные данные и настройки сайта. В DATABASE_URL вставьте url вида `postgres://USER:PASSWORD@HOST:PORT/NAME`, где `USER`, `PASSWORD`, `HOST`, `PORT`, `NAME` - ваши данные 

### Пример запуска

```
python manage.py runserver
```
