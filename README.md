# Django Polls Application

This is a web-based application created using Django framework that allows users to view and vote in polls.

## Features

1. Users can view the list of polls.
2. Users can vote in each poll.
3. Users can view the results of each poll.
4. The application has an admin panel that allows managing (create, update, delete) the polls.

## Technology

1. Python 3
2. Django Framework
3. MySQL Database

## Installation

Before you start, make sure you have Python and pip installed on your machine.

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/yourrepository.git
Navigate to the project directory:

bash
Copy code
cd yourrepository
Install the required modules:

bash
Copy code
pip install -r requirements.txt
Running the Application
To start the application, navigate to the project directory and run:

bash
Copy code
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

Navigate to http://127.0.0.1:8000/polls to use the application.

## Installing Python dependencies

1. This project uses pip to manage Python dependencies.
2. Navigate to the base directory of the project, the same location as the `requirements.txt` file.
3. Run `pip install -r requirements.txt` to install all Python dependencies.

   The `requirements.txt` file includes `mysqlclient`, which is the MySQL client library that Django uses to interact with the MySQL database. It was installed with the command `pip install mysqlclient`.

   Note: `<version>` should be replaced with the version of `mysqlclient` you're using. If you're unsure, running `pip show mysqlclient` in your terminal will display information about your installed `mysqlclient` package, including the version.

Enjoy the app!
```
