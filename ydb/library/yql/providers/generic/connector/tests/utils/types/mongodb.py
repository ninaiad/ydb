import abc


class Type(abc.ABC):
    @abc.abstractmethod
    def to_sql(self) -> str:
        pass


class PrimitiveType(Type):
    def to_sql(self):
        return type(self).__name__


class Boolean(PrimitiveType):
    pass


class Int32(PrimitiveType):
    pass


class Int64(PrimitiveType):
    pass


class Double(PrimitiveType):
    pass


class Binary(PrimitiveType):
    pass


class String(PrimitiveType):
    pass


class ObjectId(PrimitiveType):
    pass
