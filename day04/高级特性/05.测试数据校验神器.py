from pydantic import BaseModel,Field,ValidationError

class User(BaseModel):
    id: int = Field(...)
    name: str = Field(... ,min_length=3,max_length=8,description="设置长度为3-8位的用户名")
    age: int = Field(...,ge=0,le=116,description="年龄的范围是0到116对")


if __name__ == "__main__":
    # 定义一个字典
    user_dict = {
        "id":1,
        "name":"王",
        "age":24
    }
    try:
        # 实例化，同时解包传参
        user = User(**user_dict)
        # 将对象转换位JSON字符
        user_to_json = user.model_dump_json()
        print(f"校验成功之后的User对象转换成的JSON字符串是：{user_to_json}")
    except ValidationError as e:
        print(f"校验失败，失败的原因是：{e}")
    else:
        print("校验成功")
    finally:
        print("神器真好用")
