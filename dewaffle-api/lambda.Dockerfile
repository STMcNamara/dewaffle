FROM public.ecr.aws/lambda/python:3.12

RUN pip install poetry

WORKDIR ${LAMBDA_TASK_ROOT}

COPY ./pyproject.toml ${LAMBDA_TASK_ROOT}
COPY ./app ${LAMBDA_TASK_ROOT}/app

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["app.main.handler"]