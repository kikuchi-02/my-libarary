FROM python:3.7

COPY . /main
WORKDIR /main

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --dev
