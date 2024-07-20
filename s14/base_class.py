from abc import ABC,abstractmethod
from my_exceptions import *

class Base(ABC):

    _objects: list = None
    _last_id: int = 0
    _invalid_id_message :str = "" 

    def __init__(self) -> None:
        self.id = None

    @abstractmethod
    def validate(self) -> bool:
        pass
    
    @classmethod
    def initiate_objects(cls,objects):
        cls._objects = objects
    
    def save(self) -> None:
        if self.validate():
            self.id = self._get_id()
            self._append_objects(self)
        return f"added successfully {self.id}"
    
    @classmethod
    def _get_id(cls):
        id = cls._last_id
        cls._last_id+=1
        return id

    @classmethod
    def _append_objects(cls,obj):
        cls._objects.append(obj)
    
    @classmethod
    def get(cls,id):
        for obj in cls._objects:
            if obj.id==id:
                return obj
        raise InvalidIdException(cls._invalid_id_message)

    @abstractmethod
    def remove_related(self):
        pass

    @classmethod
    def remove(cls,id):
        obj = cls.get(id)
        obj.remove_related()
        cls._objects.remove(obj)
        return f"removed successfully {obj.id}"
    
