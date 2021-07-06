# Wedding Memories

This applications is a friend's request, who wanted a social network to keep his wedding memories through photos shared by all their loved friends as their guests.

This way he and his wife can keep their memories from an important moment in their lives through differents point of view.

But all phots must be approved by him or his wife.


# Technical specifications

This is an web application developed with Django framework.


The dependencies manager used on this project is [Poetry](https://python-poetry.org/). It's suggested to install the projects dependencies using it, this way you can run the E2E tests.

It's provided a requirements.txt with all the main dependencies, but this way you won't be able to run the project tests.

It was developed with Python 3.9.5.

And is required at least Python on version 3.9.

For the tests the chosen framework is [Behave](https://pypi.org/project/behave/) supported by [Selenium](https://pypi.org/project/selenium/) and [Expects](https://pypi.org/project/expects/) to a more readable assertion.

For a development environment the database used is sqlite, in a production environment Postgres.


# How to run

All the instructions to run is assuming that you have Poetry installed and you are on the root directory.

On the root directory run this command to install all the projects dependencies:
```
poetry install
```

After the installation run this command to activate a virtual environment where the projects dependencies were installed on the above instruction.
```
poetry shell
```

Copy the environment variables sample with the following command:
```
cp env-sample .env
```

With the virtual environment activated, run the following command to create the database for development environment:
```
./manage.py migrate
```

To run the application with the development server run:
```
./manage.py runserver
```

It will be started at **localhost:8000**.


To execute the End-to-End tests the application **MUST BE RUNNING ON LOCALHOST:8000**.

To run the tests run:
```
./manage.py behave tests/acceptance/features/ --use-existing-database
```

# Improvements
There are some point to be improved on this solution:
 - The upload should send the photo to a queue system to check the file metadata to guarantee the file is  a real picture and reduce the photo size;
 - E2E need some refactor to apply the PageObject design pattern to improve the tests maintenance;
 - The frontend for the application should be developed in a proper framework and considering UX;
 - Django Rest Framework can be added to move some views to API calls;
 - Unit tests on application;
 - Add Docker and Docker-compose to improve environment setup;
