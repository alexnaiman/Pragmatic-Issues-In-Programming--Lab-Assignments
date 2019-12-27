import logging
from parser.constants import JSON_TYPES, JSON_RIGHTBRACKET, JSON_LEFTBRACE, JSON_LEFTBRACKET, JSON_RIGHTBRACE, JSON_COMMA, JSON_COLON
logger = logging.getLogger('parser')


def parse_array(tokens):
    """
        Function used for parsing JSON arrays as tokens
        Input: list of tokens
        Output: array
        Exception: Expected comma after object in array
        other possible names: json_parse_array
    """
    assert type(tokens) == list, "Did not receive list!"
    for i in tokens:
        assert type(
            i) in JSON_TYPES, "Did not receive suitable type! Cannot parse: " + str(i)
    logger.info('parse_array: Received tokens: ' + str(tokens))
    json_array = []

    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        logger.info('parse_array: Returned object: ' + str(json_array))
        return json_array, tokens[1:]

    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            logger.info('parse_array: Returned object: ' + str(json_array))
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise Exception('Expected end-of-array bracket')


def parse_object(tokens):
    """
        Function used for parsing JSON objects as tokens
        Input: list of tokens
        Output: python dictionary
        Exception: 
            - Expected colon after key in object;
            - Expected string key; Expected comma after pair in object
            - Expected end-of-object bracket'
        other possible names: json_parse_object
    """
    assert type(tokens) == list, "Did not receive list!"
    for i in tokens:
        assert type(
            i) in JSON_TYPES, "Did not receive suitable type! Cannot parse: " + str(i)
    logger.info('parse_object: Received tokens: ' + str(tokens))
    json_object = {}

    t = tokens[0]
    if t == JSON_RIGHTBRACE:
        logger.info('parse_object: Returned object: ' + str(json_object))
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expected string key, got: {}'.format(json_key))

        if tokens[0] != JSON_COLON:
            raise Exception(
                'Expected colon after key in object, got: {}'.format(t))

        json_value, tokens = parse(tokens[1:])

        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            logger.info('parse_object: Returned object: ' + str(json_object))
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception(
                'Expected comma after pair in object, got: {}'.format(t))

        tokens = tokens[1:]

    raise Exception('Expected end-of-object bracket')


def parse(tokens, is_root=False):
    """
        Function used for parsing JSON string as tokens
        Input: list of tokens
        Output: python objects
        Exception: 
            - Root must be an object;
        other possible names: json_parse
    """
    assert type(tokens) == list, "Did not receive list!"
    for i in tokens:
        assert type(
            i) in JSON_TYPES, "Did not receive suitable type! Cannot parse: " + str(i)
    assert type(is_root) == bool, "Did not receive bool!"
    logger.info('parse: Received tokens: ' +
                str(tokens) + " is_root = " + str(is_root))
    t = tokens[0]

    if is_root and t != JSON_LEFTBRACE:
        raise Exception('Root must be an object')

    if t == JSON_LEFTBRACKET:
        logger.info('parse: Returned type: ' + str(type([])))
        return parse_array(tokens[1:])
    elif t == JSON_LEFTBRACE:
        logger.info('parse: Returned type: ' + str(type({})))
        return parse_object(tokens[1:])
    else:
        logger.info('parse: Returned type: ' + str(type(t)))
        return t, tokens[1:]
