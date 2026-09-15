VENV= .venv
venv:
	uv venv --clear

install: 
	uv sync

run:
	uv run python -m src

run_wf:
	@uv run python -m src --functions_definition data/input/functions_definition.json --input data/input/function_calling_tests.json --output data/output/function_calls.json

debug:
	uv run python -m pdb src/__main__.py

clean:
	find .   -type d  \( -name ".mypy_cache" -o -name "__pycache__" \) ! -path $(VENV) -exec rm -rf {} +

fclean: clean
	rm -rf $(VENV)
	
lint:
	-flake8 . --extend-exclude $(VENV),llm_sdk
	mypy . --exclude llm_sdk --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	-flake8 . --extend-exclude $(VENV),llm_sdk
	mypy . --exclude llm_sdk --strict