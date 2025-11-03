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
  ./loaddata.sh
  ```

* Browse to http://localhost:8000/graphql

* Dealing with base64 encoding. Relay expects every Node id to be a base64 encoded string.
  Therefore, to get the base64 encoded ID strings of a user and app from our fixture data,
  do something like this:
  ```
  echo -n 'User:u_abc12345' | base64
  ```
  ```
  echo -n 'App:app_1234abcd' | base64
  ```
  Those examples will output `VXNlcjp1X2FiYzEyMzQ1` and `QXBwOmFwcF8xMjM0YWJjZA==`
  respectively, which we can use in the following queries.

* Run some test queries:
  ```
  query {
    node(id: "VXNlcjp1X2FiYzEyMzQ1") {
      ... on User {
        userId
        username
        plan
      }
    }
  }

  ```

  ```
  query getApp {
    node(id: "QXBwOmFwcF8xMjM0YWJjZA==") {
      ...on App {
        id
        active
      }
    }
  }
  
  ```

  ```
  mutation {
    upgradeAccount(id: "VXNlcjp1X2FiYzEyMzQ1") {
      ok
      user {
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
  cp .env.example .env # and configure as needed
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
