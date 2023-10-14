FROM python:3.10-slim as requirements-stage

WORKDIR /tmp

RUN pip install --upgrade pip &&\
    pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10-slim

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src

CMD ["uvicorn", "src.main:backend_app", "--reload", "--host", "0.0.0.0", "--port", "8000"]