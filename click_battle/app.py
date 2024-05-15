from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette import status
import redis.asyncio as redis
from click_battle.template_generation import generate_main_page

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    r = get_redis_connection(request)
    left = await read_int(r, f"{request.app.state.prefix}:left_score")
    right = await read_int(r, f"{request.app.state.prefix}:right_score")

    return generate_main_page(left, right)


@router.post("/score_left")
async def click_left(request: Request):
    r = get_redis_connection(request)
    await r.incr(f"{request.app.state.prefix}:left_score")
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


@router.post("/score_right")
async def click_right(request: Request):
    r = get_redis_connection(request)
    await r.incr(f"{request.app.state.prefix}:right_score")
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


async def read_int(r, key):
    value = await r.get(key)
    value = value if value is not None else 0

    return int(value)


def get_redis_connection(request):
    p = request.app.state.redis_pool
    r = redis.Redis.from_pool(p)
    r.auto_close_connection_pool = False

    return r


@asynccontextmanager
async def create_db(app):
    app.state.redis_pool = redis.ConnectionPool.from_url("redis://localhost:6379")
    yield
    await app.state.redis_pool.disconnect(inuse_connections=True)


def create_app(prefix="main"):
    app = FastAPI(lifespan=create_db)
    app.state.prefix = prefix
    app.state.redis_pool = None
    app.include_router(router)
    return app
