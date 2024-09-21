run:
	cd solucoesweb && python manage.py runserver
migrate:
	cd solucoesweb && python manage.py makemigrations
	cd solucoesweb && python manage.py migrate
