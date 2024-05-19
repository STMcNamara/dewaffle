# Overview
This folder contains all backend code for the Dewaffle API.

# Installation
## Prerequisites
* Python
* poetry

 (Refer to pyroject.toml for version constraints.

## Dependencies
Install required python packages by running the following command in the same location as pyproject.toml:

> poetry install

# Run
## Local
To **manually** start the API, set the working directory to:
> "/dewaffle-api/dewaffle-api"

Activate the environment:
> "poetry shell"

Launch  web server with default local host settings
> "uvicorn main:app --reload"

Alternatively, use the **poetry script**:

Set the working directory to:
> "/dewaffle-api/"

Run the script:
> "poetry run start"

## With Docker
Prerequisite - Install Docker.

In 
> ./dewaffle-api

First build the image with (changing names and tags as required)
> docker build . -f local.Dockerfile -t dewaffle-api:v0

Run the container with:

> docker run -p 8000:8000 dewaffle-api:v0 

The API will be available on localhost:8000.

# Test
Testing is implements using Pytest.
## Local
To **manually** run all tests, set the working directory to:
> "/dewaffle-api"

Activate the environment:
> "poetry shell"

Run all tests with the command:
> "pytest"

Alternatively use the **poetry script**:
> "poetry run pytest"
