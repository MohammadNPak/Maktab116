from abc import abstractmethod,ABC
import re
import argparse
from argparse import Action
from enum import Enum
from typing import Self


class TimeTypeEnum(Enum):
    FULLTIME = 0
    PARTTIME = 1
    PROJECT = 2


class InvalidNameException(BaseException):
    def __str__(self) -> str:
        return 'invalid name'


class InvalidAgeExcepion(BaseException):
    pass


class InvalidTimeTypeException(BaseException):
    def __str__(self) -> str:
        return f'invalid timetype'


class InvalidSalaryException(BaseException):
    def __str__(self) -> str:
        return f"invalid salary"


class InvalidIndexExcetption(BaseException):
    pass


class RepeatedSkillException(BaseException):
    def __str__(self) -> str:
        return 'repeated skill'


def validate_name(name: str) -> str:
    if re.match(r'^[a-zA-Z]{1,10}$', name) is None:
        raise InvalidNameException('invalid name')
    return name


class AgeIntervalValidationAction(Action):
    def __call__(self,
                 parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace,
                 values: str | None,
                 option_string: str | None = None) -> None:

        age = int(values)
        if not 0 <= age <= 200:
            raise InvalidAgeExcepion('invalid age interval')
        if self.dest == "maxage" and age < namespace.minage:
            raise InvalidAgeExcepion('invalid age interval')
        setattr(namespace, self.dest, age)


def validate_time_type(time_type: str) -> TimeTypeEnum:
    if time_type not in TimeTypeEnum.__members__:
        raise InvalidTimeTypeException
    return TimeTypeEnum[time_type]


def validate_salary(salary: str) -> int:
    salary = int(salary)
    if not 0 <= salary < 1_000_000_000 or salary % 1000 != 0:
        raise InvalidSalaryException
    return salary


def validate_age(age: str) -> int:
    age = int(age)
    if not 0 <= age <= 200:
        raise InvalidAgeExcepion('invalid age')
    return age


class UtilitiesMixin:

    @classmethod
    def all(cls):
        return cls._objects

    @classmethod
    def exist(cls, id: str | int) -> bool:
        if not id in cls._objects:
            raise InvalidIndexExcetption(cls._invalid_index_message)
        return True

    @classmethod
    def get(cls, id):
        if cls.exist(id):
            return cls.all()[id]


class Skills(UtilitiesMixin,ABC):
    _objects: list[str] = []
    _skills: Self | None = None
    __is_initialized:bool = False
    _invalid_index_message = 'invalid skill'


    def __new__(cls, *args, **kwargs) -> Self:
        if cls._skills is None:
            cls._skills = super().__new__(cls)
            cls.__is_initialized=False
        return cls._skills

    def __init__(self, values:list[str]) -> None:
        if not self.__is_initialized:
            self.__class__._objects = values
            self.__class__.__is_initialized=True


class Base:

    _objects: dict[int, Self] | None = None
    _last_id: int = 0

    def __init__(
            self, name: str,
            age: int | tuple[int, int],
            time_type: TimeTypeEnum,
            salary: int) -> None:

        self.id: int | None = None
        self.name = name
        self.age = age
        self.time_type = time_type
        self.salary = salary
        self.skills: set[str] = set()
        self.views: list['Base'] = []

    @classmethod
    def init_cls_vars(cls):
        cls._objects = dict()

    def save(self) -> str:
        id = self.get_last_id()
        id += 1
        self.id = id
        self.set_last_id(id)
        self._objects.update({id: self})
        return f'{self.__class__.__name__.lower()} id is {self.id}'

    @classmethod
    def set_last_id(cls, value):
        cls._last_id = value

    @classmethod
    def get_last_id(cls):
        return cls._last_id

    def add_skill(self, skill: str) -> None:
        if Skills.exist(skill):
            if skill in self.skills:
                raise RepeatedSkillException
            self.skills.add(skill)
            return f'skill added'


    def add_view(self, viewer: 'Base') -> None:
        self.views.append(viewer)


class StatusParameterMixin:

    def set_status_param(self) -> list[str]:
        skills_views: list[tuple[str, int]] = list(map(
            lambda x: (x, len([y for y in self.views if x in y.skills])), self.skills))
        skills_views.sort(key=lambda x: (x[1], x[0]))
        return [f'({x[0]},{x[1]})' for x in skills_views]


class Job(UtilitiesMixin,StatusParameterMixin, Base):
    _invalid_index_message = 'invalid index'
    
    def status(self) -> str:
        return f"{self.name}-{len(self.views)}-{''.join(self.set_status_param())}"


class User(UtilitiesMixin,StatusParameterMixin, Base):
    _invalid_index_message = 'invalid index'

    def status(self) -> str:
        return f"{self.name}-{''.join(self.set_status_param())}"

    def get_job_list(self):
        suggested_jobs = [(x.id, self.__get_score(x))
                      for x in Job.all().values()]
        suggested_jobs.sort(key=lambda x:(x[1],x[0]),reverse=True)
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
        score = int(score*1000+job.id)
        return score



def add_job(name, minage, maxage, time_type, salary, **kwargs):
    job = Job(name, (minage, maxage), time_type, salary)
    message = job.save()
    print(message)


def add_user(name, age, time_type, salary, **kwargs):
    user = User(name, age, time_type, salary)
    message = user.save()
    print(message)


def add_job_skill(job_id: int, skill: str,**kwargs):
    job: Job = Job.get(job_id)
    message = job.add_skill(skill)
    print(message)


def add_user_skill(user_id: int, skill: str,**kwargs):
    user = User.get(user_id)
    message = user.add_skill(skill)
    print(message)


def view(user_id,job_id,**kwargs):
    user = User.get(user_id)
    job = Job.get(job_id)
    user.add_view(job)
    job.add_view(user)
    print('tracked')


def job_status(job_id,**kwargs):
    job = Job.get(job_id)
    print(job.status())


def user_status(user_id,**kwargs):
    user = User.get(user_id)
    print(user.status())


def get_job_list(user_id,**kwargs):
    user = User.get(user_id)
    print(user.get_job_list())



def main():
    # ADD-JOB <NAME> <MINAGE> <MAXAGE> <FULLTIME|PARTTIME|PROJECT> <SALARY>
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    add_job_subparser = subparser.add_parser('ADD-JOB')
    add_job_subparser.add_argument('name', type=validate_name)
    add_job_subparser.add_argument(
        'minage', type=int, action=AgeIntervalValidationAction)
    add_job_subparser.add_argument(
        'maxage', type=int, action=AgeIntervalValidationAction)
    add_job_subparser.add_argument('time_type', type=validate_time_type)
    add_job_subparser.add_argument('salary', type=validate_salary)
    add_job_subparser.set_defaults(func=add_job)

    # ADD-USER <NAME> <AGE> <FULLTIME|PARTTIME|PROJECT> <SALARY>
    add_user_subparser = subparser.add_parser('ADD-USER')
    add_user_subparser.add_argument('name', type=validate_name)
    add_user_subparser.add_argument('age', type=validate_age)
    add_user_subparser.add_argument('time_type', type=validate_time_type)
    add_user_subparser.add_argument('salary', type=validate_salary)
    add_user_subparser.set_defaults(func=add_user)

    # ADD-JOB-SKILL <JOB-ID> <SKILL>
    add_job_skill_subparser = subparser.add_parser('ADD-JOB-SKILL')
    add_job_skill_subparser.add_argument('job_id', type=int)
    add_job_skill_subparser.add_argument('skill', type=str)
    add_job_skill_subparser.set_defaults(func=add_job_skill)

    # ADD-USER-SKILL <USER-ID> <SKILL>
    add_user_skill_subparser = subparser.add_parser('ADD-USER-SKILL')
    add_user_skill_subparser.add_argument('user_id', type=int)
    add_user_skill_subparser.add_argument('skill', type=str)
    add_user_skill_subparser.set_defaults(func=add_user_skill)

    # VIEW <USER-ID> <JOB-ID>

    view_parser = subparser.add_parser('VIEW')
    view_parser.add_argument('user_id', type=int)
    view_parser.add_argument('job_id', type=int)
    view_parser.set_defaults(func=view)
  
    # JOB-STATUS <JOB-ID>
    job_staus_parser = subparser.add_parser('JOB-STATUS')
    job_staus_parser.add_argument('job_id', type=int)
    job_staus_parser.set_defaults(func=job_status)
    

    # USER-STATUS <USER-ID>
    usr_satus_parser = subparser.add_parser('USER-STATUS')
    usr_satus_parser.add_argument('user_id', type=int)
    usr_satus_parser.set_defaults(func=user_status)
    
    # GET-JOBLIST <USER-ID>
 
    usr_satus_parser = subparser.add_parser('GET-JOBLIST')
    usr_satus_parser.add_argument('user_id', type=int)
    usr_satus_parser.set_defaults(func=get_job_list)


    s = int(input())
    skills = Skills(input().split())
    q = int(input())
    User.init_cls_vars()
    Job.init_cls_vars()

    for _ in range(q):
        try:
            args = parser.parse_args(input().split())
            args.func(**vars(args))
        # except Exception as e:
        #     raise e
        except BaseException as e:
            print(e)


if __name__ == "__main__":
    main()
