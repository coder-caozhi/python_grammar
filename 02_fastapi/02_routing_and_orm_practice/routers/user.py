"""
路由分发
"""
from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["用户管理"]
)

@router.get("/")
def get_all_users():
    return {"message": "获取所有的用户列表"}

@router.get("/{user_id}")
async def get_by_user_id(user_id: int):
    return {"message": f"获取用户ID为{user_id}的信息"}