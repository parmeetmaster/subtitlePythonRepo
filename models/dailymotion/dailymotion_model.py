from typing import Any, List, Dict, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class Info:
    enable: bool

    def __init__(self, enable: bool) -> None:
        self.enable = enable

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        assert isinstance(obj, dict)
        enable = from_bool(obj.get("enable"))
        return Info(enable)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enable"] = from_bool(self.enable)
        return result


class Advertising:
    ad_url: str
    ad_error_url: str
    ad_sync_script_url: str
    ima: Info

    def __init__(self, ad_url: str, ad_error_url: str, ad_sync_script_url: str, ima: Info) -> None:
        self.ad_url = ad_url
        self.ad_error_url = ad_error_url
        self.ad_sync_script_url = ad_sync_script_url
        self.ima = ima

    @staticmethod
    def from_dict(obj: Any) -> 'Advertising':
        assert isinstance(obj, dict)
        ad_url = from_str(obj.get("ad_url"))
        ad_error_url = from_str(obj.get("ad_error_url"))
        ad_sync_script_url = from_str(obj.get("ad_sync_script_url"))
        ima = Info.from_dict(obj.get("ima"))
        return Advertising(ad_url, ad_error_url, ad_sync_script_url, ima)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ad_url"] = from_str(self.ad_url)
        result["ad_error_url"] = from_str(self.ad_error_url)
        result["ad_sync_script_url"] = from_str(self.ad_sync_script_url)
        result["ima"] = to_class(Info, self.ima)
        return result


class Consent:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Consent':
        assert isinstance(obj, dict)
        return Consent()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class Avatars:
    the_60: str

    def __init__(self, the_60: str) -> None:
        self.the_60 = the_60

    @staticmethod
    def from_dict(obj: Any) -> 'Avatars':
        assert isinstance(obj, dict)
        the_60 = from_str(obj.get("60"))
        return Avatars(the_60)

    def to_dict(self) -> dict:
        result: dict = {}
        result["60"] = from_str(self.the_60)
        return result


class Owner:
    id: str
    screenname: str
    url: str
    username: str
    avatars: Avatars
    type: str
    watermark_image_url: str
    watermark_link_url: None

    def __init__(self, id: str, screenname: str, url: str, username: str, avatars: Avatars, type: str, watermark_image_url: str, watermark_link_url: None) -> None:
        self.id = id
        self.screenname = screenname
        self.url = url
        self.username = username
        self.avatars = avatars
        self.type = type
        self.watermark_image_url = watermark_image_url
        self.watermark_link_url = watermark_link_url

    @staticmethod
    def from_dict(obj: Any) -> 'Owner':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        screenname = from_str(obj.get("screenname"))
        url = from_str(obj.get("url"))
        username = from_str(obj.get("username"))
        avatars = Avatars.from_dict(obj.get("avatars"))
        type = from_str(obj.get("type"))
        watermark_image_url = from_str(obj.get("watermark_image_url"))
        watermark_link_url = from_none(obj.get("watermark_link_url"))
        return Owner(id, screenname, url, username, avatars, type, watermark_image_url, watermark_link_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["screenname"] = from_str(self.screenname)
        result["url"] = from_str(self.url)
        result["username"] = from_str(self.username)
        result["avatars"] = to_class(Avatars, self.avatars)
        result["type"] = from_str(self.type)
        result["watermark_image_url"] = from_str(self.watermark_image_url)
        result["watermark_link_url"] = from_none(self.watermark_link_url)
        return result


class PlayerOwner:
    id: None
    watermark_image_url: None
    watermark_link_url: None

    def __init__(self, id: None, watermark_image_url: None, watermark_link_url: None) -> None:
        self.id = id
        self.watermark_image_url = watermark_image_url
        self.watermark_link_url = watermark_link_url

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerOwner':
        assert isinstance(obj, dict)
        id = from_none(obj.get("id"))
        watermark_image_url = from_none(obj.get("watermark_image_url"))
        watermark_link_url = from_none(obj.get("watermark_link_url"))
        return PlayerOwner(id, watermark_image_url, watermark_link_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_none(self.id)
        result["watermark_image_url"] = from_none(self.watermark_image_url)
        result["watermark_link_url"] = from_none(self.watermark_link_url)
        return result


class Auto:
    type: str
    url: str

    def __init__(self, type: str, url: str) -> None:
        self.type = type
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Auto':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        url = from_str(obj.get("url"))
        return Auto(type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["url"] = from_str(self.url)
        return result


class Qualities:
    auto: List[Auto]

    def __init__(self, auto: List[Auto]) -> None:
        self.auto = auto

    @staticmethod
    def from_dict(obj: Any) -> 'Qualities':
        assert isinstance(obj, dict)
        auto = from_list(Auto.from_dict, obj.get("auto"))
        return Qualities(auto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auto"] = from_list(lambda x: to_class(Auto, x), self.auto)
        return result


class COMScore:
    c2: int
    c3: str
    c4: str

    def __init__(self, c2: int, c3: str, c4: str) -> None:
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    @staticmethod
    def from_dict(obj: Any) -> 'COMScore':
        assert isinstance(obj, dict)
        c2 = int(from_str(obj.get("c2")))
        c3 = from_str(obj.get("c3"))
        c4 = from_str(obj.get("c4"))
        return COMScore(c2, c3, c4)

    def to_dict(self) -> dict:
        result: dict = {}
        result["c2"] = from_str(str(self.c2))
        result["c3"] = from_str(self.c3)
        result["c4"] = from_str(self.c4)
        return result


class Ias:
    anid: int
    partner: str

    def __init__(self, anid: int, partner: str) -> None:
        self.anid = anid
        self.partner = partner

    @staticmethod
    def from_dict(obj: Any) -> 'Ias':
        assert isinstance(obj, dict)
        anid = int(from_str(obj.get("anid")))
        partner = from_str(obj.get("partner"))
        return Ias(anid, partner)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anid"] = from_str(str(self.anid))
        result["partner"] = from_str(self.partner)
        return result


class Tracking:
    internal: str
    history: str
    history_8010_m: str
    behavior_403_m: str

    def __init__(self, internal: str, history: str, history_8010_m: str, behavior_403_m: str) -> None:
        self.internal = internal
        self.history = history
        self.history_8010_m = history_8010_m
        self.behavior_403_m = behavior_403_m

    @staticmethod
    def from_dict(obj: Any) -> 'Tracking':
        assert isinstance(obj, dict)
        internal = from_str(obj.get("internal"))
        history = from_str(obj.get("history"))
        history_8010_m = from_str(obj.get("history@80%|10m"))
        behavior_403_m = from_str(obj.get("behavior@40%|3m"))
        return Tracking(internal, history, history_8010_m, behavior_403_m)

    def to_dict(self) -> dict:
        result: dict = {}
        result["internal"] = from_str(self.internal)
        result["history"] = from_str(self.history)
        result["history@80%|10m"] = from_str(self.history_8010_m)
        result["behavior@40%|3m"] = from_str(self.behavior_403_m)
        return result


class Reporting:
    enable: bool
    tracking: Tracking
    estat: None
    google: None
    ias: Ias
    com_score: COMScore

    def __init__(self, enable: bool, tracking: Tracking, estat: None, google: None, ias: Ias, com_score: COMScore) -> None:
        self.enable = enable
        self.tracking = tracking
        self.estat = estat
        self.google = google
        self.ias = ias
        self.com_score = com_score

    @staticmethod
    def from_dict(obj: Any) -> 'Reporting':
        assert isinstance(obj, dict)
        enable = from_bool(obj.get("enable"))
        tracking = Tracking.from_dict(obj.get("tracking"))
        estat = from_none(obj.get("estat"))
        google = from_none(obj.get("google"))
        ias = Ias.from_dict(obj.get("ias"))
        com_score = COMScore.from_dict(obj.get("comScore"))
        return Reporting(enable, tracking, estat, google, ias, com_score)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enable"] = from_bool(self.enable)
        result["tracking"] = to_class(Tracking, self.tracking)
        result["estat"] = from_none(self.estat)
        result["google"] = from_none(self.google)
        result["ias"] = to_class(Ias, self.ias)
        result["comScore"] = to_class(COMScore, self.com_score)
        return result


class Ar:
    label: str
    urls: List[str]

    def __init__(self, label: str, urls: List[str]) -> None:
        self.label = label
        self.urls = urls

    @staticmethod
    def from_dict(obj: Any) -> 'Ar':
        assert isinstance(obj, dict)
        label = from_str(obj.get("label"))
        urls = from_list(from_str, obj.get("urls"))
        return Ar(label, urls)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_str(self.label)
        result["urls"] = from_list(from_str, self.urls)
        return result


class Data:
    en: Ar
    es: Ar
    pt: Ar
    de: Ar
    zh: Ar
    ar: Ar
    hi: Ar
    ms: Ar
    th: Ar
    id: Ar

    def __init__(self, en: Ar, es: Ar, pt: Ar, de: Ar, zh: Ar, ar: Ar, hi: Ar, ms: Ar, th: Ar, id: Ar) -> None:
        self.en = en
        self.es = es
        self.pt = pt
        self.de = de
        self.zh = zh
        self.ar = ar
        self.hi = hi
        self.ms = ms
        self.th = th
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        en = Ar.from_dict(obj.get("en"))
        es = Ar.from_dict(obj.get("es"))
        pt = Ar.from_dict(obj.get("pt"))
        de = Ar.from_dict(obj.get("de"))
        zh = Ar.from_dict(obj.get("zh"))
        ar = Ar.from_dict(obj.get("ar"))
        hi = Ar.from_dict(obj.get("hi"))
        ms = Ar.from_dict(obj.get("ms"))
        th = Ar.from_dict(obj.get("th"))
        id = Ar.from_dict(obj.get("id"))
        return Data(en, es, pt, de, zh, ar, hi, ms, th, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["en"] = to_class(Ar, self.en)
        result["es"] = to_class(Ar, self.es)
        result["pt"] = to_class(Ar, self.pt)
        result["de"] = to_class(Ar, self.de)
        result["zh"] = to_class(Ar, self.zh)
        result["ar"] = to_class(Ar, self.ar)
        result["hi"] = to_class(Ar, self.hi)
        result["ms"] = to_class(Ar, self.ms)
        result["th"] = to_class(Ar, self.th)
        result["id"] = to_class(Ar, self.id)
        return result


class Subtitles:
    enable: bool
    data: Data

    def __init__(self, enable: bool, data: Data) -> None:
        self.enable = enable
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'Subtitles':
        assert isinstance(obj, dict)
        enable = from_bool(obj.get("enable"))
        data = Data.from_dict(obj.get("data"))
        return Subtitles(enable, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enable"] = from_bool(self.enable)
        result["data"] = to_class(Data, self.data)
        return result


class UI:
    watermark_url: str
    watermark_link_url: None

    def __init__(self, watermark_url: str, watermark_link_url: None) -> None:
        self.watermark_url = watermark_url
        self.watermark_link_url = watermark_link_url

    @staticmethod
    def from_dict(obj: Any) -> 'UI':
        assert isinstance(obj, dict)
        watermark_url = from_str(obj.get("watermark_url"))
        watermark_link_url = from_none(obj.get("watermark_link_url"))
        return UI(watermark_url, watermark_link_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["watermark_url"] = from_str(self.watermark_url)
        result["watermark_link_url"] = from_none(self.watermark_link_url)
        return result


class DailymotionResponseModel:
    url: str
    filmstrip_url: str
    protected_delivery: bool
    channel: str
    created_time: int
    detected_language: str
    duration: int
    explicit: bool
    has_shop_offer: bool
    id: str
    is_created_for_kids: bool
    is_shoppable: bool
    language: str
    media_type: str
    partner: bool
    live_show_viewers: bool
    seeker_url: str
    tags: List[str]
    title: str
    verified: bool
    view_id: str
    mode: str
    private: bool
    data_center: str
    access_id: str
    is_password_protected: bool
    advertising: Advertising
    posters: Dict[str, str]
    owner: Owner
    player_owner: PlayerOwner
    qualities: Qualities
    reporting: Reporting
    sharing: None
    stream_type: str
    subtitles: Subtitles
    ui: UI
    info: Info
    consent: Consent

    def __init__(self, url: str, filmstrip_url: str, protected_delivery: bool, channel: str, created_time: int, detected_language: str, duration: int, explicit: bool, has_shop_offer: bool, id: str, is_created_for_kids: bool, is_shoppable: bool, language: str, media_type: str, partner: bool, live_show_viewers: bool, seeker_url: str, tags: List[str], title: str, verified: bool, view_id: str, mode: str, private: bool, data_center: str, access_id: str, is_password_protected: bool, advertising: Advertising, posters: Dict[str, str], owner: Owner, player_owner: PlayerOwner, qualities: Qualities, reporting: Reporting, sharing: None, stream_type: str, subtitles: Subtitles, ui: UI, info: Info, consent: Consent) -> None:
        self.url = url
        self.filmstrip_url = filmstrip_url
        self.protected_delivery = protected_delivery
        self.channel = channel
        self.created_time = created_time
        self.detected_language = detected_language
        self.duration = duration
        self.explicit = explicit
        self.has_shop_offer = has_shop_offer
        self.id = id
        self.is_created_for_kids = is_created_for_kids
        self.is_shoppable = is_shoppable
        self.language = language
        self.media_type = media_type
        self.partner = partner
        self.live_show_viewers = live_show_viewers
        self.seeker_url = seeker_url
        self.tags = tags
        self.title = title
        self.verified = verified
        self.view_id = view_id
        self.mode = mode
        self.private = private
        self.data_center = data_center
        self.access_id = access_id
        self.is_password_protected = is_password_protected
        self.advertising = advertising
        self.posters = posters
        self.owner = owner
        self.player_owner = player_owner
        self.qualities = qualities
        self.reporting = reporting
        self.sharing = sharing
        self.stream_type = stream_type
        self.subtitles = subtitles
        self.ui = ui
        self.info = info
        self.consent = consent

    @staticmethod
    def from_dict(obj: Any) -> 'DailymotionResponseModel':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        filmstrip_url = from_str(obj.get("filmstrip_url"))
        protected_delivery = from_bool(obj.get("protected_delivery"))
        channel = from_str(obj.get("channel"))
        created_time = from_int(obj.get("created_time"))
        detected_language = from_str(obj.get("detected_language"))
        duration = from_int(obj.get("duration"))
        explicit = from_bool(obj.get("explicit"))
        has_shop_offer = from_bool(obj.get("has_shop_offer"))
        id = from_str(obj.get("id"))
        is_created_for_kids = from_bool(obj.get("is_created_for_kids"))
        is_shoppable = from_bool(obj.get("is_shoppable"))
        language = from_str(obj.get("language"))
        media_type = from_str(obj.get("media_type"))
        partner = from_bool(obj.get("partner"))
        live_show_viewers = from_bool(obj.get("live_show_viewers"))
        seeker_url = from_str(obj.get("seeker_url"))
        tags = from_list(from_str, obj.get("tags"))
        title = from_str(obj.get("title"))
        verified = from_bool(obj.get("verified"))
        view_id = from_str(obj.get("view_id"))
        mode = from_str(obj.get("mode"))
        private = from_bool(obj.get("private"))
        data_center = from_str(obj.get("data_center"))
        access_id = from_str(obj.get("access_id"))
        is_password_protected = from_bool(obj.get("is_password_protected"))
        advertising = Advertising.from_dict(obj.get("advertising"))
        posters = from_dict(from_str, obj.get("posters"))
        owner = Owner.from_dict(obj.get("owner"))
        player_owner = PlayerOwner.from_dict(obj.get("player_owner"))
        qualities = Qualities.from_dict(obj.get("qualities"))
        reporting = Reporting.from_dict(obj.get("reporting"))
        sharing = from_none(obj.get("sharing"))
        stream_type = from_str(obj.get("stream_type"))
        subtitles = Subtitles.from_dict(obj.get("subtitles"))
        ui = UI.from_dict(obj.get("ui"))
        info = Info.from_dict(obj.get("info"))
        consent = Consent.from_dict(obj.get("consent"))
        return DailymotionResponseModel(url, filmstrip_url, protected_delivery, channel, created_time, detected_language, duration, explicit, has_shop_offer, id, is_created_for_kids, is_shoppable, language, media_type, partner, live_show_viewers, seeker_url, tags, title, verified, view_id, mode, private, data_center, access_id, is_password_protected, advertising, posters, owner, player_owner, qualities, reporting, sharing, stream_type, subtitles, ui, info, consent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["filmstrip_url"] = from_str(self.filmstrip_url)
        result["protected_delivery"] = from_bool(self.protected_delivery)
        result["channel"] = from_str(self.channel)
        result["created_time"] = from_int(self.created_time)
        result["detected_language"] = from_str(self.detected_language)
        result["duration"] = from_int(self.duration)
        result["explicit"] = from_bool(self.explicit)
        result["has_shop_offer"] = from_bool(self.has_shop_offer)
        result["id"] = from_str(self.id)
        result["is_created_for_kids"] = from_bool(self.is_created_for_kids)
        result["is_shoppable"] = from_bool(self.is_shoppable)
        result["language"] = from_str(self.language)
        result["media_type"] = from_str(self.media_type)
        result["partner"] = from_bool(self.partner)
        result["live_show_viewers"] = from_bool(self.live_show_viewers)
        result["seeker_url"] = from_str(self.seeker_url)
        result["tags"] = from_list(from_str, self.tags)
        result["title"] = from_str(self.title)
        result["verified"] = from_bool(self.verified)
        result["view_id"] = from_str(self.view_id)
        result["mode"] = from_str(self.mode)
        result["private"] = from_bool(self.private)
        result["data_center"] = from_str(self.data_center)
        result["access_id"] = from_str(self.access_id)
        result["is_password_protected"] = from_bool(self.is_password_protected)
        result["advertising"] = to_class(Advertising, self.advertising)
        result["posters"] = from_dict(from_str, self.posters)
        result["owner"] = to_class(Owner, self.owner)
        result["player_owner"] = to_class(PlayerOwner, self.player_owner)
        result["qualities"] = to_class(Qualities, self.qualities)
        result["reporting"] = to_class(Reporting, self.reporting)
        result["sharing"] = from_none(self.sharing)
        result["stream_type"] = from_str(self.stream_type)
        result["subtitles"] = to_class(Subtitles, self.subtitles)
        result["ui"] = to_class(UI, self.ui)
        result["info"] = to_class(Info, self.info)
        result["consent"] = to_class(Consent, self.consent)
        return result


def dailymotion_response_model_from_dict(s: Any) -> DailymotionResponseModel:
    return DailymotionResponseModel.from_dict(s)


def dailymotion_response_model_to_dict(x: DailymotionResponseModel) -> Any:
    return to_class(DailymotionResponseModel, x)
