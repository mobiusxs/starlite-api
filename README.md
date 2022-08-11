# Starlite API

Example API using Starlite with SQLAlchemy and [SQLAlchemy-Mixins](https://github.com/absent1706/sqlalchemy-mixins)

## Quickstart

1. Install dependencies

    ```
    python -m venv venv
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

## Docker

1. Build and run

```
docker build -t api .
docker run -d -p 80:5000 -e "DATABASE_URL=sqlite:///db.sqlite3" --name api api
```

1. Initialize database

```
docker exec -it api bash
alembic -c alembic/alembic.ini revision --autogenerate
alembic -c alembic/alembic.ini upgrade head
exit
```

1. Teardown

```
docker stop api
docker rm api
docker image rm api
```

## Docker Compose

1. Run

```
docker compose up -d
```

1. Initialize database

```
docker compose exec api bash
alembic -c alembic/alembic.ini revision --autogenerate
alembic -c alembic/alembic.ini upgrade head
exit
```

1. Teardown

```
docker compose down
docker image rm api
```

