#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = perfil_de_cliente_ideal
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = py

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Instala as dependências Python
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Instala as dependencias Python, inclusives as de dev
.PHONY: requirements_dev
requirements_dev: requirements
	$(PYTHON_INTERPRETER) -m pip install -r requirements_dev.txt


## Deleta os arquivos compilados do Python
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff format --check
	ruff check

## Format source code with ruff
.PHONY: format
format:
	ruff check --fix
	ruff format

## Cria ambiente virtual com venv
.PHONY: create_environment
create_environment:
	$(PYTHON_INTERPRETER) -m venv .venv
	@echo ">>> Ambiente virtual criado em .venv"
	@echo ">>> Ative com:"
	@echo "    - Windows: .venv\\Scripts\\activate"
	@echo "    - Linux/Mac: source .venv/bin/activate"

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################


## Treino do modelo
.PHONY: train
train:
	$(PYTHON_INTERPRETER) run.py cmd_train

## Predição com entrada obrigatória e saída opcional
.PHONY: predict
predict:
	@$(if $(strip $(INPUT)),,$(error ERRO: informe o arquivo de entrada com INPUT=<caminho>))
	$(PYTHON_INTERPRETER) run.py cmd_predict -pti $(INPUT) $(if $(strip $(OUTPUT)),-o $(OUTPUT),)


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
