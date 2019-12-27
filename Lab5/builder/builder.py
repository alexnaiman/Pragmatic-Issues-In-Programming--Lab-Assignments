from parser import to_string
import logging
logger = logging.getLogger('lexer')


class JsonObjectBuilder:
    """
        Class for our JSON builder used for building JSON arrays
    """

    def __init__(self, parent=None, key=None):
        self.__parent = parent
        self.__object = dict()
        self.__key = key

    def put(self, key, value):
        """
            Function used for adding a property in our object
            Input:
                @param key -> string
                @param value -> oneOf(int, bool, float, None, array, JsonBuilder)
            Output: JsonObjectBuilder
            other possible names: add, maybe overriding __setitem__
        """
        assert type(key) == str, "Did not receive string as key!"
        assert type(value) in [str, int, float, list, dict, JsonBuilder,
                               JsonArrayBuilder, JsonObjectBuilder], "Did not receive compatible type as value!"

        logger.info("JsonObjectBuilder::put: ("+key+"," + str(key)+")")
        self.__object[key] = value
        return self

    def start_object(self, key):
        """
            Function used for starting  a new empty object in our JSON  as a new property
             Input:
                @param key -> string, it will add the new object as the given key
            Output: JsonObjectBuilder
            other possible names: start_json_object
        """
        assert type(key) == str, "Did not receive string as key!"
        logger.info("JsonObjectBuilder::start_object: " + key)

        self.__object[key] = JsonObjectBuilder(self, key)
        return self.__object[key]

    def start_array(self, key):
        """
            Function used for starting  a new empty object in our JSON  as a new property
             Input:
                @param key -> string, it will add the new array as the given key
            Output: JsonArrayBuilder
            other possible names: start_json_array
        """
        assert type(key) == str, "Did not receive string as key!"
        logger.info("JsonObjectBuilder::start_array: " + key)

        self.__object[key] = JsonArrayBuilder(self, key)
        return self.__object[key]

    def end_object(self):
        """
            Function used for ending the object in our JSON
            Output: JsonObjectBuilder | JsonArrayBuilder | JsonBuilder
            other possible names: end_json_object
        """
        logger.info("JsonObjectBuilder::end_object")
        if self.__key != None:
            self.__parent.put(self.__key, self.__object)
        if type(self.__parent) == JsonArrayBuilder:
            self.__parent.put(self.__object)
        return self.__parent

    def internal_form(self):
        """
            Function that returns the internal form for our object
            Output: dict
        """
        logger.info("JsonObjectBuilder::internal_form")

        return self.__object


class JsonArrayBuilder:
    """
        Class for our JSON builder used for building JSON arrays
    """

    def __init__(self, parent=None, key=None):
        self.__parent = parent
        self.__object = []
        self.__key = key

    def put(self, item):
        """
            Function used for adding a new object in our array
            Input:
                @param item -> oneOf(int, bool, float, None, array, JsonBuilder)
            Output: JsonArrayBuilder
            other possible names: append
        """
        assert type(item) in [str, int, float, list, dict, JsonBuilder,
                              JsonArrayBuilder, JsonObjectBuilder], "Did not receive compatible type as item!"
        logger.info("JsonArrayBuilder::put: " + str(item))
        self.__object.append(item)
        return self

    def start_object(self):
        """
            Function used for starting  a new empty object in our JSON
            Output: JsonObjectBuilder
            other possible names: start_json_object
        """
        logger.info("JsonArrayBuilder::start_object:")

        return JsonObjectBuilder(self)

    def start_array(self):
        """
            Function used for starting  a new empty array in our JSON
            Output: JsonArrayBuilder
            other possible names: start_json_array
        """
        logger.info("JsonArrayBuilder::start_array:")

        return JsonArrayBuilder(self)

    def end_array(self):
        """
            Function used for ending the array in our JSON
            Output: JsonObjectBuilder | JsonArrayBuilder | JsonBuilder
            other possible names: end_json_array
        """
        logger.info("JsonArrayBuilder::end_array:")

        if self.__key != None:
            self.__parent.put(self.__key, self.__object)
        if type(self.__parent) == JsonArrayBuilder:
            self.__parent.put(self.__object)
        return self.__parent

    def internal_form(self):
        """
            Function that returns the internal form for our object
            Output: array
        """
        logger.info("JsonArrayBuilder::internal_form:")
        return self.__object


class JsonBuilder:
    """
        Class for our JSON builder used for building JSONs
    """

    def __init__(self):
        self.__object = None

    def start_object(self):
        """
            Function used for starting  a new empty object in our JSON, as our root in the JSON tree
            Output: JsonObjectBuilder
            Exception: Cannot start another object! You need to build the object first
            other possible names: start_json_object
        """
        logger.info("JsonBuilder::start_object:")

        if self.__object != None:
            raise Exception(
                "Cannot start another object! You need to build the object first")
        self.__object = JsonObjectBuilder(self)
        return self.__object

    def start_array(self):
        """
            Function used for starting  a new empty object in our JSON, as our root in the JSON tree
            Output: JsonArrayBuilder
            Exception: Cannot start another array! You need to build the array first
            other possible names: start_json_array
        """
        logger.info("JsonBuilder::start_array:")

        if self.__object != None:
            raise Exception(
                "Cannot start another array! You need to build the array first")
        self.__object = JsonArrayBuilder(self)
        return self.__object

    def build(self):
        """
            Function used for building our JSON as a string
            Output: str
            other possible names: get, build_json
        """
        logger.info("JsonBuilder::build:")
        if self.__object == None:
            return to_string({})
        return to_string(self.__object.internal_form())
