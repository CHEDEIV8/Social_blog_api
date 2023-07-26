Social_blog_api
===============

Описание:
----
***Social_blog_api*** - это DRF для Yatube(социальная сеть). Позволяющая просматривать и создавать посты, 
просматривать группы, подписываться на авторов постов.

Как запустить проект:  
----
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:CHEDEIV8/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:  
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Обновляем версию pip:
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:  
```
python manage.py runserver
```
Примеры запросов к API:  
----
Получить список всех постов (GET):

    http://127.0.0.1:8000/api/v1/posts/

Получить определенный пост (GET):    

    http://127.0.0.1:8000/api/v1/posts/1/
Получить коментарии определенного поста (GET): 

    http://127.0.0.1:8000/api/v1/posts/1/comments/
Получить список всех групп (GET):  

    http://127.0.0.1:8000/api/v1/groups/
Создать новый пост(требуется аутентификация) (POST):

	http://127.0.0.1:8000/api/v1/posts/
Получить документацию по всем эндпойнтам API (GET):

	http://127.0.0.1:8000/redoc/
___

## Author: 


Denis Cherednisenko
___

