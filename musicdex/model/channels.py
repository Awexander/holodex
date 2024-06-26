from typing import Optional
from attrs import define


@define(kw_only=True)
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    english_name: Optional[str] = None
    type: Optional[str] = None
    org: Optional[str] = None
    suborg: Optional[str] = None
    group: Optional[str] = None
    lang: Optional[str] = None
    photo: Optional[str] = None
    twitter: Optional[str] = None
    video_count: Optional[int] = None
    subscriber_count: Optional[int] = None
    clip_count: Optional[int] = None
    top_topics: Optional[list[str]] = None
    inactive: Optional[bool] = None
    twitch: Optional[str] = None
    extra_ids: Optional[str] = None
