import re
import argparse
from typing import ClassVar, Optional, Self, Iterable
from enum import Enum
from math import floor


class InvalidNameException(BaseException):
    def __str__(self) -> str:
        return "invalid name"


class InvalidAgeException(BaseException):
    def __str__(self) -> str:
        return f"invalid age interval"


class InvalidTimveTypeException(BaseException):
    def __str__(self) -> str:
        return f"invalid timetype"


class InvalidSalaryException(BaseException):
    def __str__(self) -> str:
        return f"invalid salary"


class InvalidIndexException(BaseException):
    def __str__(self) -> str:
        return "invalid index"


class InvalidSkill(BaseException):
    def __str__(self) -> str:
        return "invalid skill"


class RepeatedSkill(BaseException):
    def __str__(self) -> str:
        return "repeated skill"


class TimeTypeEnum(Enum):
    FULLTIME = 1
    PARTTIME = 2
    PROJECT = 3


class NameValidation(argparse.Action):
    def __call__(self,
                 parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace,
                 values: str | None,
                 option_string: str | None = None) -> None:
        result = re.match(r'^[A-Za-z]{1,10}$', values)
        if result is None:
            # parser.error(f"invalid name")
            # raise argparse.ArgumentError(self,"invalid name")
            raise InvalidNameException
        setattr(namespace, self.dest, values)


class AgeValidation(argparse.Action):
    def __call__(self,
                 parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace,
                 values: str | None,
                 option_string: str | None = None) -> None:

        if not 0 <= float(values) <= 200:
            raise InvalidAgeException
        setattr(namespace, self.dest, values)


class TimeTypeValidation(argparse.Action):
    def __call__(self,
                 parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace,
                 values: str | None,
                 option_string: str | None = None) -> None:

        try:
            a = TimeTypeEnum[values]
        except KeyError:
            raise InvalidTimveTypeException
        setattr(namespace, self.dest, values)


class SalaryValidation(argparse.Action):
    def __call__(self,
                 parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace,
                 values: str | None,
                 option_string: str | None = None) -> None:
        salary = int(values)
        if salary < 0 or salary % 1000 != 0:
            raise InvalidSalaryException
        # if not values in ("FULLTIME","PARTTIME","PROJECT"):
        setattr(namespace, self.dest, values)




skills_set: set[str]


class BaseClass:
    _objects: ClassVar[list['BaseClass']]
    _last_id: int

    def __init__(self,
                 name: str,
                 age: int | tuple[int, int],
                 time_type: str,
                 salary: float) -> None:

        self.name = name
        self.age = age
        self.time_type: TimeTypeEnum = TimeTypeEnum(time_type)
        self.salary = salary
        self.id: Optional[int] = None
        self.skills: set[str] = set()
        self.views: list['BaseClass'] = []

    @classmethod
    def get_last_id(cls) -> int:
        return cls._last_id

    @classmethod
    def set_last_id(cls, id: int) -> None:
        cls._last_id = id

    @classmethod
    def append_to_objects(cls, obj: Self) -> None:
        cls._objects.append(obj)

    @classmethod
    def get_all_objects(cls) -> list[Self]:
        return cls._objects

    @classmethod
    def get(cls, id: int) -> Self:
        for obj in Self.get_all_objects():
            if obj.id == id:
                return obj
        raise InvalidIndexException

    def save(self) -> str:
        self.id = self.get_last_id()
        self.append_to_objects(self)
        self.set_last_id(self.id+1)
        return f'{self.__class__.__name__.lower()} id is {self.id}'

    def add_skill(self, skill: str) -> str:
        if skill not in skills_set:
            raise InvalidSkill
        if skill in self.skills:
            raise RepeatedSkill
        self.skills.update(skill)
        return f"skill added"

    def add_view(self, viewer: 'BaseClass') -> None:
        self.views.append(viewer)


class StatusParameterMixin:

    def set_status_param(self) -> list[str]:
        skils_views: list[tuple[str, int]] = list(map(
            lambda x: (x, len([y for y in self.views if x in y.skills])), self.skills))
        skils_views.sort(key=lambda x: (x[1], x[0]))
        skils_views_str: list[str] = [f'({x[0]},{x[1]})' for x in skils_views]
        return skils_views_str


class Job(StatusParameterMixin, BaseClass,):
    def status(self) -> str:
        return f"{self.name}-{len(self.views)}-{''.join(self.set_status_param())}"


class User(StatusParameterMixin, BaseClass):
    def status(self) -> str:
        return f"{self.name}-{''.join(self.set_status_param())}"

    def get_job_list(self):
        suggested_jobs = [(x.id, self.get_score(x))
                      for x in Job.get_all_objects()]
        suggested_jobs.sort(key=lambda x:x[1])
        suggested_jobs = [f'({x[0]},{x[1]})' for x in suggested_jobs]
        suggested_jobs = ''.join(suggested_jobs)
        return suggested_jobs
    
    def __age_score(self, l: int, r: int):
        x = self.age
        if x < l:
            return x-l
        elif x > r:
            return r-x
        else:
            return min(r-x, x-l)

    def __skills_score(self, B: set[str]):
        A: set[str] = self.skills
        return 3*len(A.intersection(B))-len(B-A)

    def __time_type_score(self, job_time_type: str) -> int:
        user_time_type: TimeTypeEnum = self.time_type

        if user_time_type == job_time_type:
            return 10
        elif user_time_type == TimeTypeEnum.FULLTIME and job_time_type == TimeTypeEnum.PROJECT:
            return 4
        elif job_time_type == TimeTypeEnum.FULLTIME and user_time_type == TimeTypeEnum.PROJECT:
            return 4
        else:
            return 5

    def __salary_score(self, y: int) -> int:
        x: int = self.salary
        return 1000//(max(abs(x-y), 1))

    def __get_score(self, job: Job) -> int:
        score: int = 0
        score += self.__age_score(*job.age)
        score += self.__skills_score(job.skills)
        score += self.__time_type_score(job.time_type)
        score += self.__salary_score(job.salary)
        score = score*1000+job.id
        return score


def view(user_id, job_id) -> str:
    user = User.get(user_id)
    job = Job.get(job_id)
    user.add_view(job)
    job.add_view(user)
    return 'tracked'



def add_job(name,minage,maxage,time_type,salary,**kwargs):
    print(name,minage,maxage,time_type,salary)

def add_user(name,age,time_type,salary,**kwargs):
    print(name,age,time_type,salary)

def add_job_skill(job_id,skill,**kwargs):
    pass

def add_user_skill(user_id,skill,**kwargs):
    pass

def view(user_id,job_id,**kwargs):
    pass

def job_status(job_id,**kwargs):
    pass

def user_status(user_id,**kwargs):
    pass

def get_job_list(user_id,**kwargs):
    pass


def get_parser():
    arg_parser = argparse.ArgumentParser()
    subparser = arg_parser.add_subparsers()
    
    # ADD-JOB <NAME> <MINAGE> <MAXAGE> <FULLTIME|PARTTIME|PROJECT> <SALARY>
    add_job_parser = subparser.add_parser('ADD-JOB')
    add_job_parser.add_argument('name', action=NameValidation, type=str)
    add_job_parser.add_argument('minage', action=AgeValidation, type=float)
    add_job_parser.add_argument('maxage', action=AgeValidation, type=float)
    add_job_parser.add_argument('time_type', action=TimeTypeValidation, type=str)
    add_job_parser.add_argument('salary', action=SalaryValidation, type=str)
    add_job_parser.set_defaults(func=add_job)

    # ADD-USER <NAME> <AGE> <FULLTIME|PARTTIME|PROJECT> <SALARY>
 
    add_user_parser = subparser.add_parser('ADD-USER')
    add_user_parser.add_argument('name', action=NameValidation, type=str)
    add_user_parser.add_argument('age', action=AgeValidation, type=int)
    add_user_parser.add_argument('time_type', action=TimeTypeValidation, type=str)
    add_user_parser.add_argument('salary', action=SalaryValidation, type=int)
    add_user_parser.set_defaults(func=add_user)

    # ADD-JOB-SKILL <JOB-ID> <SKILL>

    add_job_skill_parser = subparser.add_parser('ADD-JOB-SKILL')
    add_job_skill_parser.add_argument('job_id', type=int)
    add_job_skill_parser.add_argument('skill', type=str)
    add_job_skill_parser.set_defaults(func=add_job_skill)

    # ADD-USER-SKILL <USER-ID> <SKILL>

    add_user_skill_parser = subparser.add_parser('ADD-USER-SKILL')
    add_user_skill_parser.add_argument('user_id', type=int)
    add_user_skill_parser.add_argument('skill', type=str)
    add_user_skill_parser.set_defaults(func=add_user_skill)


    # VIEW <USER-ID> <JOB-ID>

    view_parser = subparser.add_parser('VIEW')
    view_parser.add_argument('user_id', type=int)
    view_parser.add_argument('job_id', type=int)
    view_parser.set_defaults(func=view)
  
    # JOB-STATUS <JOB-ID>
 
    job_staus_parser = subparser.add_parser('JOB-STATUS')
    job_staus_parser.add_argument('user_id', type=int)
    job_staus_parser.set_defaults(func=job_status)
    

    # USER-STATUS <USER-ID>
    usr_satus_parser = subparser.add_parser('USER-STATUS')
    usr_satus_parser.add_argument('user_id', type=int)
    usr_satus_parser.set_defaults(func=user_status)
    
    # GET-JOBLIST <USER-ID>
 
    usr_satus_parser = subparser.add_parser('GET-JOBLIST')
    usr_satus_parser.add_argument('user_id', type=int)
    usr_satus_parser.set_defaults(func=get_job_list)

    return arg_parser


if __name__=="__main__":
    s = int(input())
    skills_set = set(input().split())
    q = int(input())
    parser = get_parser()
    for _ in range(q):    
        try:
            args = parser.parse_args(input().split()) 
            args.func(**vars(args))

        except BaseException as e:
            print(e)