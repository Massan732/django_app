# ベースイメージの指定
FROM python:3.10

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリの設定
WORKDIR /app/backend

# poetryの準備
RUN pip install poetry
RUN poetry config virtualenvs.in-project false

# poetryによるパッケージインストール
COPY ./backend/pyproject.toml /app/backend/
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi
