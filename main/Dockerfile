FROM alpine:3.12.8

WORKDIR /app

# install python & pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip && pip3 install --no-cache --upgrade pip setuptools

# copy application
COPY . /app
RUN chmod 755 /app/main.py
CMD ["/app/main.py"]
