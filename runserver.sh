#!/bin/bash

docker-compose down --remove-orphans --rmi all -v


docker-compose build && docker-compose up -d && docker-compose logs -f

