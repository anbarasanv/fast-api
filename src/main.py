from fastapi import FastAPI
from starlette.routing import Route
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
import uvicorn

# Creating APP
app = FastAPI()


async def home_page(request):
    return JSONResponse({"Hello": "Hi are you?"})


routes = [
    Route('/', endpoint=home_page, methods=['GET'])
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
