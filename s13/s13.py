
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

class PlaceDoesNotExist(BaseException):
    def __str__(self) -> str:
        return "Error: Place not found"

class AdsDoesNotExist(BaseException):
    def __str__(self) -> str:
        return "Error: Ads not found"

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
    


    @classmethod
    def append_to_objects(cls,obj):
        cls.objects.append(obj)

    @classmethod
    def _is_not_duplicate(cls,name):
        return name not in [x.name for x in cls.objects]

    def success_message(self):
        return f"Done: {self.__class__.__name__.title()} id is {self.id}"

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


class SimpleSaveMixin:
    def save(self):
        if self._is_not_duplicate(self.name):
            self.id=self._get_id()
            self.__class__.append_to_objects(self)
        else:
            raise self.duplicate_exception
            # raise DuplicateTagNameException
            # raise Exception("Error: Tag already exists")

class ComplexSaveMixin:
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



class Tag(SimpleSaveMixin,Base):
    duplicate_exception = DuplicateTagNameException
    

class AddsPlaceCommon(Base,ABC):

    @abstractmethod
    def get_duplicate_exception(self):
        pass

    def __init__(self, name,cpc,tags) -> None:
        super().__init__(name)
        self.cpc=cpc
        self.tags = tags
    
    

    @classmethod
    def get(cls,id):
        for obj in cls.objects:
            if obj.id==id:
                return obj
        raise cls.does_not_exist_exception

    def suggest(self):
        ids = map(lambda z:str(z[0]),
                  sorted([(x.id,self.proper(x.cpc,self.cpc,x.tags,self.tags)
                 ) for x in self.suggest_objects.objects],key=lambda y:y[1],
                 reverse=True))
        return f"SUGGEST-{self.suggest_objects.__name__.upper()}: {' '.join(list(ids))}"

    @staticmethod
    def proper(cpci,cpcj,tagsi,tagsj):
        tagsi=set(tagsi)
        tagsj=set(tagsj)
        common = len(tagsj.intersection(tagsi))
        diff = len(tagsi-tagsj)
        return 1/max(1,cpci-cpcj)*(common-diff)
        


class ADS(ComplexSaveMixin,AddsPlaceCommon):
    duplicate_exception = DuplicateAdsNameException
    does_not_exist_exception = AdsDoesNotExist
    suggest_objects = None
    def get_duplicate_exception(self):
        return self.duplicate_exception

class Place(ComplexSaveMixin,AddsPlaceCommon):
    duplicate_exception = DuplicatePlaceNameException
    does_not_exist_exception = PlaceDoesNotExist
    suggest_objects = ADS
    def get_duplicate_exception(self):
        return self.duplicate_exception


def match(place_id,ads_id):
    ad=ADS.get(ads_id)
    place=Place.get(place_id)
    ADS.objects.remove(ad)
    Place.objects.remove(place)
    return f"Done: {ad.id} matched to {place.id}"

Tag.objects = []
ADS.objects=[]
ADS.suggest_objects=Place
Place.objects=[]

t = int(input())
for _ in range(t):
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
            cpc=int(data[3])
            tags = data[5:]
            ads = ADS(name,cpc,tags)
            ads.save()
            print(ads.success_message())
        elif command=="ADS-LIST":
            print(ADS.list())

        # "ADD-PLACE -name <name> -cpc <cpc> -tags <tag1> <tag2>"
        elif command=="ADD-PLACE":
            name=data[1]
            cpc=int(data[3])
            tags = data[5:]
            place = Place(name,cpc,tags)
            place.save()
            print(place.success_message())
        elif command=="PLACE-LIST":
            print(Place.list())
        
        # SUGGEST-ADS -id <id>
        elif command=="SUGGEST-ADS":
            id = int(data[1])
            place = Place.get(id)
            print(place.suggest())
        
        # SUGGEST-PLACE -id <id>
        elif command=="SUGGEST-PLACE":
            id = int(data[1])
            ads = ADS.get(id)
            print(ads.suggest())
        
        # MATCH -ads-id <adds-id> -place-id <place-id>
        elif command== "MATCH":
            print(match(ads_id=int(data[1]),place_id=int(data[3])))

    except DuplicateTagNameException as e:
        print(e)
    except DuplicateAdsNameException as e:
        print(e)
    except DuplicatePlaceNameException as e:
        print(e)
    except TagNotFoundException as e:
        print(e)
    except PlaceDoesNotExist as e:
        print(e)
    except AdsDoesNotExist as e:
        print(e)
