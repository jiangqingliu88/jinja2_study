import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arg", type=str, required=False, help="optional argument")

args = parser.parse_args()
if args.arg:
    print("Argument exists with value:", args.arg)
else:
    print("Argument does not exist")
