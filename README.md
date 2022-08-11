# Starlite API

Example API using Starlite with SQLAlchemy and [SQLAlchemy-Mixins](https://github.com/absent1706/sqlalchemy-mixins)

## Quickstart

1. Install dependencies

    ```
    pip install -r requirements.txt
    ```

1. Set environment variables

    ```
    DATABASE_URL=sqlite:///db.sqlite3
    ```

1. Initialize database

    ```
    alembic -c alembic/alembic.ini revision --autogenerate
    alembic -c alembic/alembic.ini upgrade head
    ```

1. Run

    ```
    uvicorn api:app --host localhost --port 80 --reload
    ```

1. Interactive Swagger UI

    http://localhost/swagger
