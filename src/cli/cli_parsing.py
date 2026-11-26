from pydantic import BaseModel, ValidationError, Field

INPUT_DEFAULT_PATH = "data/input/"
OUTPUT_DEFAULT_PATH = "data/output/"


class Bad_argument(Exception):
    """Exception raised for wrong programme arguments."""
    def __init__(self) -> None:
        super().__init__("Invalide programme arguments.")
        # enrichire potentiellement le message avec un format d'argument valide


class Cli(BaseModel):
    # Field(..., alias="...") permet d'associer le flag au nom de la variable
    functions_definition: str = Field(
                                        ...,
                                        validation_alias
                                        ="--functions_definition"
                                     )
    input_path: str = Field(..., validation_alias="--input")
    output_path: str = Field(..., alias="--output")


def get_arguments_obj(argv: list[str]) -> dict[str, str]:
    """ convert an argument list to  dictionnary """
    args: dict[str, str] = {}
    match len(argv):
        case 2:
            args = {
                        argv[0]: argv[1],
                        "--input": INPUT_DEFAULT_PATH,
                        "--output": OUTPUT_DEFAULT_PATH
                    }
        case 4:
            args = {
                        argv[0]: argv[1],
                        argv[2]: argv[3],
                        "--output": OUTPUT_DEFAULT_PATH
                    }
        case 6:
            args = {
                        argv[0]: argv[2],
                        argv[2]: argv[3],
                        argv[4]: argv[5]
                    }
        case _:
            raise Bad_argument
    return args


def check_argument_validity(argv: list[str]) -> Cli:
    """
        This fonction check the good validity of program argument.
        Doesnt check the validity of path
    """
    try:
        args: dict[str, str] = get_arguments_obj(argv)
        cli: Cli = Cli.model_validate(args)
        print("argument are valide")
    except ValidationError:
        raise Bad_argument
    return cli
