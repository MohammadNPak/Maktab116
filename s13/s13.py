
from abc import ABC,abstractmethod

class DuplicateTagNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Tag already exists"

class DuplicateAdsNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Ad already exists"

class DuplicatePlaceNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Place already exists"

class TagNotFoundException(BaseException):
    def __str__(self) -> str:
        return "Error: Tag not found"


class Base:

    objects = []
    last_id=0

    def __init__(self,name) -> None:
        self.name=name
        self.id = None

    @classmethod
    def _get_id(cls):
        cls.last_id+=1
        return cls.last_id
    
    def save(self):
        if self._is_not_duplicate(self.name):
            self.id=self._get_id()
            self.__class__.append_to_objects(self)
        else:
            raise self.duplicate_exception
            # raise DuplicateTagNameException
            # raise Exception("Error: Tag already exists")

    @classmethod
    def append_to_objects(cls,obj):
        cls.objects.append(obj)

    @classmethod
    def _is_not_duplicate(cls,name):
        return name not in [x.name for x in cls.objects]

    def success_message(self):
        return f"Done: {self.__class__.__name__} id is {self.id}"

    @classmethod
    def list(cls):
        return f"{cls.__name__.upper()}s: {' '.join([x.name for x in sorted(cls.objects,key=lambda x:x.id)])}"

    @classmethod
    def exist(cls,names):
        existed_names = [x.name for x in cls.objects]
        for name in names:
            if name not in existed_names:
                return False
        return True


class Tag(Base):
    duplicate_exception = DuplicateTagNameException
    

class AddsPlaceCommon(Base,ABC):

    @abstractmethod
    def get_duplicate_exception(self):
        pass

    def __init__(self, name,cpc,tags) -> None:
        super().__init__(name)
        self.cpc=cpc
        self.tags = tags
    
    def save(self):
        if self._is_not_duplicate(self.name):
            if Tag.exist(self.tags):
                self.id=self._get_id()
                self.__class__.append_to_objects(self)
            else:
                raise TagNotFoundException
        else:
            raise self.get_duplicate_exception()
            # raise DuplicateTagNameException
            # raise Exception("Error: Tag already exists")


class ADS(AddsPlaceCommon):
    duplicate_exception = DuplicateAdsNameException
    def get_duplicate_exception(self):
        return self.duplicate_exception

class Place(AddsPlaceCommon):
    duplicate_exception = DuplicatePlaceNameException
    def get_duplicate_exception(self):
        return self.duplicate_exception

Tag.objects = []
ADS.objects=[]
Place.objects=[]

while True:
    command,*data = input().split() 
    
    # "ADD-TAG -name <name>"
    try:
        if command == "ADD-TAG":
            name=data[1]
            tag = Tag(name=name)
            tag.save()
            print(tag.success_message())
        elif command=="TAG-LIST":
            print(Tag.list())
        
        # "<ADD-ADS -name <name> -cpc <cpc> -tags <tag1> <tag2>"
        elif command == "ADD-ADS":
            name=data[1]
            cpc=data[3]
            tags = data[5:]
            ads = ADS(name,cpc,tags)
            ads.save()
            print(ads.success_message())
        elif command=="ADS-LIST":
            print(ADS.list())

        # "ADD-PLACE -name <name> -cpc <cpc> -tags <tag1> <tag2>"
        elif command=="ADD-PLACE":
            name=data[1]
            cpc=data[3]
            tags = data[5:]
            place = Place(name,cpc,tags)
            place.save()
            print(place.success_message())
        elif command=="PLACE-LIST":
            print(Place.list())

    # except DuplicateAdsNameException as e:
    #     pass
    # except DuplicateTagNameException as e:
    #     pass
    except BaseException as e:
        print(e)