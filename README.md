# Quickstart

To clone and run this application you will need Docker, Docker-Compose and Git to be installed on you computer.
Also there are a set of handy 'make' commands, which can help you to run app quicker.
From your command line:

```
- git clone git@github.com:stefanyuk/ecommerce-django-service.git
- cd ecommerce-django-service
```

Create file with environment variables. The name must be the same as in the command below: 
```
- touch .env
```

Add to the file variables specified in the '.env.dist' template.


Run application in Docker:

```
- docker-compose up -d --build
```

Generate test data:

```
- make setup_test_data
```

Now you can open the following url http://127.0.0.1:8000/admin and login to the application admin with following credentials:

- username: admin
- password: 1234
