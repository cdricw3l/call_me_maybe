import cli
import pytest

def test_cli_parsing():
    
    # Valide arguments

    argv_1: list[str] = ["--functions_definition", "data/input/functions_definition.json"]
    argv_2: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json"]
    argv_3: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--output", "data/output/function_calls.json"]
    
    # manage argument in different order
    argv_4: list[str] = ["--input", "data/input/function_calling_tests.json", "--functions_definition", "data/input/functions_definition.json", "--output", "data/output/function_calls.json"]
    
    assert(cli.check_argument_validity(argv_1) is not None)
    assert(cli.check_argument_validity(argv_2) is not None)
    assert(cli.check_argument_validity(argv_3) is not None)
    assert(cli.check_argument_validity(argv_4) is not None)
   

    # Invalide arguments

    argv_5: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--output"]



    