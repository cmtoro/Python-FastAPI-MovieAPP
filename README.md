
# Python-FastAPI-MovieAPP

Python app created with FastAPI and MongoDB to define an API and expose CRUD REST services and a simple jwt based authentication method.

## Config
Docker MongoDB
```bash
docker run -p 27017:27017 --name some-mongo -d mongo:latest
```
No further config needed.
## Clone repository
```bash
git clone https://github.com/cmtoro/Python-FastAPI-MovieAPP.git
```
## Python virtual environments (Mac)
```bash
pip install virtualenv
virtualenv -p python3 my-movie-api
cd my-movie-api
source bin/activate
```
## Install Python dependencies
```bash
pip3 install -r requirements.txt
```
* pip version: 22.3.1
* python version: 3.11.2
## Run application
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```
