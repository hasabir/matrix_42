from typing import TypeVar, Generic, List, Type

K = TypeVar('K')


def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def row_echelon(self) -> 'Matrix[K]':
        ...
    
    
    if not hasattr(cls, "row_echelon"):
        setattr(cls, "row_echelon", row_echelon)
    
    return cls