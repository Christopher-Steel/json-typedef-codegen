# Code generated by jtd-codegen for Python v0.3.1

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Type, Union, get_args, get_origin


@dataclass
class Root:
    foo: 'str'

    @classmethod
    def from_json_data(cls, data: Any) -> 'Root':
        variants: Dict[str, Type[Root]] = {
            "BAR_BAZ": RootBarBaz,
            "QUUX": RootQuux,
        }

        return variants[data["foo"]].from_json_data(data)

    def to_json_data(self) -> Any:
        pass

@dataclass
class RootBarBaz(Root):
    baz: 'str'

    @classmethod
    def from_json_data(cls, data: Any) -> 'RootBarBaz':
        return cls(
            "BAR_BAZ",
            _from_json_data(str, data.get("baz")),
        )

    def to_json_data(self) -> Any:
        data = { "foo": "BAR_BAZ" }
        data["baz"] = _to_json_data(self.baz)
        return data

@dataclass
class RootQuux(Root):
    quuz: 'str'

    @classmethod
    def from_json_data(cls, data: Any) -> 'RootQuux':
        return cls(
            "QUUX",
            _from_json_data(str, data.get("quuz")),
        )

    def to_json_data(self) -> Any:
        data = { "foo": "QUUX" }
        data["quuz"] = _to_json_data(self.quuz)
        return data

def _from_json_data(cls: Any, data: Any) -> Any:
    if data is None or cls in [bool, int, float, str, object] or cls is Any:
        return data
    if cls is datetime:
        return _parse_rfc3339(data)
    if get_origin(cls) is Union:
        return _from_json_data(get_args(cls)[0], data)
    if get_origin(cls) is list:
        return [_from_json_data(get_args(cls)[0], d) for d in data]
    if get_origin(cls) is dict:
        return { k: _from_json_data(get_args(cls)[1], v) for k, v in data.items() }
    return cls.from_json_data(data)

def _to_json_data(data: Any) -> Any:
    if data is None or type(data) in [bool, int, float, str, object]:
        return data
    if type(data) is datetime:
        return data.isoformat()
    if type(data) is list:
        return [_to_json_data(d) for d in data]
    if type(data) is dict:
        return { k: _to_json_data(v) for k, v in data.items() }
    return data.to_json_data()

def _parse_rfc3339(s: str) -> datetime:
    datetime_re = r'^(\d{4})-(\d{2})-(\d{2})[tT](\d{2}):(\d{2}):(\d{2})(\.\d+)?([zZ]|((\+|-)(\d{2}):(\d{2})))$'
    match = re.match(datetime_re, s)
    if not match:
        raise ValueError('Invalid RFC3339 date/time', s)

    (year, month, day, hour, minute, second, frac_seconds, offset,
     *tz) = match.groups()

    frac_seconds_parsed = None
    if frac_seconds:
        frac_seconds_parsed = int(float(frac_seconds) * 1_000_000)
    else:
        frac_seconds_parsed = 0

    tzinfo = None
    if offset == 'Z':
        tzinfo = timezone.utc
    else:
        hours = int(tz[2])
        minutes = int(tz[3])
        sign = 1 if tz[1] == '+' else -1

        if minutes not in range(60):
            raise ValueError('minute offset must be in 0..59')

        tzinfo = timezone(timedelta(minutes=sign * (60 * hours + minutes)))

    second_parsed = int(second)
    if second_parsed == 60:
        second_parsed = 59

    return datetime(int(year), int(month), int(day), int(hour), int(minute),
                    second_parsed, frac_seconds_parsed, tzinfo)            
