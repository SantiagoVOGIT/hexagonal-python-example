def utilityClass(cls):
    def __new__(cls, *args, **kwargs):
        raise Exception(f"La clase {cls.__name__} es una clase de utilidad y no debe de ser instanciada.")

    cls.__new__ = __new__
    return cls