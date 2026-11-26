import cli
import pytest
import os
import time

def test_check_path():

    # No valide path
    assert(cli.check_path("data/", cli.File.INPUT) is False)
    assert(cli.check_path("data/input", cli.File.INPUT) is False)
    assert(cli.check_path("data/data_no_readable/input", cli.File.INPUT) is False)
    assert(cli.check_path("data/data_no_readable/output", cli.File.INPUT) is False)
    assert(cli.check_path("data/data_no_readable/input/function_calling_tests_no_readable.json", cli.File.INPUT) is False)
    assert(cli.check_path("data/data_no_readable/input/functions_definition_no_redable.json", cli.File.INPUT) is False)
    assert(cli.check_path("data/data_no_readable/output/function_calls_no_readable.json", cli.File.INPUT) is False)

    #valide path
    assert(cli.check_path("data/input/function_calling_tests.json", cli.File.INPUT) is True)
    assert(cli.check_path("data/input/functions_definition.json", cli.File.INPUT) is True)
    if (os.access("data/output/function_calls.json", os.W_OK)):
        assert(cli.check_path("data/output/function_calls.json", cli.File.INPUT) is True)

    try:
        c: cli.Cli = cli.check_argument_validity(["--functions_definition", "data/input/functions_definition.json", "--input", "data/input/function_calling_tests.json", "--output", "data/output/function_calls.json"]) 
        assert(c is not None)
        if os.access(c.output_path, os.W_OK):
            print(f"Remove {c.output_path}")
            os.remove(c.output_path)
            time.sleep(1)
        path: cli.PATH = cli.PATH(c)
        assert(os.access(path.output_path,os.W_OK))
    except cli.WRONG_PATH as e:
        print(e)
