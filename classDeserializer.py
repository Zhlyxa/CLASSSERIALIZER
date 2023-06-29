import json


class ClassDeserializer:
    @staticmethod
    def deserializer(className: str, fileName: str):
        """Метод десериализации сериализованного экземпляра класса
        
        Args:
            ``className`` (str): имя класса в результате
            ``fileName`` (str): имя файла данных для десериализации\n
        """
        with open(fileName, 'r') as file:
            raw_class = json.load(file)

            return type(className, (object,), {**raw_class})

    @staticmethod
    def deserializerAll(classNames: list[str],fileName: str):
        """Метод десериализации набора сериализованных экземпляров классов
        
        Args:
            ``classNames`` (list): список имен классов в результате
            ``fileName`` (str): имя файла данных для десериализации
        """
        with open(fileName, 'r') as file:
            raw_class = json.load(file)
            result = []
            for e, data in enumerate(raw_class.values()):
                result.append(type(classNames[e], (object,), {**data}))

            return result

    @staticmethod
    def deserializerStructururAll(fileName: str):
        """Метод десериализации структурной сериализации
        
        Args:
            ``fileName`` (str): имя файла данных для десериализации
        """
        with open(fileName, 'r') as file:
            raw_class = json.load(file)
            result = []

            for data in raw_class.items():
                for obj in data[1]:
                    result.append(type(data[0], (object,), {**obj}))

            return result