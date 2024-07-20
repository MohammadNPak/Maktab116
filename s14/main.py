from abc import ABC,abstractmethod
from movie import Movie,Cast
from my_exceptions import *

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
def main():
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
        
if __name__=="__main__":
    main()