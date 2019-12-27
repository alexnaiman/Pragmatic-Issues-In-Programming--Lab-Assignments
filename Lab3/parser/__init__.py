from parser.lexer import lex
from parser.parser import parse

# Basic interface for our parser


def from_string(string):
    """
        Returns the corresponding python object for the given JSON input
        :param string - input string in JSON
        :return object - corresponding to the given json
        :raises Exception -  if input string cannot be parsed
    """
    tokens = lex(string)
    return parse(tokens, is_root=True)[0]


def to_string(json):
    """
        Returns the corresponding JSON string for the given python object
        :param json - input python object
        :return string - JSON encoding for given object
    """
    json_type = type(json)
    if json_type is dict:
        string = '{'
        dict_len = len(json)

        for i, (key, val) in enumerate(json.items()):
            string += '"{}": {}'.format(key, to_string(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'

        return string
    elif json_type is list:
        string = '['
        list_len = len(json)

        for i, val in enumerate(json):
            string += to_string(val)

            if i < list_len - 1:
                string += ', '
            else:
                string += ']'

        return string
    elif json_type is str:
        return '"{}"'.format(json)
    elif json_type is bool:
        return 'true' if json else 'false'
    elif json_type is None:
        return 'null'

    return str(json)
