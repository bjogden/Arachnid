# Arachnid

## What
Dockerized Python scraper using Selenium with Firefox web driver.

## Why
Simply using Python's [requests](https://docs.python-requests.org/) library will not allow for JavaScript execution on a web page. Selenium takes web automation a step further by loading a full (headless) web browser to allow for JavaScript execution.

## How
- Docker
- Python 3.9
    - Jupyter Notebook
- Selenium
    - Firefox

### Local Development

1. `docker-compose up`
2. Navigate to [http://localhost:8888](http://localhost:8888) to open Jupyter Notebook UI to create new Python notebook
3. Import Selenium, and get started