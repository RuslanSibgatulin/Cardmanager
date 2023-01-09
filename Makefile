## ----------------------------------------------------------------------
## Makefile is to manage Cardman project.
## ----------------------------------------------------------------------
include docker/envs/Cardman-dev.env
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

static:
		wget -q https://github.com/twbs/bootstrap/releases/download/v5.0.2/bootstrap-5.0.2-dist.zip -O /tmp/bootstrap-5.0.2.zip
		unzip -j -o /tmp/bootstrap-5.0.2.zip **/css/bootstrap.min.css -d /tmp/static/css
		docker exec -it app_django bash -c 'mkdir /usr/src/app/static/css/'
		docker cp /tmp/static/css/bootstrap.min.css app_django:/usr/src/app/static/css/

runserver:
		cd app && python manage.py runserver --settings=cardman.settings.settings_local

shell:
		cd app && python manage.py shell

migrate:
		cd app && python manage.py makemigrations && python manage.py migrate


lint-install:
		pip install lxml mypy wemake-python-styleguide flake8-html types-python-dateutil

lint:
		isort app/
		flake8 app/ --show-source
		mypy app/ --ignore-missing-imports --no-strict-optional --exclude /migrations/ --exclude /tests/ --disable-error-code=attr-defined
