# Description

Реализация системы API для комментариев блога. Методы API
обеспечивают:
* Добавление статьи
* Добавление комментария к статье
* Добавление коментария в ответ на другой комментарий (возможна любая вложенность)
* Получение всех комментариев к статье вплоть до 3 уровня вложенности.
* Получение всех вложенных комментариев для комментария по его id.

# Installation

Clone repo from Github:

`git clone https://github.com/smolin8033/strategia_t.git`

Create and activate a new virtualenv for the project:

`virtualenv new_env`

Linux/MacOS:

`source new_env/bin/activate`

Windows:

`.\new_env\Scripts\activate`

Install all the dependencies from requirements.txt:

`pip install -r requirements.txt`

Go to the folder, where you see the file 'manage.py'.
Autocreate SQLlite database by running:

```
python manage.py makemigrations
python manage.py migrate
```

To start the server type:

`python manage.py runserver`

Now you can check API's swagger documentation
and test all endpoints at:

`localhost:8000/swagger/`