from pydantic import BaseModel, ValidationError, Field

INPUT_DEFAULT_PATH = "data/input/"
OUTPUT_DEFAULT_PATH = "data/output/"

class Bad_argument(Exception):
     """Exception raised for wrong programme arguments."""
     def __init__(self):
         super().__init__("Invalide programme arguments.") # enrichire potentiellement le message avec un format d'argument valide


class Cli(BaseModel):
    # Field(..., alias="...") permet d'associer le flag au nom de la variable
    functions_definition: str = Field(..., validation_alias="--functions_definition")
    input_path: str | None  = Field(..., validation_alias="--input")
    output_path: str | None = Field(..., alias="--output")


def get_arguments_obj(argv: list[str]) -> dict[str, str]:
    """ convert an argument list to  dictionnary """
    args: dict[str, str] = {}
    match len(argv):
        case 3:
            args = {argv[1]:argv[2], "--input":INPUT_DEFAULT_PATH, "--output":OUTPUT_DEFAULT_PATH}
        case 5:
            args = {argv[1]:argv[2], argv[3]:argv[4], "--output":OUTPUT_DEFAULT_PATH}
        case 7:
            args = {argv[1]:argv[2], argv[3]:argv[4], argv[5]:argv[6]}
        case _:
            raise Bad_argument
    return args


def check_argument_validity(argv: list[str]) -> Cli:
    try:
        args : dict[str, str] = get_arguments_obj(argv)
        cli: Cli = Cli.model_validate(args)
        print("argument are valide")
    except ValidationError as e:
        raise Bad_argument
    return cli
