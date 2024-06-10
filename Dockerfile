FROM python:3.12
ADD . /end-to-end-project
WORKDIR /end-to-end-project
RUN pip install -r requirements.txt