FROM python:3.6.12

MAINTANER Your Name "serinahmad00@gmail.com"

COPY ./Flask-edited

WORKDIR /dock

RUN python3 -m pip install -r requirements.txt

COPY . /dock

EXPOSE 5000/tcp
EXPOSE 5000/udp

CMD [ "main.py" ]
