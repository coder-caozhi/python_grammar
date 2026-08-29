"""
- 保存学生成绩
- 修改成绩
- 统计：平均分、优秀学生名单、Top3、分组（及格/不及格）
"""
students = [
    {"name": "王飞龙", "score": 88},
    {"name": "丁一", "score": 20},
    {"name": "王海洋", "score": 99},
    {"name": "刘永佳", "score": 68},
    {"name": "刘益行", "score": 8},
]


# 添加学生是函数
def add_stu(stus, name, score):
    stus.append({"name": name, "score": score})

# 修改学生成绩的函数
def modify_score(stus, name, score):
    flag = False
    # 遍历所有的学生
    for stu in stus:
        if stu["name"] == name:
            stu["score"] = score
            flag = True
    return flag
# 统计学生信息
def report_stu(stus):
    if not stus:
        return {"平均分":0,"优秀学生名单":[],"前三名":[],"及格/不及格情况":{}}

    # 获取平均分
    avg = sum(s["score"] for s in stus) / len(stus)

    # 获取优秀学生名单
    exec_stu = [s["name"] for s in stus if s["score"] > 90]

    # 获取Top3
    top3 = [sorted(stus,key=lambda x:x["score"],reverse=True)[:3]]

    # 分组统计及格/不及格情况
    group = {}
    # 遍历列表
    for s in stus:
        # 三元运算符
        key = "及格" if s["score"] >= 60 else "不及格"
        group.setdefault(key,[]).append(s["name"])

    return {"平均分":round(avg,2),"优秀学生名单":exec_stu,"前三名":top3,"及格/不及格情况":group}

# 添加学生
add_stu(students,"王飞龙",66)

# 修改学生分数
# modify_score(students,"王飞龙",56)

# 统计
result = report_stu(students)

print(result)