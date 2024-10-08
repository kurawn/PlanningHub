## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/kurawn/PlanningHub.git
$ cd PlanningHub
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
## Accessing the Admin Panel

To access the Django admin panel, follow these steps:
1. Navigate to the Django admin panel in your browser:
http://127.0.0.1:8000/admin/
2. Log in using the admin credentials: Username: admin; Password: admin
