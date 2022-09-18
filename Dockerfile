FROM python:3.10.7-slim

# python specific
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /app/
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN poetry install
RUN poetry add gunicorn psycopg2-binary

# Copies all in the new docker container
COPY . .

RUN mkdir /data
# symbolic link (-fs = -f -s, in case file already exists)
RUN ln -fs /data/settings_local.py bundeswehrbung/settings_local.py

# program, start, with gunicorn, name, port, worker number 6 max
CMD ["poetry", "run", "gunicorn", "bundeswehrbung.wsgi", "-b", "0.0.0.0:8000", "-w", "6"]