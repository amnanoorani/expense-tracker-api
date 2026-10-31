# Expense Tracker REST API

## Description
A RESTful CRUD API built with FastAPI to manage financial expense records, migrating an existing command-line Python application into a web service backed by PostgreSQL.

## Tech Stack
Python, FastAPI, PostgreSQL, Pydantic, psycopg2, Uvicorn

## Features
- Full CRUD operations for expenses
- Aggregate summary endpoint (total and average)
- Monthly summary endpoint
- Request validation with Pydantic
- Parameterized SQL queries to prevent SQL injection
- Routes and handlers separated into different modules

## Project Structure
- `main.py`: API routes
- `handlers.py`: request handlers (business logic)
- `models.py`: Pydantic models
- `database.py`: PostgreSQL connection

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
3. Run the server: `uvicorn main:app --reload`
4. Open the docs at `http://127.0.0.1:8000/docs`

## Planned
- User accounts with authentication
- Expense categories
