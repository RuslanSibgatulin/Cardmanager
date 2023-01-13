## ----------------------------------------------------------------------
## Makefile is to manage Cardman project.
## ----------------------------------------------------------------------
include docker/envs/Cardman.env
export

compose_files=-f docker-compose.yml

help:     ## Show this help.
		@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

start:  ## Start project
		cd docker && DOCKER_BUILDKIT=1 docker-compose $(compose_files) up -d --build --force-recreate

stop:
		cd docker && DOCKER_BUILDKIT=1 docker-compose $(compose_files) down

init:  ## First and full initialization. Create database, superuser and collect static files
		docker exec -it app_django bash -c \
		'python manage.py migrate && python manage.py createsuperuser --noinput && python manage.py collectstatic --noinput'

static:  ## Install bootstrap-5.0.2 css library
		wget -q https://github.com/twbs/bootstrap/releases/download/v5.0.2/bootstrap-5.0.2-dist.zip -O /tmp/bootstrap-5.0.2.zip
		unzip -j -o /tmp/bootstrap-5.0.2.zip bootstrap-5.0.2-dist/css/bootstrap.min.css -d /tmp
		docker exec -it app_django bash -c 'mkdir /usr/src/app/static/css/'
		docker cp /tmp/bootstrap.min.css app_django:/usr/src/app/static/css/

runserver:  # Override prod variables
		DJANGO_DEBUG=True
runserver:  # Start dev server
		cd app && python manage.py runserver --settings=cardman.settings.settings_local

shell:  ## Open django shell
		cd app && python manage.py shell --settings=cardman.settings.settings_local

migrate:  ## Apply models changes
		cd app && python manage.py makemigrations && python manage.py migrate


lint-install:  ## Install linters
		pip install lxml mypy wemake-python-styleguide flake8-html types-python-dateutil

lint:  ## Check code with linters
		isort app/
		flake8 app/ --show-source
		mypy app/ --ignore-missing-imports --no-strict-optional --exclude /migrations/ --exclude /tests/ --disable-error-code=attr-defined
