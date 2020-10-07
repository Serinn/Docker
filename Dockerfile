FROM ubuntu:18.04

MAINTANER Your Name "serinahmad00@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /dock

RUN pip install -r requirements.txt

COPY . /dock

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]