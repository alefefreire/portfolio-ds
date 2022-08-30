# Business Problem

Book Club is a book exchange Startup. The business model works based on the exchange of books by users, each book registered by the user gives the right to exchange, but the user can also buy the book, if he does not offer another book in exchange.

One of the most important tools for this rental business to enable is a business model. An excellent offer and sales volume exchange on the site.

You are a Data Scientist contracted by the company to build a Recommender System that drives the volume of exchanges and sales among users. However, Book Club does not collect or store the books submitted by users.

The books themselves for exchange are sent by users through an “Upload” button, they are not visible on the site, along with their stars, which represent how much users liked or disliked the book, but Startup does not collect or store this data in a database.

So, before building a recommender system, you need to collect and store website data. So your first job as a Data Scientist will be to collect and store the following data:

* The name of the book.
* The book category.
* The number of stars the book received.
* The price of the book.
* Whether the book is in Stock or not.

# Tecnology Stack
Below, the list of techonologies used in this project:

* Python
* Pyenv
* Poetry
* tox
* Beautiful Soup
* Airflow
* PostgreSQL
* Docker

## Brief Description
The primary programming language used to solve this problem is [Python](https://www.python.org/). The latter is used to write down the web scraping logic, using the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library, and also to write the data pipelines, which are orchestrated using [Airflow](https://airflow.apache.org/).  We use [Pyenv](https://github.com/pyenv/pyenv) to create a virtual environment where python versions can be managed and [Poetry](https://python-poetry.org/) as a package manager to handle the project's dependencies.

The ETL process runs on top of Airflow, and all data collected is saved in the [PostgreSQL](https://www.postgresql.org/) database. The ETL can be run locally using [Docker](https://www.docker.com/). If you want to check code formatting, linting, and unit tests all of these are executed via [tox](https://tox.wiki/en/latest/).

# Local Environment Setup
In order to build this project and install ist dependencies follow the instructions below:
1. Install `pyenv` and `pyenv-virtualenv` ([here](https://github.com/pyenv/pyenv#installation) you can find some guidance for installation and how to configure your shell's environment for `pyenv` and [here](https://github.com/pyenv/pyenv-virtualenv) for `pyenv-virtualenv`)

2. Install [poetry](https://python-poetry.org/docs/).

3. After cloning project's repo, navigate to `portfolio-ds/data-eng` and run the command
```
pyenv install 3.9.10
```
This will install Python 3.9.10. After that, to select the python version for this project, run the command:

```
pyenv local 3.9.10
```
You can check that this Python version was chosen by typing `python -V`. If the version that appears is different from 3.9.10, try to restart your terminal to see the changes.
4. In `portfolio-ds/data-eng` run
```
poetry install
```
The dependencies will be installed in the virtual environment previously created.

5. In your bashrc file , `~/.bashrc` or `~/.zshrc` (macOS users), add the following lines:
```
export PATH="$HOME/.pyenv/bin:$HOME/.poetry/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
and then run `source ~/.bashrc` to restart it.

6. After dependencies installation and virtualenv creation, just choose the Python interpreter that Poetry just created. If you are in VS code use the **Python: Select Interpreter command** from the **Command Palette** (⇧⌘P). In PyCharm, you can switch your Python interpreter either using the **Python Interpreter** selector or in the project **Settings/Preferences** (more details can be found [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)).

## Usage

After the local environment setup completion, you can navigate to `portfolio-ds/data-eng` and run `poetry shell` to activate the virtual environment. After that, if you want to run unit tests and check linting, navigate to `portfolio-ds/data-eng` and run `tox`.

# Running the ETL
After dependencies are installed, in order to run the ETL pipeline, navigate to `portfolio-ds/data-eng` and run

```
docker-compose up
```
This will build the Airflow image (make sure that you have Docker installed), including all its services: webserver, scheduler, triggered, and the PostgreSQL database where the data will be stored.  After the Airflow image building completion, you can access the web server UI via [localhost](http://localhost:8080/). And you will be redirected to the Airflow login session:
![airflow](/docs/airflow-login.png)

The username and password are `airflow`. After the login session, you will be redirected to the main Airflow session where you can find the DAGs. In the Admin tab access the `Connections` section where you can insert the `PostgreSQL` database connection info.
![postgresql](/docs/connection-config.png)

Below you can find some guidance on how to fill in the information for the database connection

* **Connection Id**: `postgres_default`
* **Connection Type**: `Postgres`
* **Host**: `data-eng-postgres-1`
* **Login**: `airflow`
* **Password**: `airflow`
* **Port**: `5432`

After edit connection just click on `Save` button and the connection to the PostgreSQL database will be granted.

You can navigate back to the main Airflow session just clicking by on `DAGs` tab at the top. The `scrapy_book` DAG will be available and scheduled to run on a daily basis.