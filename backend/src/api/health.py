from fastapi import APIRouter


router = APIRouter()


@router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `data = await get_all_datas()`
    return {"ping": "pong!"}
