<p align="center">
    <a href="https://github.com/nickatnight/fastapi-backend-base/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/fastapi-backend-base/actions/workflows/main.yml/badge.svg">
    </a>
</p>


# fastapi-backend-base

Small base project to build and deploy a fastapi backend..batteries included.

## Features
* **Docker Compose** integration and optimization for local development.
* **Production ready** Python web server using Uvicorn
* Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> backend:
    * **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
    * **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
    * **Easy**: Designed to be easy to use and learn. Less time reading docs.
    * **Short**: Minimize code duplication. Multiple features from each parameter declaration.
    * **Robust**: Get production-ready code. With automatic interactive documentation.
    * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
    * <a href="https://fastapi.tiangolo.com/features/" class="external-link" target="_blank">**Many other features**</a> including automatic validation, serialization, interactive documentation, authentication with OAuth2 JWT tokens, etc.
* **SQLAlchemy** models
* **CORS** (Cross Origin Resource Sharing).
* **NGINX** High Performance Load Balancer, Web Server, & Reverse Proxy
* **Let's Encrypt** A free, automated, and open certificate authority (CA), provided by the Internet Security Research Group (ISRG)...with automatic cert renewal.
* **MongoDB** General purpose, document-based, distributed database built for modern application developers.
* **Motor** Coroutine-based API for non-blocking access to MongoDB
* Request rate limiting for api routes.


## Usage
1. `git clone https://github.com/nickatnight/fastapi-backend-base.git`
2. `cd fastapi-backend-base`
3. `mv .env_example .env`
4. `docker compose up --build`
5. visit `http://localhost:8000` for uvicorn server, or `http://localhost` for nginx

## Deploy
