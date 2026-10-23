"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
"""
1. 编写函数get_mondays(start_date: str, n: int)接收一个起始日期（字符串格式 YYYY-MM-DD）和天数 N，完成：
- 把字符串转为 datetime 日期对象
- 生成从起始日期开始 未来 N 天 的所有日期
- 筛选出其中所有周一的日期
- 返回周一日期列表
    输入：start_date="2025-01-01", N=30
    输出：["2025-01-06", "2025-01-13", "2025-01-20", "2025-01-27"]

"""
from datetime import datetime
from datetime import timedelta
def get_mondays(start_date: str, n: int)->list:
    datetime_obj = datetime.strptime(start_date, "%Y-%m-%d")
    dates_list = [(datetime_obj + timedelta(days=i)).date() for i in range(n+1)]
    mondays = [d.strftime("%Y-%m-%d") for d in dates_list if d.weekday()==0]
    return mondays

print(get_mondays("2025-01-01", 30))
#[datetime.date(2025, 1, 6), datetime.date(2025, 1, 13), datetime.date(2025, 1, 20), datetime.date(2025, 1, 27)]