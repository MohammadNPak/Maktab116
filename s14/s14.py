
from abc import ABC,abstractmethod
# type hint

class InvalidIdException(BaseException):
    pass

class ValidationException(BaseException):
    pass

class AlreadyLinked(BaseException):
    def __str__(self) -> str:
        return "already linked"

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

    @classmethod
    def remove(cls,id):
        obj = cls.get(id)
        cls._objects.remove(obj)
        return f"removed successfully {obj.id}"
    

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


def link_cast_to_movie(cast_id,movie_id):
    cast:Cast = Cast.get(cast_id)
    movie: Movie =Movie.get(movie_id)
    if movie in cast.movies or cast in movie.casts:
        raise AlreadyLinked
    cast.movies.append(movie)
    movie.casts.append(cast)
    return f"successfully linked {cast.id} to {movie.id}"

Movie.initiate_objects([])
Cast.initiate_objects([])

# ADD-MOVIE <title> <date> <quality>
# REM-MOVIE <movie-id>
# ADD-CAST <name>
# REM-CAST <cast-id>
# SHOW-MOVIE <movie-id>
# SHOW-CAST <cast-id>
# LINK-CAST-TO-MOVIE <cast-id> <movie-id>
# FILTER-MOVIES-BY-TITLE <pattern>
# FILTER-MOVIES-BY-DATE <ineq> <n>
# FILTER-MOVIES-BY-QUALITY <pattern>

n = int(input())
for _ in range(n):
    command,*data=input().split()
    try:
        if command=="ADD-MOVIE":
            movie = Movie(*data)
            print(movie.save())
        elif command =="REM-MOVIE":
            movie_id = int(data[0])
            print(Movie.remove(movie_id))
        elif command=="ADD-CAST":
            cast = Cast(name=data[0])
            print(cast.save())
        elif command=="REM-CAST":
            cast_id = int(data[0])
            print(Cast.remove(cast_id))
        elif command=="SHOW-MOVIE":
            print(Movie.get(int(data[0])))
        elif command=="SHOW-CAST":
            print(Cast.get(int(data[0])))
        elif command=="LINK-CAST-TO-MOVIE":
            cast_id=int(data[0])
            movie_id=int(data[1])
            print(link_cast_to_movie(cast_id,movie_id))
        elif command=="FILTER-MOVIES-BY-TITLE":
            pattern = data[0]
            print(Movie.filter(pattern,type="title"))
        elif command == "FILTER-MOVIES-BY-DATE":
            pattern = data[0]+" "+data[1]
            print(Movie.filter(pattern,type="date"))
        elif command=="FILTER-MOVIES-BY-QUALITY":
            pattern =data[0]
            print(Movie.filter(pattern,type="quality"))

    except BaseException as e:
        print(e)
    except Exception as e:
        print(e)