import os
import cli
from pathlib import Path
from enum import Enum

class WRONG_PATH(Exception):
    """ exception raised when input/output path doesn't existe """ 
    message:str
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class File(Enum):
    DEFINITION = 1
    INPUT = 2
    OUTPUT = 3

def check_path(path: str, file: File) -> bool :
    """
        --functions_definition -> check if the path existe , if he is readable, if he is a file.
        --input -> check if the path existe , if he is readable, if he is a file.
        --output -> check if the path existe , if he is writable, if he is a file if not, try to create.
    """
    if (file == File.DEFINITION or file == File.INPUT):
        if (os.access(path, os.R_OK) and os.path.isfile(path)):
            return (True)
    if (file == File.OUTPUT and os.access(path, os.W_OK)):
        if os.path.isfile(path):
            return (True)
    return (False)

class PATH:
    """ this class check and create a path object with input and output file informations """

    definition_path: str
    input_path: str
    output_path: str
    def __init__(self, cli: cli.Cli):
        if check_path(cli.functions_definition, File.DEFINITION) is False:
            raise WRONG_PATH(f"function definition {cli.functions_definition} invalide path")
        if check_path(cli.input_path, File.INPUT) is False:
            raise WRONG_PATH(f"input file {cli.input_path} invalide path")
        if check_path(cli.output_path, File.OUTPUT) is False:
            try:
                with open(cli.output_path, 'a'):
                    pass
            except Exception as e:
                raise WRONG_PATH(f"output file {cli.output_path} error: {e}")
        self.definition_path = cli.functions_definition
        self.input_path = cli.input_path
        self.output_path = cli.output_path

    def __str__(self):
        return(f"definition_path: {self.definition_path:>10}\ninput_path: {self.input_path:>10}\noutput_path:{self.output_path:>10}")
