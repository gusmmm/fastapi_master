# Project objectives
- Implement a FastAPI application with CRUD operations for sqlite3 local database with patient medical data
- Use Pydantic models for request validation and response serialization.
- Write unit tests for the API endpoints using FastAPI's TestClient.

## how to manage python dependencies and manage the project
- use poetry to manage dependencies and virtual environments.
- add dependencies using `poetry add <package_name>`.
- install all dependencies using `poetry install`.
- use the taskipy tasks to run and automate common tasks.
- the tests/ directory contains all the test files for the project. Use taskipy and pytest to run the tests.

## local sqlite3 database
- use a local sqlite3 database to store patient medical data.
- create a database file (`database.db`) in the project directory.
- use SQLAlchemy to interact with the database and define the data models.