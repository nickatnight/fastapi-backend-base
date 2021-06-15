from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter


router = APIRouter()


@router.get("/ping", tags=["health"], dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def pong():
    # some async operation could happen here
    # example: `data = await get_all_datas()`
    return {"ping": "pong!"}
