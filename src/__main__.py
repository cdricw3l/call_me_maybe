import sys
import argument_parsing
import llm_sdk


if __name__ == "__main__":
    try:
        argument_parsing.check_argument_validity(sys.argv)
        print("Argument Valide !")
    except argument_parsing.Bad_argument as e:
        print(e)
   