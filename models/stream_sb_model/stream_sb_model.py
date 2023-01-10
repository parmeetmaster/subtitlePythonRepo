# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = stream_sb_model_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Dict, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Logo:
    hide: bool
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Logo':
        assert isinstance(obj, dict)
        hide = from_stringified_bool(from_str(obj.get("hide")))
        url = from_str(obj.get("url"))
        return Logo(hide, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hide"] = from_str(str(self.hide).lower())
        result["url"] = from_str(self.url)
        return result


@dataclass
class Sub:
    file: str
    label: str

    @staticmethod
    def from_dict(obj: Any) -> 'Sub':
        assert isinstance(obj, dict)
        file = from_str(obj.get("file"))
        label = from_str(obj.get("label"))
        return Sub(file, label)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file"] = from_str(self.file)
        result["label"] = from_str(self.label)
        return result


@dataclass
class StreamData:
    logo: Logo
    hash: str
    backup: str
    country: str
    qlabel: Dict[str, str]
    file: str
    cdn_img: str
    subs: List[Sub]
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'StreamData':
        assert isinstance(obj, dict)
        logo = Logo.from_dict(obj.get("logo"))
        hash = from_str(obj.get("hash"))
        backup = from_str(obj.get("backup"))
        country = from_str(obj.get("country"))
        qlabel = from_dict(from_str, obj.get("qlabel"))
        file = from_str(obj.get("file"))
        cdn_img = from_str(obj.get("cdn_img"))
        subs = from_list(Sub.from_dict, obj.get("subs"))
        title = from_str(obj.get("title"))
        return StreamData(logo, hash, backup, country, qlabel, file, cdn_img, subs, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["logo"] = to_class(Logo, self.logo)
        result["hash"] = from_str(self.hash)
        result["backup"] = from_str(self.backup)
        result["country"] = from_str(self.country)
        result["qlabel"] = from_dict(from_str, self.qlabel)
        result["file"] = from_str(self.file)
        result["cdn_img"] = from_str(self.cdn_img)
        result["length"] = from_int(self.length)
        result["id"] = from_int(self.id)
        result["subs"] = from_list(lambda x: to_class(Sub, x), self.subs)
        result["title"] = from_str(self.title)
        return result


@dataclass
class UserData:
    id: int
    adb: int
    adss: int
    dlp3: int
    uam: int
    dmlg: str
    uew: int
    ua: int
    uas: List[Any]
    pr: int
    ulp: str
    uet: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserData':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        adb = from_int(obj.get("adb"))
        adss = int(from_str(obj.get("adss")))
        dlp3 = from_int(obj.get("dlp3"))
        uam = from_int(obj.get("uam"))
        dmlg = from_str(obj.get("dmlg"))
        uew = from_int(obj.get("uew"))
        ua = from_int(obj.get("ua"))
        uas = from_list(lambda x: x, obj.get("uas"))
        pr = from_int(obj.get("pr"))
        ulp = from_str(obj.get("ulp"))
        uet = from_int(obj.get("uet"))
        return UserData(id, adb, adss, dlp3, uam, dmlg, uew, ua, uas, pr, ulp, uet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["adb"] = from_int(self.adb)
        result["adss"] = from_str(str(self.adss))
        result["dlp3"] = from_int(self.dlp3)
        result["uam"] = from_int(self.uam)
        result["dmlg"] = from_str(self.dmlg)
        result["uew"] = from_int(self.uew)
        result["ua"] = from_int(self.ua)
        result["uas"] = from_list(lambda x: x, self.uas)
        result["pr"] = from_int(self.pr)
        result["ulp"] = from_str(self.ulp)
        result["uet"] = from_int(self.uet)
        return result


@dataclass
class StreamSbModel:
    status_code: int
    user_data: UserData
    stream_data: StreamData

    @staticmethod
    def from_dict(obj: Any) -> 'StreamSbModel':
        assert isinstance(obj, dict)
        status_code = from_int(obj.get("status_code"))
        user_data = UserData.from_dict(obj.get("user_data"))
        stream_data = StreamData.from_dict(obj.get("stream_data"))
        return StreamSbModel(status_code, user_data, stream_data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status_code"] = from_int(self.status_code)
        result["user_data"] = to_class(UserData, self.user_data)
        result["stream_data"] = to_class(StreamData, self.stream_data)
        return result


def stream_sb_model_from_dict(s: Any) -> StreamSbModel:
    return StreamSbModel.from_dict(s)


def stream_sb_model_to_dict(x: StreamSbModel) -> Any:
    return to_class(StreamSbModel, x)
