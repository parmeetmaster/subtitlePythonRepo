from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Track:
    file: str
    label: str
    default: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Track':
        assert isinstance(obj, dict)
        file = from_str(obj.get("file"))
        label = from_str(obj.get("label"))
        default = from_union([from_bool, from_none], obj.get("default"))
        return Track(file, label, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file"] = from_str(self.file)
        result["label"] = from_str(self.label)
        if self.default is not None:
            result["default"] = from_union([from_bool, from_none], self.default)
        return result


@dataclass
class DongManModel:
    title: str
    poster: str
    tracks: List[Track]

    @staticmethod
    def from_dict(obj: Any) -> 'DongManModel':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        poster = from_str(obj.get("poster"))
        tracks = from_list(Track.from_dict, obj.get("tracks"))
        return DongManModel(title, poster, tracks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["poster"] = from_str(self.poster)
        result["tracks"] = from_list(lambda x: to_class(Track, x), self.tracks)
        return result


def dong_man_model_from_dict(s: Any) -> DongManModel:
    return DongManModel.from_dict(s)


def dong_man_model_to_dict(x: DongManModel) -> Any:
    return to_class(DongManModel, x)
