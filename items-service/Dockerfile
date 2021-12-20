FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

RUN pip install poetry --no-cache-dir && poetry config virtualenvs.create false
RUN pip install poetry
COPY poetry.lock pyproject.toml ./

# RUN poetry build

COPY ./items_service /app/
RUN poetry install --no-interaction

EXPOSE 8080

CMD ["uvicorn","--host","0.0.0.0", "--port", "8000",  "app:app", "--reload"]


