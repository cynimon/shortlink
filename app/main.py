import uvicorn
from fastapi import FastAPI, status, HTTPException, Query
from fastapi.responses import Response
from sqlalchemy.exc import NoResultFound

from app.config import get_config
from app.dependencies import DBSession
from app.database import service, schemas
from app import service as app_service

settings = get_config()

app = FastAPI(title="Shortlink", description="Link shortener app")


@app.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShortLinkSchema, tags=["Links"],
          responses={
              409: {
                  "description": "Duplicate link",
                  "content": {
                      "application/json": {
                          "example": {"message": "Link for this URL already exist"}
                      }
                  },
              },
          },
          )
def add_link(db_session: DBSession, data: schemas.LongLinkSchema) -> schemas.ShortLinkSchema:
    """Add long link to database and get connected short link"""
    if service.url_exists(db_session, data):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"message": "Link for this URL already exist"})
    else:
        link_object = service.add_new_link(db_session=db_session, link_object=data)
        short_link = app_service.get_short_link(link_object=link_object)
        service.add_short_link(db_session=db_session, short_link=short_link, link_object=link_object)

    return {"url": short_link}


@app.get("/", status_code=status.HTTP_200_OK, response_model=schemas.LongLinkSchema, tags=["Links"],
         responses={
             404: {
                 "description": "Link not found",
                 "content": {
                     "application/json": {
                         "example": {"message": "This URL does not exist"}
                     }
                 },
             },
         },
         )
def get_full_link(db_session: DBSession, short_url: str = Query()) -> schemas.LongLinkSchema:
    """Get long link by the short one"""
    try:
        long_link = service.get_long_link_by_short(db_session=db_session, short_link=short_url)
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": "This URL does not exist"})

    return {"url": long_link}


@app.delete("/", status_code=status.HTTP_204_NO_CONTENT, tags=["Links"], response_class=Response,
            response_description="Successfully deleted")
def delete_link(db_session: DBSession, short_url: str = Query()) -> Response:
    """Delete link object by short link"""
    service.delete_link_by_short_url(db_session=db_session, short_link=short_url)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
