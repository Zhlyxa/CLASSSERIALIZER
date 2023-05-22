import json


class ClassSerializer:
    @staticmethod
    def serializer(obj, fileName: str):
        """Метод сериализации экземпляра класса

        Args:
            ``obj`` (Any): один экземляр класса для сериализации\n
            ``fileName`` (str): имя файла для результата сериализации (``.json``)\n
        """
        with open(fileName, 'w') as file:
            data = {}
            attributes = obj.__dict__

            for attribute in attributes:
                if attribute.find('__') >= 0:
                    data[attribute[attribute.find(
                        '__')+2:]] = obj.__getattribute__(attribute)
                else:
                    data[attribute] = obj.__getattribute__(attribute)

            json.dump(data, file)

    @staticmethod
    def serializerAll(objs: list, fileName: str):
        """Метод для сериализации списка экземпляров классов

        Аргументы:
            ``objs`` (list): список экземпляров классов\n
            ``fileName`` (str): имя файла для результата сериализации (``.json``)\n
        """
        with open(fileName, 'w') as file:
            data = {}

            for enum, obj in enumerate(objs):
                data[enum] = {}
                attributes = obj.__dict__
                for attribute in attributes:
                    if attribute.find('__') >= 0:
                        data[enum][attribute[attribute.find(
                            '__')+2:]] = obj.__getattribute__(attribute)
                    else:
                        data[enum][attribute] = obj.__getattribute__(attribute)

            json.dump(data, file)

    @staticmethod
    def structurSerializeAll(objs: list, fileName: str, schema: dict):
        """Метод структурной сериализации списка экземляров 

        Аргументы:
            ``objs`` (list): список экземпляров классов\n
            ``fileName`` (str):имя файла для результата сериализации (``.json``)\n
            ``schema`` (dict): структура результата сериализации вида ``KeyClasses (str):TypeClasses (str)``\n
        """
        with open(fileName, 'w') as file:
            data = {key: [] for key in schema}

            for obj in objs:
                className = str(obj.__class__)
                className = className[className.rfind(
                    '.')+1:className.rfind("'")]

                for keyClass, typeClass in schema.items():
                    if typeClass == className:
                        item = {}
                        attributes = obj.__dict__

                        for attribute in attributes:
                            if attribute.find('__') >= 0:
                                item[attribute[attribute.find(
                                    '__')+2:]] = obj.__getattribute__(attribute)
                            else:
                                item[attribute] = obj.__getattribute__(
                                    attribute)

                        data[keyClass].append(item)
                        break

            json.dump(data, file)