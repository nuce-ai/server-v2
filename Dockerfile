# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8.2

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev && \
    apt-get install -y libgl1-mesa-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]
