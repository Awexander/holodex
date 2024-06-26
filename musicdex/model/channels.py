from typing import Optional
from attrs import define


@define(kw_only=True)
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    english_name: Optional[str] = None
    description: Optional[str] = None
    photo: Optional[str] = None
    thumbnail: Optional[str] = None
    banner: Optional[str] = None
    org: Optional[str] = None
    suborg: Optional[str] = None
    lang: Optional[str] = None
    published_at: Optional[str] = None
    view_count: Optional[int] = None
    video_count: Optional[int] = None
    subscriber_count: Optional[int] = None
    comments_crawled_at: Optional[str] = None
    updated_at: Optional[str] = None
    yt_uploads_id: Optional[str] = None
    crawled_at: Optional[str] = None
    type: Optional[str] = None
    clip_count: Optional[int] = None
    twitter: Optional[str] = None
    inactive: Optional[bool] = None
    created_at: Optional[str] = None
    top_topics: Optional[list[str]] = None
    yt_handle: Optional[list[str]] = None
    twitch: Optional[str] = None
    yt_name_history: Optional[list[str]] = None
    extra_ids: Optional[str] = None
    index_all: Optional[bool] = None
    group: Optional[str] = None
