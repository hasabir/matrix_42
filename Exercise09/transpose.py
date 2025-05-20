from typing import TypeVar, Type

K = TypeVar('K')


def Transpose(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def transpose(self) -> 'Matrix[K]':
        return cls(self.get_columns())

    if not hasattr(cls, "transpose"):
        setattr(cls, "transpose", transpose)
    return cls