# Установка poetry
install:
	poetry install

# Сборка
build:
	poetry build

# Публикация
publish:
	poetry publish --dry-run

# Установка или переустановка с флагом --force-reinstall
package-install:
	python3 -m pip install --user dist/* --force-reinstall

# Проверка линтера
lint:
	poetry run flake8 gendiff

# Запуск тестов
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/