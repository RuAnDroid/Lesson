import os
import json
import requests
import dataclasses
import typing
from pprint import pprint

# email = os.environ['email']
# password = os.environ['password']
email = input('ВВедите адрес почты:')
password = input('Введите пароль:')
URL = "https://jang.xpech.ru/api/users/auth-via-email"
x = requests.Session()
res = x.post(URL, json={"email": email, "password": password})
pprint(res.json())

URL2 = "https://jang.xpech.ru/api/collections/python21_pets_auth/records"
y = requests.Session()

res2 = y.post(URL2, )
pprint(res2.json())


@dataclasses.dataclass
class petInfo:
    _name: str
    _type: typing.List[str]
    species: str
    ID_User: str

    class petInfoDecoder(json.JSONDecoder):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, object_hook=self.object_hook, **kwargs)

        def object_hook(self, obj):
            return petInfo(obj["_name"], obj["_type"], obj["species"],
                           obj["ID_User"])


class petInfoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, petInfo):
            return {
                "name": obj._name,
                "_type": obj._type,
                "species": obj.species,
                "userId": obj.ID_User
            }