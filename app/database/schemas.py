from pydantic import BaseModel, HttpUrl


class LongLinkSchema(BaseModel):
    url: HttpUrl

    class Config:
        schema_extra = {
            "example":
                {
                    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                }
        }


class ShortLinkSchema(BaseModel):
    url: str

    class Config:
        schema_extra = {
            "example":
                {
                    "url": "example.com/TdMY"
                }
        }
