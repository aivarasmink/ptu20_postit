# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./ptu20_postit .
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
