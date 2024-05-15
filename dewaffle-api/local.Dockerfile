FROM python

RUN pip install poetry

WORKDIR /src

COPY ./pyproject.toml /src/pyproject.toml
COPY ./app /src/app

RUN poetry install

EXPOSE 8000
CMD ["poetry", "run", "start_docker"]
