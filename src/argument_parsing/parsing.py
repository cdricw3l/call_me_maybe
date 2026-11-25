from pydantic import BaseModel, ValidationError, Field
from typing import Optional, Literal

class Bad_argument(Exception):
     """Exception raised for wrong programme arguments."""
     def __init__(self):
         super().__init__("Invalide programme arguments.") # enrichire potentiellement le message avec un format d'argument valide


class Parsing(BaseModel):
  # Field(..., alias="...") permet d'associer le flag au nom de la variable
  functions_definition: str = Field(..., validation_alias="--functions_definition")
  input_path: str | None  = Field(None, validation_alias="--input")
  output_path: str | None = Field(None, alias="--output")



def get_arguments_obj(argv: list[str]) -> dict[str, str]:
    """ convert an argument list to  dictionnary """
    dict_arg: dict[str, str | None] = {}
    for i in range(1, len(argv), 2):
        if i == len(argv):
            dict_arg.update({argv[i]:None})
        else:
            dict_arg.update({argv[i]:argv[i + 1]})
    return dict_arg



class Test(BaseModel):
    functions_definition: str = Field(alias="--functions_definition")
    caca1: str = Field(alias="--caca")
   

# def check_argument_validity(argv: list[str]) -> bool:
#     args: dict[str, str] = get_arguments_obj(argv)
    # print(args)
    # try:
    #     Parsing.model_validate(args)
    # except ValidationError as e:
    #     raise Bad_argument

def check_argument_validity(argv: list[str]) -> bool:
    d = {"--functions_definition": "hello", "--caca1": "hello"}
    Test.model_validate(d)
    # print(args)
    # try:
    #     Parsing.model_validate(args)
    # except ValidationError as e:
    #     raise Bad_argument