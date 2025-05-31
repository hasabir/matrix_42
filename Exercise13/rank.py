from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Rank(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:

    def _rank(self) -> int:
        row_echelon_form = self.row_echelon()
        rank = 0
        for row in row_echelon_form.matrix:
            if any(value != 0 for value in row.vec):
                rank += 1
        return rank

    for name, method in [("rank", _rank)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls
