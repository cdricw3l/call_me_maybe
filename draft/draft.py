from pathlib import Path
import os
from pydantic import BaseModel, Field
from typing import Literal, Callable
import cli
import json
import llm_sdk
import torch
import math
import numpy as np
from functools import wraps, lru_cache
import time
import interface

E =  2,71828

def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Fonction completed in {round(end - start, 3) * 1000} ms")
        return result
    return wrapper

@timer
def softmax_1(x) -> np.ndarray:
    return (np.exp(x) / np.exp(x).sum())

@timer
def softmax_2(x) -> np.ndarray:
    return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

def softmax_3(logits: list[float], ) -> np.ndarray:
    ex = np.exp(logits - np.max(logits))
    return (ex / ex.sum())


def get_logits(model: llm_sdk.Small_LLM_Model , tokens: list[int]) -> list[float]:
    return model.get_logits_from_input_ids(tokens)


def generation(model: llm_sdk.Small_LLM_Model, prompt: str, nb_token: int):

    
    tool = {
        "name": "fn_add_numbers",
        "description": "Add two numbers together and return their sum.",
        "parameters": {
        "a": {
            "type": "number"
        },
        "b": {
            "type": "number"
        }
        },
        "returns": {
        "type": "number"
        }
    }
    formatted_prompt = (
        f"<|im_start|>user\n"
        f"{prompt}<|im_end|>\n"
        f"<|im_start|>assistant\n"
        f"<think>\n\n</think>\n\n"
    )
    token = model.encode(formatted_prompt).tolist()[0]

    for i in range(1, nb_token):
        logits = get_logits(model,token)
        soft = softmax_3(logits)
        next = int(np.argmax(soft))
        token.append(next)
    print(model.decode(token))



# class Promt(BaseModel):


if __name__ == "__main__":

    tool = {
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
            },
            "dwd": {
                "type": "number"
            }
        },
        "returns": {
            "type": "number"
        }
    }

    prompt = {
        
        "prompt": "Substitute the word 'cat' with 'dog' in 'The cat sat on the mat with another cat'"
    }

    calling = {
        
        "prompt": "What is the sum of 2 and 3?",
        "name": "fn_add_numbers",
        "parameters": {"a": {"hello": 10}, "b": 3.0}
    }

    interface.Definition.model_validate(tool)
    interface.Prompt.model_validate(calling)
    interface.Calling.model_validate(calling)

    