[![Build Status](https://travis-ci.org/Copyrighted/portfolio.svg?branch=master)](https://travis-ci.org/Copyrighted/portfolio)

# Flask Blog Site

Blog with authentication, authorization, and error handling. Allows users to create, update and delete posts.
Uses PyTest for unit testing. Uses Travis CI for automated testing. Deployed using Azure and Docker.

## Getting Started

### Prerequisites

Python 3.x

Docker

### Installing

Install Python 3.x

Select your favorite IDE (I use PyCharm so that is what I'll be doing the instructions in)

git clone https://github.com/Copyrighted/portfolio

Open project in preferred IDE

Set up Python Virtual Environment

To install requirements do pip install -r requirements.txt

## Manually running the tests

To run tests, use 

python -m pytest tests

If you want to run unit tests you could do

python -m pytest --setup-show tests/unit/

## Using Travis CI to run Tests

Connect your github account to Travis-CI.org

The .travis.yaml file will take care of the tests.

## Deployment

### Deployment on Azure

#### Get an Azure Subscription

#### Create a resource group in Azure

#### Create an Azure Container Registry
Enable admin rights in your ACR

#### Login to your Azure container registry

docker login <azure_container_registry_name>

#### Create a docker image using the Dockerfile

cd ~/path/to/portfolio/folder

docker build . -t blog:latest

#### Tag the image

docker tag blog <azure_container_registry_name>/blog

#### Push the image to your Azure Container Registry

docker push <azure_container_registry_name>/blog

#### Create web app in App Services in Azure

Select the docker option when creating the Application

#### You've deployed the application!


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Backend framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM Used
* [SQLite](https://sqlite.org/index.html) - Database used
* [Summernote](https://summernote.org/) - Markdown Editor used
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja2 used for templating
* [Bcrypt](http://bcrypt.sourceforge.net/) - Bcrypt used to salt/hash passwords
* [Docker](https://www.docker.com/) - Docker used to make images and quickly deploy application
* [Azure](https://azure.com) - Azure used to host container made from Docker Image

## Authors

* **Tyler Scheffler** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to hackersandslackers.com for in depth info on Flasks inner workings. [HackersandSlackers](https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/)

