FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY exam_project/ requirements.txt .
COPY docker-entrypoint-app.sh .

RUN pip install -r requirements.txt
RUN python manage.py makemigrations

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint-app.sh"]
