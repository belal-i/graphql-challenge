### About

A simple GraphQL backend implemented with Django, which allows users
to be owners of apps, and lets them upgrade and downgrade between
a "hobby" and a "pro" plan.

### Installing/running

* Clone the repository, `cd` into it, and run:
  ```
  docker compose up --build --detach
  ```

* Load the fixtures:
  ```
  docker exec  -ti graphql-challenge-backend-1 python manage.py loaddata users/fixtures/users.json
  docker exec  -ti graphql-challenge-backend-1 python manage.py loaddata deployed_apps/fixtures/apps.json
  ```

* Browse to http://localhost:8000/graphql

* Run some test queries:
  ```
  {
    users {
      id
      username
      plan
      apps {
        id
        active
      }
    }
  }
  ```

  ```
  mutation {
    upgradeAccount(id: 1) {
      user {
        id
        username
        plan
      }
    }
  }
  ```

#### Alternative: without Docker

* ```
  python -m venv .venv
  ```
* ```
  . .venv/bin/activate
  ```
* ```
  python -m pip install -r requirements.txt
  ```
* ```
  python manage.py migrate
  ```
* ```
  python manage.py loaddata users/fixtures/users.json
  ```
* ```
  python manage.py loaddata deployed_apps/fixtures/apps.json
  ```
* ```
  python manage.py runserver
  ```
* Run the same queries as above.
