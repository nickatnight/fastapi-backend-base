all:

# docker
up:
	@echo "bringing up project...."
	docker compose up

down:
	@echo "bringing down project...."
	docker compose down

# alembic
alembic-scaffold:
	@echo "scaffolding migrations folder..."
	docker compose exec backend alembic init -t async migrations

alembic-init:
	@echo "initializing first migration...."
	docker compose exec backend alembic revision --autogenerate -m "init"

alembic-make-migrations:
	@echo "creating migration file...."
	docker compose exec backend alembic revision --autogenerate -m "add year"

alembic-migrate:
	@echo "applying migration...."
	docker compose exec backend alembic upgrade head

# lint
test:
	@echo "running pytest...."
	docker compose exec backend pytest --cov-report xml --cov=src tests/

flake8:
	@echo "running flake8...."
	docker compose exec backend flake8

black:
	@echo "running black...."
	docker compose exec backend black .

# misc
check: BREW-exists
BREW-exists: ; @which brew > /dev/null

hooks: check
	@echo "installing pre-commit hooks...."
	pre-commit install
