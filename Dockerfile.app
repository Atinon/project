FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY ./exam_project ./exam_project
COPY ./requirements.txt .
COPY ./Dockerfile.app .
COPY ./docker-compose.yml .
COPY ./docker-entrypoint-app.sh .
COPY ./init.sql .

RUN pip install -r requirements.txt
RUN python ./exam_project/manage.py makemigrations

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint-app.sh"]
