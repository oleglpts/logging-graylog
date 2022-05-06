#!/bin/bash

eval $(minikube docker-env -p gray)
docker build -t logging_graylog:latest ../main
