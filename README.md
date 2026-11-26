

# flow


## cli Argument

Synopsis: [--functions_definition <*function_definition_file*>] [--input <*input_file*>] [--output <*output_file*>]

Le synopsis decrit les arguments comme facultatifs [ ... ] . Si un argument est present il doit obligatoirement avoir cette structure [--argument <*variable*>]

### Exemple paramètres valide:

```bash

uv run python -m s
uv run python -m s --functions_definition path_1
uv run python -m s --functions_definition path_1 --output path_2
uv run python -m s --functions_definition path_1 --output path_2 --input path_3

```

### Exemple paramètres invalide:

```bash

uv run python -m s
uv run python -m s --functions_definition 
uv run python -m s --functions_definition path_1 --output
uv run python -m s --functions_definition path_1 --output path_2 --input
uv run python -m s --functions_definition  --output path_2 --input path_3

```


# Ressources


## UV

* https://docs.astral.sh/uv/pip/environments/
* https://docs.astral.sh/uv/guides/integration/pytorch/

##transformer
https://sebastianraschka.com/llm-architecture-gallery/
https://jalammar.github.io/illustrated-transformer/

## Calling tool

### BNF grammar

* https://www.ietf.org/ietf-ftp/rfc/std/std90.txt ->>> json rfc 8259
* https://camillemo.github.io/posts/bnf/

### CS 329Z: 
* https://www.youtube.com/watch?v=s0S38lz6O7M

### Logit masking

https://www.youtube.com/watch?v=QhgQKRRu3d4
