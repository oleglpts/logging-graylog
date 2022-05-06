#!/bin/bash

docker build -t logging_graylog:latest ../main && docker run -d --name logging_graylog logging_graylog:latest
