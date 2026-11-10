import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from routers import user, item # 手动套入 其他文件夹的模块

# 3.2.1 创建新的项目
app = FastAPI(title="路由分发demo")

app.include_router(user.router)

app.include_router(item.router)

@app.get("/")
async def root():
    return {"hello world"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 3.3.1 声明路径参数
# @app.get("/items/{item_id}")
async def read_item_id(item_id: int):
    return {"item_id": type(item_id).__name__}

# 3.3.3 参数顺序
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# 3.4.1 url带查询参数
items_list = [{"item1": "Foo"}, {"item2":"Bar"},{"item3":"Baz"}] # 用于数据查询
@app.get("/items/")
async def read_item(start: int, limit: int):
    return items_list[start : start + limit]

# 3.4.3 可选的查询参数
# @app.get("/items/{item_id}")
async def read_item_optional(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 3.4.4 查询参数bool类型转换说明
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, short: bool = False):
    item: dict[str, int | str] = {"item": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "this a description message"})
    return item

# 3.4.5 多个路径和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "这是描述信息"})
    return item

# 3.5请求传参
class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float

@app.post("/items/") #注意请求方式是post（post方式请求的数据在地址栏不会显示）
async def create_item(item: Item):
    return item




if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8002,
        reload=True
    )