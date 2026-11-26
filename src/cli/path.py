import os
import cli
from pathlib import Path

class WRONG_PATH(Exception):
    """ exception raised when input path doesn't existe """ 
    message:str
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_path(path: str) -> bool :
    """ this fonction check the validity of a path """
    if (os.path.exists(path)):
        return (True)
    return (False)

class PATH:
    """ this class check and create a path object with input and output file informations """

    definition_path: str
    input_path: str
    output_path: str
    def __init__(self, cli: cli.Cli):
        if check_path(cli.input_path) is False:
            raise WRONG_PATH(f"input file {cli.input_path} doesn't exist")
        elif check_path(cli.input_path) is False:
            raise WRONG_PATH(f"input file {cli.input_path} doesn't exist")
        if check_path(cli.output_path) is False:
            try:
                path: Path = Path(cli.output_path)
                path.parent.mkdir(parents=True,exist_ok=True)
                path.touch(exist_ok=True)
                # 0o -> base octal. à approfondir
                path.chmod(0o660)
            except Exception as e:
                raise WRONG_PATH(f"output file {cli.output_path} error: {e}")
        self.definition_path = cli.functions_definition
        self.input_path = cli.input_path
        self.output_path = cli.functions_definition

    def __str__(self):
        return(f"definition_path: {self.definition_path:>10}\ninput_path: {self.input_path:>10}\noutput_path:{self.output_path:>10}")
