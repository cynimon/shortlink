import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import Response

from app.config import get_config
from app.dependencies import DBSession

settings = get_config()

app = FastAPI(title="Shortlink", description="Link shortener app")


@app.post("/", status_code=status.HTTP_201_CREATED)
def add_link(db_session: DBSession):
    """Add long link to database and get connected short link"""
    pass


@app.get("/{short_url}", status_code=status.HTTP_200_OK)
def get_full_link(db_session: DBSession):
    """Get long link by the short one"""
    pass


@app.delete("/{short_url}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(db_session: DBSession) -> Response:
    """Delete link object by short link"""
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
