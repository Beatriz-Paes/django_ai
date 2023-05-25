# 🐾 Django AI

Django AI is a web application that uses Python, Django and connects to OpenAI, creator of ChatGPT, thus being able to
send code snippets for correction, instructions for creating code, and requesting general topic questions. The project
is the result of a [course](https://www.udemy.com/course/curso-de-django-com-openai-chatgpt/) taught
by [Davi Werner](https://www.linkedin.com/in/dwl), but with adaptations and has the following features:

- Submit your codes for the AI to suggest corrections;

- Send instructions to the AI to create source code;

- Choose from several different languages;

- Save interactions with the AI. in the database;

- View and delete history of interactions with the AI;

- User authentication and access control;

- Registration of new users.

## 🚀 Starting

These instructions will allow you to get a working copy of the project on your local machine for
development and testing.

### 📋 Requirements

You will need [python](https://www.python.org) installed on your machine. Being at the root of the project, run the
next steps via your terminal.

Create a virtual environment with the command:

```
python -m venv venv
```

Now, to activate the created venv:

```
source venv/bin/activate
```

### 🔧 Installation

With the virtual environment activated, let's install the dependencies.
To install all of the Python modules and packages listed in requirements.txt file, use:

```
pip install -r requirements.txt
```

To use the application, you need a key which is obtained from the
website [OpenAi](https://platform.openai.com/account/api-keys), create an account and generate the key for free.
With the call in hand, you can clone the env.credentials file, rename it to .env and add your key to the variable
OPENAI_KEY.


Creating the migrations in the database:

```
python manage.py migrate
```

And finally putting the application to run:

```
python manage.py runserver
```

If all goes well, you can access the links below:

| Page         | Address                                                              | Authenticated |
|:-------------|:---------------------------------------------------------------------|:--------------|
| Login        | [http://127.0.0.1:8000/signin](http://127.0.0.1:8000/signin)         | No            |
| Signup       | [http://127.0.0.1:8000/signup](http://127.0.0.1:8000/signup)         | No            |
| Correction   | [http://127.0.0.1:8000/correction](http://127.0.0.1:8000/correction) | Yes (Django)  |
| Creation     | [http://127.0.0.1:8000/creation](http://127.0.0.1:8000/creation)     | Yes (Django)  |
| General      | [http://127.0.0.1:8000/general](http://127.0.0.1:8000/general)       | Yes (Django)  |
| Historic     | [http://127.0.0.1:8000/historic](http://127.0.0.1:8000/historic)     | Yes (Django)  |
| Django Admin | [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)           | Yes (Django)  |

## 🖼️ Visualization

How you should see it in your browser:
![django_ia](https://github.com/Beatriz-Paes/django_ai/assets/59239202/69e1afa2-9dcb-45d7-b6ae-cb078906bdd9)

## 🛠️ Built with

This project was the result of a course taught by Davi Werner. Below are some useful links used in the
development:

* [Udemy course](https://www.udemy.com/course/curso-de-django-com-openai-chatgpt/) - Django course with
  OpenAI/ChatGPT
* [OpenAi](https://openai.com/)
* [Python](https://www.python.org/)
* [Bootstrap](https://getbootstrap.com/)
* [Django](https://www.djangoproject.com/)

## 🎁 Additional Information

* Project still under development with predictions of improvements 📢;
* Feel free to collaborate or call for a beer 🍺;

---
⌨️ with ❤️ by [Beatriz Paes](https://github.com/beatriz-paes) 😊
