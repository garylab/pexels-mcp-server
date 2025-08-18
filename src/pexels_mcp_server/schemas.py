from typing import Optional
from pydantic import BaseModel, Field


class PhotosSearchRequest(BaseModel):
    query: str = Field(..., description="Search query")
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    orientation: Optional[str] = Field(
        None, description="landscape | portrait | square"
    )
    size: Optional[str] = Field(None, description="large | medium | small")
    color: Optional[str] = Field(None, description="Color name or hex (e.g. #ff0000)")
    locale: Optional[str] = Field(None, description="Locale, e.g. en-US")


class PhotosCuratedRequest(BaseModel):
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")


class PhotoGetRequest(BaseModel):
    id: int = Field(..., description="Photo ID")


class VideosSearchRequest(BaseModel):
    query: str = Field(..., description="Search query")
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    orientation: Optional[str] = Field(
        None, description="landscape | portrait | square"
    )
    size: Optional[str] = Field(None, description="large | medium | small")
    locale: Optional[str] = Field(None, description="Locale, e.g. en-US")


class VideosPopularRequest(BaseModel):
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")
    min_width: Optional[int] = Field(None, description="Minimum video width")
    min_height: Optional[int] = Field(None, description="Minimum video height")
    min_duration: Optional[int] = Field(None, description="Minimum duration in seconds")
    max_duration: Optional[int] = Field(None, description="Maximum duration in seconds")


class VideoGetRequest(BaseModel):
    id: int = Field(..., description="Video ID")


class CollectionsFeaturedRequest(BaseModel):
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")


class CollectionsMediaRequest(BaseModel):
    id: str = Field(..., description="Collection ID")
    type: Optional[str] = Field(None, description="photos | videos | all")
    per_page: Optional[int] = Field(15, ge=1, le=80, description="Results per page")
    page: Optional[int] = Field(1, ge=1, description="Page number")
