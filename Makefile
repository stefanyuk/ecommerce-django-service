start_db_locally:
	docker-compose run -d -p 5432:5432 db

stop_db:
	docker-compose down

run_server:
	python manage.py runserver

setup_test_data:
	docker-compose down -v && docker-compose up -d --build && sleep 2 && docker exec -it ecommerce_django_service_backend_app_1 poetry run python manage.py setup_test_data
