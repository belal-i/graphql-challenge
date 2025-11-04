#!/bin/bash

docker exec  -ti graphql-challenge-backend-1 python manage.py loaddata users/fixtures/users.json
docker exec  -ti graphql-challenge-backend-1 python manage.py loaddata deployed_apps/fixtures/apps.json
