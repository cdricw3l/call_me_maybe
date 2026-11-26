import sys
from cli import Cli, Bad_argument, check_argument_validity
from cli import PATH, WRONG_PATH 

if __name__ == "__main__":
    argv: list[str] = sys.argv
    try:
        cl: Cli = check_argument_validity(argv[1:])
        p: PATH = PATH(cl)
        print(p)
    except (Bad_argument, WRONG_PATH) as e:
        print(e)
