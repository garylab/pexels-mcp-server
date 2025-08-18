from typing import Optional
from pydantic import BaseModel, Field


class PhotosSearchRequest(BaseModel):
    query: str = Field(..., description="Search query")
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )
    orientation: Optional[str] = Field(
        None,
        pattern=r"^(landscape|portrait|square)$",
        description="landscape | portrait | square",
    )
    size: Optional[str] = Field(
        None, pattern=r"^(large|medium|small)$", description="large | medium | small"
    )
    color: Optional[str] = Field(
        None,
        pattern=r"^[a-zA-Z]+$|^#[0-9a-fA-F]{6}$",
        description="Color name or hex (e.g. #ff0000)",
    )
    locale: Optional[str] = Field(
        None, pattern=r"^[a-z]{2}-[A-Z]{2}$", description="Locale, e.g. en-US"
    )


class PhotosCuratedRequest(BaseModel):
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )


class PhotoGetRequest(BaseModel):
    id: str = Field(
        ..., pattern=r"^[1-9]\d*$", description="Photo ID (string, positive integer)"
    )


class VideosSearchRequest(BaseModel):
    query: str = Field(..., description="Search query")
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )
    orientation: Optional[str] = Field(
        None,
        pattern=r"^(landscape|portrait|square)$",
        description="landscape | portrait | square",
    )
    size: Optional[str] = Field(
        None, pattern=r"^(large|medium|small)$", description="large | medium | small"
    )
    locale: Optional[str] = Field(
        None, pattern=r"^[a-z]{2}-[A-Z]{2}$", description="Locale, e.g. en-US"
    )


class VideosPopularRequest(BaseModel):
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )
    min_width: Optional[str] = Field(
        None,
        pattern=r"^[1-9]\d*$",
        description="Minimum video width (string, positive integer)",
    )
    min_height: Optional[str] = Field(
        None,
        pattern=r"^[1-9]\d*$",
        description="Minimum video height (string, positive integer)",
    )
    min_duration: Optional[str] = Field(
        None,
        pattern=r"^[1-9]\d*$",
        description="Minimum duration in seconds (string, positive integer)",
    )
    max_duration: Optional[str] = Field(
        None,
        pattern=r"^[1-9]\d*$",
        description="Maximum duration in seconds (string, positive integer)",
    )


class VideoGetRequest(BaseModel):
    id: str = Field(
        ..., pattern=r"^[1-9]\d*$", description="Video ID (string, positive integer)"
    )


class CollectionsFeaturedRequest(BaseModel):
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )


class CollectionsMediaRequest(BaseModel):
    id: str = Field(..., description="Collection ID")
    type: Optional[str] = Field(
        None, pattern=r"^(photos|videos|all)$", description="photos | videos | all"
    )
    per_page: Optional[str] = Field(
        "15",
        pattern=r"^([1-9]|[1-7][0-9]|80)$",
        description="Results per page (string, 1-80)",
    )
    page: Optional[str] = Field(
        "1", pattern=r"^[1-9]\d*$", description="Page number (string, minimum 1)"
    )
