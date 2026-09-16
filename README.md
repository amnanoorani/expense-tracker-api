# Expense Tracker REST API

## Description
A RESTful CRUD API built with FastAPI to manage financial expense records, migrating an existing command-line Python application into a scalable, multi-client web service. Developed during my Backend Developer Internship at Eurus Technologies.

## Tech Stack
Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, psycopg2

## Features
- Full CRUD operations across multiple endpoints
- Custom analytics endpoints for monthly and aggregate expense summaries using PostgreSQL date-extraction functions
- Data integrity enforced through Pydantic schema validation (type checking, numeric constraints, malformed input rejection)
- Secure database practices using SQLAlchemy ORM and parameterized SQL queries via psycopg2 (SQL injection prevention)
- Layered architecture separating routing, request handlers, data models, and database access
- Structured error handling with appropriate HTTP status codes (400, 404, 422, 500)
- User registration/login, category-based expense organization, and JWT-based authentication for per-user data isolation
- Tested via Swagger UI and Postman

## Status
🚧 Code to be pushed soon

## Author
Amna Bibi
