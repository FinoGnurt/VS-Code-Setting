from collections.abc import Iterable
from typing import SupportsIndex, TypeVar, overload
from typing_extensions import Self, TypeAlias

_T = TypeVar("_T")

class BarrelList(list[_T]):
    lists: list[list[_T]]
    @overload
    def __init__(self, iterable: None = None) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def insert(self, index: SupportsIndex, item: _T) -> None: ...
    def append(self, item: _T) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def pop(self, *a) -> _T: ...
    def iter_slice(self, start: int, stop: int, step: int | None = None) -> Iterable[_T]: ...
    def del_slice(self, start: int, stop: int, step: int | None = None) -> None: ...
    __delslice__ = del_slice
    @classmethod
    def from_iterable(cls, it: Iterable[_T]) -> Self: ...
    def __getslice__(self, start: int, stop: int): ...
    def __setslice__(self, start: int, stop: int, sequence: int) -> None: ...
    def sort(self) -> None: ...  # type: ignore[override]
    def reverse(self) -> None: ...
    def count(self, item: _T) -> int: ...
    def index(self, item: _T) -> int: ...  # type: ignore[override]

BList: TypeAlias = BarrelList[_T]

class SplayList(list[_T]):
    def shift(self, item_index: int, dest_index: int = 0) -> None: ...
    def swap(self, item_index: int, dest_index: int) -> None: ...