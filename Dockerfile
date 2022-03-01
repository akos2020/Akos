FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code

# Start the development server
RUN pip install -U pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt


