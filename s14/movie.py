from my_exceptions import *
from base_class import Base

class Movie(Base):
    _invalid_id_message :str = "invalid movie id"
    def __init__(self,title,date,quality) -> None:
        super().__init__()
        self.title=title
        self.date=int(date)
        self.quality=quality
        self.casts=[]

    def validate_title(self):
        if len(self.title)<=20:
            return True
        return False
    

    def validate_date(self):
        return 1888<=self.date <=2024

    def validate_quality(self):
        return self.quality in ("720p","1080p" ,"4K")
    
    def validate(self):
        if not self.validate_title():
            raise ValidationException("invalid title")
        if not self.validate_date():
            raise ValidationException("invalid date") 
        if not self.validate_quality():
            raise ValidationException("invalid quality")
        return True
    
    def __str__(self) -> str:
        c = ", ".join([str(x.id) for x in sorted(self.casts,key=lambda y:y.id)])
        return f'{{title:"{self.title}", date:"{self.date}", quality:"{self.quality}", casts:[{c}]}}'

    @classmethod
    def filter(cls,pattern,type="title"):
        if type=="title":
            movies = [x.id for x in cls._objects if x.title.startswith(pattern)]
            movies.sort()
            return movies
        
        elif type=="date":
            ineq,n = pattern.split()
            if ineq == '=':
                ineq="=="
            # eval("2>10")
            movies = [x.id for x in cls._objects if eval(f"{x.date}{ineq}{n}")]
            movies.sort()
            return movies

        elif type=="quality":
            movies = [x.id for x in cls._objects if x.quality == pattern]
            movies.sort()
            return movies
        else:
            raise Exception("invalid type")
    
    def remove_related(self):
        for cast in Cast._objects:
            if self in cast.movies:
                cast.movies.remove(self)
    


class Cast(Base):
    _invalid_id_message :str = "invalid cast id"
    def __init__(self,name) -> None:
        super().__init__()
        self.name :str =name
        self.movies = []

    def validate_name(self):
        if len(self.name)>20:
            return False
        if not self.name.isalpha():
            return False
        return True
    
    def validate(self) -> bool:
        if not self.validate_name():
            raise ValidationException("invalid name")
        return True

    def __str__(self) -> str:
        m = ", ".join([str(x.id) for x in sorted(self.movies,key=lambda y:y.id)])
        return f'{{name:"{self.name}", movies:[{m}]}}'


    def remove_related(self):
        for movie in Movie._objects:
            if self in movie.casts:
                movie.casts.remove(self)

