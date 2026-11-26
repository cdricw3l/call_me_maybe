import cli
import pytest

def test_cli_parsing():
    """ This test check the good validation of flag argumennt"""
    
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
    argv_6: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--input"]
    argv_7: list[str] = ["--functions_definition"]
    argv_8: list[str] = []
    argv_9: list[str] = ["--bad_flag", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--output", "data/output/function_calls.json"]
    argv_10: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--bad_flag", "data/input/function_calling_tests.json", "--output", "data/output/function_calls.json"]
    argv_11: list[str] = ["--functions_definition", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--bad_flag", "data/output/function_calls.json"]
    argv_12: list[str] = ["--functions_definitions", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--output", "data/output/function_calls.json"]

    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_5)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_6)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_7)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_8)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_9)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_10)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_11)
    with pytest.raises(cli.Bad_argument):
        cli.check_argument_validity(argv_12)
    

    