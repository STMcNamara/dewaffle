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
To start the API, set the working directory to:

> "/dewaffle-api/dewaffle-api"

Activate the environment:

> "poetry shell"

Launch  web server with default local host settings

> "uvicorn main:app --reload"