#!/bin/bash
docker-compose -p blockchain down
docker volume prune --force
docker network prune --force
