# Quickbutik

This is a Django web application that retrieves data from Quickbutik API and presents a basic dashboard view of the recent orders and a graph of the top 3 most sold products.

## Technologies 

The following technologies were used in this project:

- [HTML](https://html.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [JavaScript](https://www.javascript.com)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Quickbutik API](https://speca.io/abqb/quickbutik-api-global#get-orders)
- [Chart.js](https://www.chartjs.org/)
- [SQLite3](https://www.sqlite.org/index.html)


## Requirements

Before starting, you need to have [Python 3](https://www.python.org/) installed.

Kindly ensure that you are in the root directory before running the following commands.


## Create virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Start server
    python manage.py runserver

## visit Homepage
    http://127.0.0.1:8000

### To fetch orders from Quickbutik API
    python manage.py shell < utils/fetch_orders.py