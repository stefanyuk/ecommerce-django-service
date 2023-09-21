# Ecommerce Service

TBD

## Technology Stack

### Runtime environment
- Docker (https://docs.docker.com/get-started/overview/)
- docker-compose for containers management and orchestration (https://docs.docker.com/compose/)
- Python ^3.10

### Third-party dependency management and build tool
- Poetry - dependency management and packaging tool (https://python-poetry.org/)

### Web/API framework
- REST API (https://docs.microsoft.com/uk-ua/azure/architecture/best-practices/api-design)
- DRF as API framework (https://www.django-rest-framework.org/)
- TBD: We need to create OpenAPI specification. (https://swagger.io/specification/)

### RDBMS
- Postgres 14

### Testing
- pytest test runner (https://docs.pytest.org/en/6.2.x/)

## How to start working on a ticket
We will be using the [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

All new features (tickets) must be developed in a separate branch. Use the following branch name template: `<ticket-id>-short-description-of-changes` e.g.: in case if I'm working on issue 34, and I'm going to add `/users` endpoint in scope of this ticket, I'm going to create a branch called `34-users-endpoint`.
After you have done all needed changes, push branch to Github and create a pull request (PR). All PRs must be pointed to the `main` branch. Assign your teammate as reviewer. Once you get an approve, proceed with the merge.
Please pay attention when pushing the branch. Since we don't have Github Team or Enterprise, branch rules are not enforced.

In order to start development you need:
1. Pick a ticket and assign it to yourself.
2. Make sure that you understand the task and acceptance criteria (never start a task you do not understand, ask TL and PO to clarify it during grooming).
3. Create a feature branch in the format `<ticket-id>-<short-feature-description>` e.g.: `git checkout -b 42-the-ultimate-answer-to-everything`
4. Implement functionality and tests.
5. Run linter and formatter locally and fix all warnings and errors.
6. Run tests and make sure they are passing locally.
7. Make sure commit messages are descriptive.
8. Push your branch to Github e.g. `git push origin -u 42-the-ultimate-answer-to-everything`
9. Go to Gihub and create a pull request. Assign your teammate as reviewer.
10. Once you get approve, feel free to merge the PR, squash commits and delete branch from the Github.


### Local dev env

Pre-requisites:
- Python 3.10
- Docker
- docker-compose


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
