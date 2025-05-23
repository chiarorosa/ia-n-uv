import sys

from .utils import parse_args

# Entry point do pacote


def main():
    print("Meu pacote python começa aqui!")
    args = parse_args()
    try:
        # url = args.url
        problema = args.problema
        print(f"Problema: {problema}")
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
