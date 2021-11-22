POETRY_RUN = poetry run python

.PHONY: db
database db: docker-compose.yml
	docker-compose -f docker-compose.yml up

.PHONY: manage
manage:
	$(POETRY_RUN) manage.py $(filter-out $@,$(MAKECMDGOALS))

%:
	@ # a match-anything command
	@ # Used to suppress error when running "make manage"
	@: