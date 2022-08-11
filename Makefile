.PHONY: lint check
lint:
	python -m black pyokx
	python -m autoflake pyokx -r --in-place --remove-unused-variables --remove-all-unused-imports
check:
	python -m black pyokx --check
	python -m mypy pyokx

.PHONY: test test-html
test:
	pytest pyokx
	coverage report

covhtml:
	coverage html

.PHONY: commit
commit: check test

.PHONY: setup
setup:
	git config --local core.hooksPath ./hooks/
	chmod +x ./hooks/pre-commit
	poetry install