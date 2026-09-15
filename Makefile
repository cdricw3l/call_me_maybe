venv:
	uv venv

install: 
	uv pip install -r pyproject.toml

run:
	@uv run python -m src --functions_definition data/input/functions_definition.json --input data/input/function_calling_tests.json --output data/output/function_calls.json

debug:
	uv run python -m pdb src/__main__.py

clean:
	find src -type d  \( -name ".mypy_cache" -o -name "__pycache__" \) -exec rm -rf {} +
