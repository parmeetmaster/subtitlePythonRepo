
from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Query:
    source: str
    id: int
    alt: int

    @staticmethod
    def from_dict(obj: Any) -> 'Query':
        assert isinstance(obj, dict)
        source = from_str(obj.get("source"))
        id = int(from_str(obj.get("id")))
        alt = int(from_str(obj.get("alt")))
        return Query(source, id, alt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["source"] = from_str(self.source)
        result["id"] = from_str(str(self.id))
        result["alt"] = from_str(str(self.alt))
        return result


@dataclass
class Source:
    file: str
    label: str
    type: Optional[str] = None
    default: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        file = from_str(obj.get("file"))
        label = from_str(obj.get("label"))
        type = from_union([from_str, from_none], obj.get("type"))
        default = from_union([from_bool, from_none], obj.get("default"))
        return Source(file, label, type, default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file"] = from_str(self.file)
        result["label"] = from_str(self.label)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.default is not None:
            result["default"] = from_union([from_bool, from_none], self.default)
        return result


@dataclass
class DonghuamanModel:
    status: str
    server_time: str
    query: Query
    embed_link: str
    download_link: str
    request_link: str
    title: str
    poster: str
    sources: List[Source]
    tracks: List[Source]

    @staticmethod
    def from_dict(obj: Any) -> 'DonghuamanModel':
        assert isinstance(obj, dict)
        status = from_str(obj.get("status"))
        server_time = from_str(obj.get("server_time"))
        query = Query.from_dict(obj.get("query"))
        embed_link = from_str(obj.get("embed_link"))
        download_link = from_str(obj.get("download_link"))
        request_link = from_str(obj.get("request_link"))
        title = from_str(obj.get("title"))
        poster = from_str(obj.get("poster"))
        sources = from_list(Source.from_dict, obj.get("sources"))
        tracks = from_list(Source.from_dict, obj.get("tracks"))
        return DonghuamanModel(status, server_time, query, embed_link, download_link, request_link, title, poster, sources, tracks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_str(self.status)
        result["server_time"] = from_str(self.server_time)
        result["query"] = to_class(Query, self.query)
        result["embed_link"] = from_str(self.embed_link)
        result["download_link"] = from_str(self.download_link)
        result["request_link"] = from_str(self.request_link)
        result["title"] = from_str(self.title)
        result["poster"] = from_str(self.poster)
        result["sources"] = from_list(lambda x: to_class(Source, x), self.sources)
        result["tracks"] = from_list(lambda x: to_class(Source, x), self.tracks)
        return result


def donghuaman_model_from_dict(s: Any) -> DonghuamanModel:
    return DonghuamanModel.from_dict(s)


def donghuaman_model_to_dict(x: DonghuamanModel) -> Any:
    return to_class(DonghuamanModel, x)
