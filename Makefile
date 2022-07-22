.PHONY: lint check
lint:
	python -m black pyokx
check:
	python -m black pyokx --check
	python -m mypy pyokx

.PHONY: test test-html
test:
	pytest pyokx
	coverage report --fail-under=95

covhtml:
	coverage html

.PHONY: commit
commit: check test

.PHONY: setup
setup:
	git config --local core.hooksPath ./hooks/
	chmod +x ./hooks/pre-commit
	poetry install