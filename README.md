# Backoffice App

## Backend

A generic backend for a backoffice app to manage some orders and products.

## Get started

### Build

```sh
docker compose build
```

### First run

```sh
docker compose up -d postgres
docker compose exec postgres psql -U postgres
```

```psql
CREATE USER backoffice WITH PASSWORD 'backoffice00';
CREATE DATABASE backoffice WITH OWNER backoffice;
\q
```

```sh
docker compose up -d
docker compose exec django ./manage.py migrate
docker compose exec django ./manage.py createsuperuser
```

### Run

```python
docker compose up [-d]
```
