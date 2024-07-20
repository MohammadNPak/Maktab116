class InvalidIdException(BaseException):
    pass

class ValidationException(BaseException):
    pass

class AlreadyLinked(BaseException):
    def __str__(self) -> str:
        return "already linked"