# Checklist

Flask web app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.6, Flask, SQLAlchemy, SQLite

### How to create database ? 

Command line:

```
sqlite3 database_name.db
sqlite> .tables
sqlite> .exit
python3
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Start flask app

```
python3 app.py
```


