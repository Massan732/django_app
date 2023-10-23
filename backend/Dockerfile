FROM python:3.9

WORKDIR /app/backend/

COPY ./backend/pyproject.toml ./backend/poetry.lock /app/backend/

RUN POETRY_HOME=/opt/poetry

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH

RUN poetry install --no-root 