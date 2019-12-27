import parser


# class BaseJsonBuilder:
"""
        Base class for our JSON builder
    """

#     def put(self, key):
#         pass

#     def __init__(self):
#         self.__object = dict()

#     def start_object(self, key=None, root=False):
#         """
#             Function used for starting  a new empty object in our json, as a new property or not
#             Input:
#                 @param key -> string (if provided, it will add the new object as the given key)
#             Output: JsonObjectBuilder
#             other possible names: start_json_object
#         """
#         assert type(key) in [str, type(None)
#                              ], "Did not receive string for key!"
#         if root:
#             self.__object = JsonObjectBuilder()
#         else:
#             self.__object = JsonObjectBuilder(self, key)
#         return self.__object

#     def start_array(self, key=None):
#         """
#             Function used for starting a new empty array in our json, as a new property or not
#             Input:
#                 @param key -> string (if provided, it will add the new object as the given key)
#             Output: JsonArrayBuilder
#             other possible names: start_json_array
#         """
#         assert type(key) in [str, type(None)
#                              ], "Did not receive string for key!"
#         self.__object = JsonArrayBuilder(self, key)
#         return self.__object

#     def build(self, root=False):
#         return self.__object.build(root)


# class JsonObjectBuilder(BaseJsonBuilder):
#     """
#         Derived class for our JSON builder used for building JSON objects
#     """

#     def __init__(self, parent=None, key=None):
#         """
#             Our constructor
#             Input:
#                 @param parent -> it's parent in the JSON tree(if exists)
#                 @param key -> name of the property of the object in which we will assign this object
#         """
#         assert type(key) in [str, type(None)
#                              ], "Did not receive string for key!"
#         assert type(parent) in [str, list, dict,
#                                 BaseJsonBuilder, JsonBuilder, JsonArrayBuilder, JsonObjectBuilder, type(None)], "parent type incompatible!"
#         BaseJsonBuilder.__init__(self)
#         self.__object = dict()
#         self.__parent = parent
#         self.__key = key

#     def put(self, key, value):
#         """
#             Function used for adding a property in our json
#             Input:
#                 @param key -> string
#                 @param value -> oneOf(int, bool, float, None, array, JsonBuilder)
#             Output: BaseJsonBuilder
#             other possible names: add, maybe overriding __setitem__
#         """
#         assert type(key) in [str, type(None)
#                              ], "Did not receive string for key!"
#         assert type(value) in [str, list, dict,
#                                BaseJsonBuilder, JsonArrayBuilder, JsonObjectBuilder, JsonBuilder, type(None)], "Value type incompatible!"
#         self.__object[key] = value
#         return self

#     def build(self):
#         """
#             Function that builds our JsonObjectBuilder into our object
#             Output: dict
#             other possible names: get
#         """
#         if self.__parent != None:
#             return self.end_object().build()
#         return self.__object

#     def end_object(self):
#         """
#             Function used for ending the object in our json, adding it as a new property or not
#             Output: JsonObjectBuilder
#             other possible names: end_json_object
#         """
#         if self.__key != None:
#             self.__parent.put(self.__key, BaseJsonBuilder.build(self))
#         else:
#             self.__parent.put(BaseJsonBuilder.build(self))
#         return self.__parent


# class JsonArrayBuilder(BaseJsonBuilder):
#     """
#         Derived class for our JSON builder used for building JSON arrays
#     """

#     def __init__(self, parent=None, key=None):
#         """
#             Our constructor
#             Input:
#                 @param parent -> it's parent in the JSON tree(if exists)
#                 @param key -> name of the property of the object in which we will assign this object
#         """
#         assert type(key) in [str, type(None)
#                              ], "Did not receive string for key!"
#         assert type(parent) in [str, list, dict,
#                                 BaseJsonBuilder, JsonBuilder, JsonArrayBuilder, JsonObjectBuilder, type(None)], "parent type incompatible!"
#         BaseJsonBuilder.__init__(self)
#         self.__parent = parent
#         self.__key = key
#         self.__list = []

#     def put(self, item):
#         """
#             Function used for adding a new object in our array
#             Input:
#                 @param item -> oneOf(int, bool, float, None, array, JsonBuilder)
#             Output: JsonArrayBuilder
#             other possible names: append
#         """
#         assert type(item) in [str, list, dict,
#                               BaseJsonBuilder, JsonArrayBuilder, JsonObjectBuilder, JsonBuilder, type(None)], "Value type incompatible!"

#         self.__list.append(item)
#         return self

#     def build(self):
#         """
#             Function that builds our JsonArrayBuilder into our array
#             Output: array
#             other possible names: get
#         """
#         if self.__parent != None:
#             raise Exception("salutare")
#         return self.__list

#     def end_array(self):
#         """
#             Function used for ending the array in our json, adding it as a new property or not
#             Output: JsonArrayBuilder
#             other possible names: end_json_object
#         """
#         if self.__key != None:
#             self.__parent.put(self.__key, self.__list)
#         else:
#             self.__parent.put(self.__list)
#         return self.__parent


# class JsonBuilder(BaseJsonBuilder):
#     """
#         Derived class for our JSON builder used for building JSONs
#     """

#     def __init__(self):
#         BaseJsonBuilder.__init__(self)

#     def build(self):
#         """
#             Function that builds our JSON object into our JSON string
#             Output: string
#             other possible names: get, to string
#         """
#         return parser.to_string(BaseJsonBuilder.build(self))

class JsonObjectBuilder:
    """
        Derived class for our JSON builder used for building JSON objects
    """

    def __init__(self, parent=None, key=None):
        """
            Our constructor
            Input:
                @param parent -> it's parent in the JSON tree(if exists)
                @param key -> name of the property of the object in which we will assign this object
        """
        assert type(key) in [str, type(None)
                             ], "Did not receive string for key!"
        assert type(parent) in [str, list, dict,
                                BaseJsonBuilder, JsonBuilder, JsonObjectBuilder, type(None)], "parent type incompatible!"
        self.__object = dict()
        self.__parent = parent
        self.__key = key

    def put(self, key, value):
        """
            Function used for adding a property in our json
            Input:
                @param key -> string
                @param value -> oneOf(int, bool, float, None, array, JsonBuilder)
            Output: BaseJsonBuilder
            other possible names: add, maybe overriding __setitem__
        """
        assert type(key) in [str, type(None)
                             ], "Did not receive string for key!"
        assert type(value) in [str, list, dict,
                               BaseJsonBuilder, JsonObjectBuilder, JsonBuilder, type(None)], "Value type incompatible!"
        self.__object[key] = value
        return self

    def build(self):
        """
            Function that builds our JsonObjectBuilder into our object
            Output: dict
            other possible names: get
        """
        if self.__parent != None:
            return self.end_object().build()
        return self.__object

    def end_object(self):
        """
            Function used for ending the object in our json, adding it as a new property or not
            Output: JsonObjectBuilder
            other possible names: end_json_object
        """
        # if self.__key != None:
        #     self.__parent.put(self.__key, BaseJsonBuilder.build(self))
        # else:
        #     self.__parent.put(BaseJsonBuilder.build(self))
        return self.__parent


class BaseJsonBuilder:
    """
        Base class for our JSON builder
    """

    # def put(self, key):
    #     pass

    def __init__(self, root=False):
        self.__object = dict()
        self.__root = root

    def start_object(self, key=None, root=False):
        """
            Function used for starting  a new empty object in our json, as a new property or not
            Input:
                @param key -> string (if provided, it will add the new object as the given key)
            Output: JsonObjectBuilder
            other possible names: start_json_object
        """
        assert type(key) in [str, type(None)
                             ], "Did not receive string for key!"
        if root:
            self.__object = JsonObjectBuilder()
        else:
            self.__object = JsonObjectBuilder(self, key)
        return self.__object

    # def start_array(self, key=None):
    #     """
    #         Function used for starting a new empty array in our json, as a new property or not
    #         Input:
    #             @param key -> string (if provided, it will add the new object as the given key)
    #         Output: JsonArrayBuilder
    #         other possible names: start_json_array
    #     """
    #     assert type(key) in [str, type(None)
    #                          ], "Did not receive string for key!"
    #     self.__object = JsonArrayBuilder(self, key)
    #     return self.__object

    # def build(self, root=False):
    #     return self.__object.build(root)


# class JsonBuilder(BaseJsonBuilder):
#     def __init__(self, root=True, obj=None):
#         self.__object = obj
#         self.__root = root

#     def start_object(self):
#         obj = BaseJsonBuilder.start_object(self, self.__root)
#         return JsonBuilder(False, obj)

#     def build(self):
#         if self.__root:
#             return ""
#         return parser.to_string(self.__object)
