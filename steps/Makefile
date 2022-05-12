.DEFAULT_GOAL := help
INSTALLATION_PATH=00-installation
DOCKER_COMPOSE_PATH=$(INSTALLATION_PATH)/docker-compose.yaml

.PHONY: help
help: ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: ## Initialize the system
	@mkdir -p ./dags ./$(INSTALLATION_PATH)/logs ./$(INSTALLATION_PATH)/plugins
	@echo -e "AIRFLOW_UID=$(shell id -u)" > .env
	@cd $(INSTALLATION_PATH) && python init.py
	@docker-compose -f $(DOCKER_COMPOSE_PATH) up airflow-init

.PHONY: airflow-start
airflow-start: ## Run Airflow
	@docker-compose -f $(DOCKER_COMPOSE_PATH) up

.PHONY: airflow-stop
airflow-stop: ## Stop airflow
	@docker-compose -f $(DOCKER_COMPOSE_PATH) down

.PHONY: cleanup
cleanup: ## Clean-up the environment
	@docker-compose -f $(DOCKER_COMPOSE_PATH) down --volumes --rmi all
	@rm -rf ./dags ./$(INSTALLATION_PATH)/logs ./$(INSTALLATION_PATH)/plugins .env

.PHONY: all
all: cleanup init airflow-start ## Clean and start environment
