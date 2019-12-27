from parser.constants import *

# Function used for obtaining python string object token from json string
# Input: string
# Output: (python string token, remaining string); if first character is JSON_QUOTE
#         (None object, remaining string), otherwise
# Exception: End of string quote was not found
# other possible names: token_string, token_string_from_json
def lex_string(string):
    json_string = ''

    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string

    for c in string:
        if c == JSON_QUOTE:
            return json_string, string[len(json_string)+1:]
        else:
            json_string += c

    raise Exception('Expected end-of-string quote')


# Function used for obtaining python int or float object token from json string
# Input: string
# Output: python int or float token, remaining string
#         (None object, remaining string), otherwise
# other possible names: token_number, token_number_from_json
def lex_number(string):
    json_number = ''

    number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']

    for c in string:
        if c in number_characters:
            json_number += c
        else:
            break

    rest = string[len(json_number):]

    if not len(json_number):
        return None, string

    if '.' in json_number:
        return float(json_number), rest

    return int(json_number), rest

# Function used for obtaining python bool object token from json string
# Input: string
# Output: python float token, remaining string
#         (None object, remaining string), otherwise
# other possible names: token_bool, token_bool_from_json
def lex_bool(string):
    string_len = len(string)

    if string_len >= TRUE_LEN and \
            string[:TRUE_LEN] == 'true':
        return True, string[TRUE_LEN:]
    elif string_len >= FALSE_LEN and \
            string[:FALSE_LEN] == 'false':
        return False, string[FALSE_LEN:]

    return None, string

# Function used for obtaining python None object token from json string
# Input: string
# Output: python bool set on True token, remaining string
#         (None object, remaining string), otherwise
# other possible names: token_null, token_null_from_json
def lex_null(string):
    string_len = len(string)

    if string_len >= NULL_LEN and \
            string[:NULL_LEN] == 'null':
        return True, string[NULL_LEN]

    return None, string

# Function used for obtaining python None object token from json string
# Input: string
# Output: python bool set on True token, remaining string
#         (None object, remaining string), otherwise
# other possible names: token_null, token_null_from_json
def lex(string):
    tokens = []

    while len(string):
        json_string, string = lex_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_bool, string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue

        c = string[0]

        if c in JSON_WHITESPACE:
            # Ignore whitespace
            string = string[1:]
        elif c in JSON_SYNTAX:
            tokens.append(c)
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(c))

    return tokens
