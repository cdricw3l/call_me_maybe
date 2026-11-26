import sys
from cli import Cli, Bad_argument, check_argument_validity

if __name__ == "__main__":
    argv: list[str] = sys.argv
    try:
        a: Cli = check_argument_validity(argv)
        print(a)
    except Bad_argument as e:
        print(e)
    