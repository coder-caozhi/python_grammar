from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["商品管理"]
)

@router.get("/")
async def get_all_item():
    return {"message": "获取所有的商品列表"}

@router.get("/{item_id}")
async def get_by_item_id(item_id: int):
    return {"message": f"获取商品ID为{item_id}的商品"}