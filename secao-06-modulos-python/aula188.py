# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Olá Mundo" na tela',
    # type=str,
    metavar="STRING",
    # default="Olá Mundo",
    required=False,
    action="append"
    # nargs="+", # Recebe mais de um valor
)
parser.add_argument("-v", "--verbose", help="Mostra logs", action="store_true")
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de "basic".')
    print(args.basic)
else:
    print(f"O valor de basic é: {args.basic}")

print(args.verbose)
