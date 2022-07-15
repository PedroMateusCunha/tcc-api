FROM nginx:1.15.8

ARG APP_NAME
ARG ENV_NAME
LABEL app=${APP_NAME}

RUN rm /etc/nginx/nginx.conf && \
    rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/
COPY project.conf /etc/nginx/conf.d/

EXPOSE 80