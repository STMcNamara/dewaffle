FROM python

RUN pip install poetry

WORKDIR /src

COPY ./pyproject.toml /src/pyproject.toml
COPY ./app /src/app

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["app.main.handler"]