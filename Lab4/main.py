import parser
import sys
import logging

# small example
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )
    if len(sys.argv) == 1:
        file = 'example1.json'
    else:
        file = sys.argv[1]
    with open(file, 'r') as f:
        print(parser.to_string(parser.from_string(f.read())))
