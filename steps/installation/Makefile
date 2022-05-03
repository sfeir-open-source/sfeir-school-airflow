.DEFAULT_GOAL := help

.PHONY: help
help: ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: ## Initialize the system
	@mkdir -p ./dags ./logs ./plugins
	@echo -e "AIRFLOW_UID=$(shell id -u)" > .env
	@python init.py
	@docker-compose up airflow-init

.PHONY: airflow-start
airflow-start: init ## Run Airflow
	@docker-compose up

.PHONY: cleanup
cleanup: ## Clean-up the environment
	@docker-compose down --volumes --rmi all
	@rm -rf ./dags ./logs ./plugins .env

.PHONY: all
all: cleanup init airflow-start ## Clean and start environment
