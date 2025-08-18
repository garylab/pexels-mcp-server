from enum import StrEnum


class PexelsTools(StrEnum):
    PHOTOS_SEARCH = "photos_search"
    PHOTOS_CURATED = "photos_curated"
    PHOTO_GET = "photo_get"
    VIDEOS_SEARCH = "videos_search"
    VIDEOS_POPULAR = "videos_popular"
    VIDEO_GET = "video_get"
    COLLECTIONS_FEATURED = "collections_featured"
    COLLECTIONS_MEDIA = "collections_media"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_
