from pydantic import BaseModel, HttpUrl, validator


class LongLinkSchema(BaseModel):
    url: HttpUrl

    class Config:
        schema_extra = {
            "example":
                {
                    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                }
        }

    @validator('url')
    def check_lower(cls, value):
        return value.lower()


class ShortLinkSchema(BaseModel):
    url: str

    class Config:
        schema_extra = {
            "example":
                {
                    "url": "example.com/TdMY"
                }
        }
