import cli
from pydantic import BaseModel, Field
from typing import Any


class Type(BaseModel):
    type: str = Field(..., validate_default="type")


class Definition(BaseModel):
    """
    functions_definition shema:

    {
            "name": "fn_add_numbers",
            "description": "Add two numbers together and return their sum.",
            "parameters": {
                "a": {
                    "type": "number"
                },
                "b": {
                    "type": "number"
                },
                "c": {
                    "type": "number"
                }
            },
            "returns": {
                "type": "number"
            }
        }

    """
    name: str = Field(..., validate_default="name")
    description: str = Field(..., validate_default="description")
    parameters: dict[str, Type] = Field(..., validate_default="parameters")
    returns: Type =  Field(..., validate_default="returns")


class Prompt(BaseModel):
    """
        prompt shema: 
        {
            "prompt": "Greet shrek"
        },

    """
    prompt: str = Field(..., validate_default="prompt")


class Calling(BaseModel):
    """
        {
            "prompt": "Reverse the string 'hello'",
            "name": "fn_reverse_string",
            "parameters": {"s": "hello"}
        }
    """
    prompt: str = Field(..., validate_default="prompt")
    name: str = Field(..., validate_default="name")
    parameters: dict[str, Any]