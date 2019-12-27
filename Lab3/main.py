import parser
import sys

# small example
if len(sys.argv) == 1:
    file = 'example1.json'
else:
    file = sys.argv[1]
with open(file, 'r') as f:
    print(parser.to_string(parser.from_string(f.read())))
