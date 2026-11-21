import sys
import init
import llm_sdk
from pydantic import BaseModel, ValidationError, Field


class Parsing(BaseModel):
  # Field(..., alias="...") permet d'associer le flag au nom de la variable
  functions_definition: str = Field(..., alias="--functions_definition")
  input_path: str = Field(..., alias="--input")
  output_path: str = Field(..., alias="--output")


def main() -> None:
    pass

def get_arguments_obj(argv: list[str]) -> dict[str]:
    """ convert an argument list to  dictionnary """
    obj: dict[str] = {argv[1]:argv[2],argv[3]:argv[4],argv[5]:argv[6]}
    return obj


if __name__ == "__main__":
    if len(sys.argv) == 1:
        try:
            paths: init.PATH = init.PATH()
        except init.WRONG_PATH as e:
            print(e)
            exit(1)
    elif len(sys.argv) == 7:
        p : dict[str] = get_arguments_obj(sys.argv)
        try:
            Parsing.model_validate(p)
        except ValidationError as e:
            print(f"modele non validé {e}")
    else:
        print("Argument error")