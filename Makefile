start_db_locally:
	docker-compose run -d -p 5432:5432 db

stop_db:
	docker-compose down

setup_test_data:
	docker-compose down -v && docker-compose run -d -p 5432:5432 db && sleep 2 && python manage.py setup_test_data