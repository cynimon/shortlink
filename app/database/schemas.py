from pydantic import BaseModel, HttpUrl, AnyUrl


class LongLinkSchema(BaseModel):
    url: HttpUrl

    class Config:
        schema_extra = {
            "example":
                {
                    "url": "https://www.clark.com/"
                }
        }


class ShortLinkSchema(BaseModel):
    url: AnyUrl
