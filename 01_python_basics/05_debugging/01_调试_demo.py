# =====================================================================
# 01. 调试练习 Demo —— 学生成绩分析器
# ---------------------------------------------------------------------
# 【这个文件是干什么的】
#   一个能跑起来、但故意埋了 5 个 bug 的小程序。
#   你可以用调试器打断点、单步执行、看变量，把 bug 一个个找出来。
#
# 【怎么运行】
#   python 01.调试demo.py        # 依次运行 5 个阶段
#   python 01.调试demo.py 1      # 只运行阶段 1
#   python 01.调试demo.py 4      # 只运行阶段 4
#
# 【怎么练习】
#   打开 README.md，按照里面的 5 个任务操作。
#   每个阶段都有一个 ★ 练习点，建议在那里打断点。
# =====================================================================

import sys
import traceback

# 7 名学生，每人 3 门课的成绩
STUDENTS = [
    {"name": "张三", "class_name": "一班", "scores": [88, 92, 79]},
    {"name": "李四", "class_name": "二班", "scores": [95, 67, 84]},
    {"name": "王五", "class_name": "一班", "scores": [72, 90, 85]},
    {"name": "赵六", "class_name": "二班", "scores": [60, 78, 91]},
    {"name": "钱七", "class_name": "三班", "scores": [99, 88, 94]},
    {"name": "孙八", "class_name": "三班", "scores": [50, 55, 58]},
    {"name": "周九", "class_name": "一班", "scores": [45, 62, 51]},
]


# ---------------------------------------------------------------------
# 阶段 1：计算全班平均分
# 调试任务：在循环里观察 total / count，看看平均分为什么不对
# ---------------------------------------------------------------------
def stage1_average(students):
    print("开始计算全班平均分 ...")

    total = 0
    count = 0
    for student in students:
        total += sum(student["scores"])
        count += 1                      # ★ 练习点 1

    average = total / count
    print(f"总分: {total}，参与计算的分数个数: {count}")
    print(f"全班平均分: {average:.2f}")
    return average


# ---------------------------------------------------------------------
# 阶段 2：找总分最高的学生
# 调试任务：练习“异常断点”，看看 IndexError 到底是从哪来的
# ---------------------------------------------------------------------
def stage2_top_student(students):
    print("开始查找总分最高的学生 ...")

    top = students[0]
    for i in range(1, len(students) + 1):   # ★ 练习点 2
        current = students[i]
        if sum(current["scores"]) > sum(top["scores"]):
            top = current

    print(f"总分最高: {top['name']}，总分: {sum(top['scores'])}")
    return top


# ---------------------------------------------------------------------
# 阶段 3：按班级分组
# 调试任务：连续调用两次，看看第二次的结果为什么“带着上一次的数据”
# ---------------------------------------------------------------------
def stage3_group_by_class(students, groups={}):     # ★ 练习点 3
    for student in students:
        class_name = student["class_name"]
        groups.setdefault(class_name, []).append(student["name"])
    return groups


def run_stage3():
    print("第一次：传入全部学生")
    first = stage3_group_by_class(STUDENTS)
    print(f"分组结果: {first}")

    print("\n第二次：只传入二班学生")
    second_batch = [s for s in STUDENTS if s["class_name"] == "二班"]
    second = stage3_group_by_class(second_batch)
    print(f"分组结果: {second}")


# ---------------------------------------------------------------------
# 阶段 4：二分查找（递归）
# 调试任务：练习“单步进入”和“调用栈”，观察 left / right / mid 的变化
# ---------------------------------------------------------------------
SORTED_SCORES = sorted(score for student in STUDENTS for score in student["scores"])


def binary_search(scores, target, left=0, right=None):
    if right is None:
        right = len(scores) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if scores[mid] == target:
        return mid
    if scores[mid] < target:
        return binary_search(scores, target, mid, right)       # ★ 练习点 4
    return binary_search(scores, target, left, mid - 1)


def run_stage4():
    print(f"有序分数: {SORTED_SCORES}")

    target = 92
    index = binary_search(SORTED_SCORES, target)
    print(f"查找 {target}: 下标 {index}，值 {SORTED_SCORES[index]}")

    print("\n再查找一个不存在的分数 100 ...")
    index = binary_search(SORTED_SCORES, 100)
    print(f"查找 100: 下标 {index}")


# ---------------------------------------------------------------------
# 阶段 5：剔除不及格的学生
# 调试任务：在循环中观察列表长度和下标，看看谁被“跳过”了
# ---------------------------------------------------------------------
def stage5_remove_failed(students, pass_line=60):
    print(f"开始剔除平均分低于 {pass_line} 的学生 ...")

    i = 0
    while i < len(students):
        student = students[i]
        average = sum(student["scores"]) / len(student["scores"])
        if average < pass_line:
            print(f"  剔除 {student['name']}（平均分 {average:.2f}）")
            students.pop(i)
        i += 1                          # ★ 练习点 5

    return students


def run_stage5():
    # 传副本，避免影响后面的阶段（字典本身不会被修改）
    remaining = stage5_remove_failed(STUDENTS.copy())
    names = [student["name"] for student in remaining]
    print(f"剩余 {len(remaining)} 人: {names}")


# ---------------------------------------------------------------------
# 运行入口
# ---------------------------------------------------------------------
STAGES = {
    "1": ("阶段 1：计算平均分", lambda: stage1_average(STUDENTS)),
    "2": ("阶段 2：找总分最高的学生", lambda: stage2_top_student(STUDENTS)),
    "3": ("阶段 3：按班级分组", run_stage3),
    "4": ("阶段 4：二分查找（递归）", run_stage4),
    "5": ("阶段 5：剔除不及格学生", run_stage5),
}


def main():
    choice = sys.argv[1] if len(sys.argv) > 1 else "all"
    if choice != "all" and choice not in STAGES:
        print("用法: python 01.调试demo.py [all|1|2|3|4|5]")
        return

    failed = []
    for key, (title, run) in STAGES.items():
        if choice not in ("all", key):
            continue

        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

        try:
            run()
        except Exception as exc:
            failed.append(key)
            print(f"\n[阶段 {key} 抛出异常] {type(exc).__name__}: {exc}")
            print("提示：在异常发生的位置打断点，或者开启“异常断点”再运行一次。")
            traceback.print_exc(limit=6)

    if choice == "all":
        print("\n" + "=" * 60)
        if failed:
            print(f"运行结束，阶段 {', '.join(failed)} 抛出了异常。")
        else:
            print("运行结束。结果都和预期一致吗？对照 README.md 检查一下。")
        print("=" * 60)


if __name__ == "__main__":
    main()
