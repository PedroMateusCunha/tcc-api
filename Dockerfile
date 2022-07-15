# STAGE 1: Create base image
FROM python:3.6 as base

ARG APP_NAME
ARG ENV_NAME
ARG USER_NAME=sakura
ARG USER_HOME=/usr/app
LABEL app=${APP_NAME}


RUN useradd --system --home $USER_HOME $USER_NAME && \
    mkdir -p $USER_HOME && \
    chown -R $USER_NAME:$USER_NAME $USER_HOME
WORKDIR $USER_HOME
COPY --chown=$USER_NAME:$USER_NAME app .

RUN python3 -m pip install --upgrade pip && \ 
    pip install -r ${USER_HOME}/requirements/base.txt

USER $USER_NAME

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "app:app", "--reload"]
