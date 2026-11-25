import os
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

    input_definition: str
    input_calling: str
    output: str
    def __init__(self,
                 input_definition: str = "data/input/functions_definition.json",
                 input_calling: str = "data/input/function_calling_tests.json",
                 output: str = "data/output/function_calls.json"):
        if check_path(input_definition) is False:
            raise WRONG_PATH(f"input file {input_definition} doesn't exist")
        elif check_path(input_calling) is False:
            raise WRONG_PATH(f"input file {input_calling} doesn't exist")
        if check_path(output) is False:
            try:
                path: Path = Path(output)
                path.parent.mkdir(parents=True,exist_ok=True)
                path.touch(exist_ok=True)
                # 0o -> base octal. à approfondir
                path.chmod(0o660)
            except Exception as e:
                raise WRONG_PATH(f"output file {output} error: {e}")
        self.input_definition = input_definition
        self.input_calling = input_calling
        self.output = output

    def __str__(self):
        return(f"input_definition: {self.input_definition:>10}\ninput_calling: {self.input_calling:>10}\noutput:{self.output:>10}")
