FROM python:3.10.7-slim

# python specific
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /app/
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN poetry install

# Copies all in the new docker container
COPY . .

CMD ["poetry", "run", "./manage.py", "runserver", "0.0.0.0:8000"]