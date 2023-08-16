start_db_locally:
	docker-compose run -d -p 5432:5432 db

stop_db:
	docker-compose down