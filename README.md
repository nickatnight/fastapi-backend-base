# fastapi-backend-base

Small base project to build and deploy a fastapi backend..batteries included.

## Services
* high performance [FastAPI](https://fastapi.tiangolo.com/) backend
* asynchronous access to key/value [database](https://motor.readthedocs.io/en/stable/)
* [nginx](https://www.nginx.com/blog/lets-encrypt-tls-nginx/) webserver/proxy with automatic ssl cert renewal

## Usage
1. `git clone https://github.com/nickatnight/fastapi-backend-base.git`
2. `cd fastapi-backend-base`
3. `mv .env_example .env`
4. `docker compose up --build`
5. visit `http://localhost:8000` for uvicorn server, or `http://localhost` for nginx

## Deploy
