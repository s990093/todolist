class BaseError(Exception):
    def __init__(self, code: int):
        self.code = code
      
        super().__init__(str(code))

    def __str__(self):
        return f'{self.code} - '

class WindowError(BaseError):
    pass