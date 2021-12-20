FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install poetry --no-cache-dir && poetry config virtualenvs.create false
RUN pip install poetry
COPY poetry.lock pyproject.toml ./

# RUN poetry build

COPY ./items_service /app/
RUN poetry install --no-interaction

EXPOSE 8080

CMD ["uvicorn","app:app", "--reload"]


