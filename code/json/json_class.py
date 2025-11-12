
import json

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = person('Max','21')

def encode(o):
    if isinstance(o, person):
        return {"name": o.name, "age": o.age}
    else:
        raise TypeError("Object is not serializable")

json_load = json.dumps(user, default=encode)
print(json_load)