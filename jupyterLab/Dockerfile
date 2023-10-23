FROM python:3.9

WORKDIR /app/jupyterLab/

COPY ./jupyterLab/pyproject.toml ./jupyterLab/poetry.lock /app/jupyterLab/

RUN POETRY_HOME=/opt/poetry

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH

RUN poetry install --no-root --no-dev