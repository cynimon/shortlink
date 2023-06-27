import uvicorn
from fastapi import FastAPI

config = get_config()

app = FastAPI(title="Shortlink", description="Link shortener app")


if __name__ == "__main__":
    uvicorn.run('main:app', host=config.SERVER_HOST, port=config.SERVER_PORT, reload=True)