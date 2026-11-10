# =====================================================================
# 05. 测试数据校验神器 —— pydantic
# ---------------------------------------------------------------------
# 【为什么需要它】类型注解（04 文件）只能提示、不会校验。
#                 pydantic 能把"注解"变成"真正的运行时校验"
# 【安装】pip install pydantic
# 【核心用法】
#     1. 定义一个类，继承 BaseModel
#     2. 用"类型注解"声明字段
#     3. 用 Field(...) 追加约束（长度、范围、说明）
#     4. 实例化时自动校验，不合法就抛 ValidationError
# 【Field 里的 "..."】表示这个字段是"必填"，等价于 required=True
# 【常见场景】接口入参校验、配置文件解析、ORM 前的数据清洗
# =====================================================================

from pydantic import BaseModel, Field, ValidationError


# ---------------------------------------------------------------------
# 一、定义数据模型
# ---------------------------------------------------------------------
print("=" * 40)
print("一、定义数据模型")
print("=" * 40)


class User(BaseModel):
    id: int = Field(...)          # ... 表示必填
    name: str = Field(..., min_length=3, max_length=8,
                      description="设置长度为3-8位的用户名")
    age: int = Field(..., ge=0, le=116,
                     description="年龄的范围是0到116对")

# Field 的常用约束记一下：
#   必填         ...            （Ellipsis）
#   字符串长度    min_length / max_length
#   数值范围      ge >=  /  le <=   （gt >  /  lt <）
#   默认值        Field(default=xxx)
#   字段说明      description="..."
#
# 注意：这里的 __init__ 不需要自己写，pydantic 会按字段自动生成


# ---------------------------------------------------------------------
# 二、用字典来构造对象（自动触发校验）
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 40)
    print("二、校验数据")
    print("=" * 40)

    # 准备一份"待校验"的数据
    user_dict = {
        "id": 1,
        "name": "王",             # 只有 1 个字，不满足 min_length=3 → 校验失败
        "age": 24
    }

    try:
        # **user_dict 是解包传参：
        #     User(**user_dict) 等价于 User(id=1, name="王", age=24)
        # 这一步就会执行 pydantic 的校验逻辑
        user = User(**user_dict)

        # 校验通过，可以把对象序列化成 JSON 字符串
        user_to_json = user.model_dump_json()
        print(f"校验成功之后的User对象转换成的JSON字符串是：{user_to_json}")
    except ValidationError as e:
        # 校验失败：e 里包含"哪个字段、为什么失败"的详细信息
        print(f"校验失败，失败的原因是：{e}")
    else:
        # 只有 try 完全没出错才会走到这里
        print("校验成功")
    finally:
        print("神器真好用")

    # 当前数据里 name 只有一个字，所以输出：
    #   校验失败，失败的原因是：1 validation error for User
    #   name
    #     String should have at least 3 characters [type=string_too_short, ...]
    #   神器真好用
    #
    # 把 name 改成 "王飞龙" 再跑，就会变成：
    #   校验成功之后的User对象转换成的JSON字符串是：{"id":1,"name":"王飞龙","age":24}
    #   校验成功
    #   神器真好用


# ---------------------------------------------------------------------
# 三、其他常用能力（了解即可）
# ---------------------------------------------------------------------
#   user.model_dump()          → 转成 dict
#   user.model_dump_json()     → 转成 JSON 字符串（本文件用的这个）
#   User.model_validate(dict)  → 从字典校验并创建对象
#   User.model_json_schema()   → 导出 JSON Schema，可以直接给前端用
#
# 题外话：pydantic v1 的写法是 user.dict() / user.json()，v2 改成了
#         model_dump / model_dump_json，网上老教程看到 v1 写法别照抄
