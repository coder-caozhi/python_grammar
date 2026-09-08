# 类型注解只能静态提示，不能动态校验
from typing import List, Dict, Optional, Union, Any

name: str = "王飞龙"
print(name)
age: int = 24
print(age)
hobby: list[str] = ["男","打台球","唱歌"]
print(hobby)
girl_friends: List[str] = ["a","b","c"]
print(girl_friends)
score: Dict[str,float] = {
    "java": 88.88,
    "python": 66.66
}
print(score)
gender: str | None = None          # Python 3.10+ 的现代简写
gender: Optional[str] = None       # typing 里的传统写法，完全等价
gender: Union[str, None] = None    # Union 写法，同样等价
email: Optional[str] = "wangfeilong@qq.com"
print(email)
salary: int|float = 88888
print(salary)
address: Union[str,list] = "宏福苑"
print(address)
id: Any = 110001201901010019
print(id)

