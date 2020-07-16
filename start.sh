#!/bin/bash
sudo docker-compose up -d
sudo watch -n 1 "docker inspect --format='{{json .State.Health.Status}}' python-application && docker inspect --format='{{json .State.Status}}' python-application"
