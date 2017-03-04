class Zone:
    __zone = None
    __name = None
    __id = None

    def __init__(self, zone_obj):
        self.__zone = zone_obj
        self.__id = zone_obj['id']
        self.__name = zone_obj['name']

    def get_name(self):
        return self.__name
