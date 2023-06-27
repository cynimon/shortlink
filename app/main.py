import uvicorn
from fastapi import FastAPI

from app.config import get_config

settings = get_config()

app = FastAPI(title="Shortlink", description="Link shortener app")


if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
