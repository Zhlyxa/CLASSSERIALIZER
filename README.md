# ClassToJson
## RU
Это модуль для сериализации и десериализации классов python с возможностью структурного расположения сериализованных классов внутри Json

### Кому пригодиться?
\-
### Примеры
```python
class MyClass:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age


ClassSerializer.serialize(MyClass('Nikita',20),'test.json')

with open('test.json','r') as file:
  print(file.read())

############
'{"name":"Nikita","age":20}'
```
